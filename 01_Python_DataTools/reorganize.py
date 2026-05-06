"""
reorganize.py — Flatten MOD_1 lesson sub-folders into clean per-section notebooks.

What it does
------------
For each section folder (S1–S10) it:
  1. Finds every `dsc-*` lesson sub-folder (sorted alphabetically).
  2. Picks the lesson notebook (index.ipynb > README.ipynb, or skips).
  3. Copies it to the section root as  S{N}_{seq:02d}_{lesson_name}.ipynb
  4. Moves image/output assets -> assets/{lesson_shortname}/
  5. Moves data files           -> data/{lesson_shortname}/
  6. Rewrites paths inside the notebook JSON accordingly.
  7. Deletes the lesson sub-folder (all boilerplate gone).

Run with --dry-run first to preview changes without touching anything.

Usage
-----
  python reorganize.py [--dry-run] [--root PATH]
"""

import argparse
import json
import os
import re
import shutil
import stat
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

# Lesson sub-folder suffixes to strip when deriving a clean name
_STRIP_SUFFIXES = [
    "-onl01-dtsc-ft-030220",
    "-onl01-dtsc-pt-030220",
    "-v2-1",
    "-v2",
    "-lab",          # keep "lab" in name but strip duplicates below
]

# File extensions treated as data (moved to data/)
DATA_EXTS = {".csv", ".tsv", ".xlsx", ".xls", ".sqlite", ".db",
             ".json", ".sql", ".txt", ".pdf"}

# File extensions treated as images/assets (moved to assets/)
ASSET_EXTS = {".png", ".jpg", ".jpeg", ".gif", ".svg", ".pdf",
              ".html", ".htm", ".css", ".gif"}

# Sub-folder names inside a lesson that contain assets
ASSET_DIRS = {"images", "index_files", "plotly_files", "figures"}

# Boilerplate files to delete (exact names, case-insensitive)
BOILERPLATE = {
    "readme.md", "contributing.md", "license.md",
    ".gitignore", ".learn", ".canvas", ".deploy",
    ".hints", ".redeploy", ".rspec", ".answers",
    ".ds_store", "gemfile", "gemfile.lock",
    "environment.yml", "windows.yml", "bp.txt",
    "test_index.py",
}

# Boilerplate name patterns (fnmatch style)
BOILERPLATE_PATTERNS = [
    "*.md~*",   # git-tracked backup files like LICENSE.md~abc123
    ".learn~*",
]

# Lesson sub-folders that are NOT dsc-* but should be kept as-is
KEEP_SUBDIRS = {"airport_database", "chinook_database", "additional-topic-plotly"}

# Temp/cache directories to delete everywhere in the tree
TEMP_DIRS = {".ipynb_checkpoints", "__pycache__"}

# Root-level scratch notebook patterns to delete (fnmatch style)
ROOT_SCRATCH_PATTERNS = [
    "Untitled*.ipynb",  # Jupyter auto-named scratch notebooks
    "?.ipynb",          # single-char notebooks like x.ipynb
]

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def clean_lesson_name(folder_name: str) -> str:
    """dsc-correlation-covariance-lab-onl01-... -> correlation_covariance_lab"""
    name = folder_name
    name = re.sub(r"^dsc-", "", name)
    name = re.sub(r"-onl01-dtsc-[a-z]+-\d+$", "", name)
    name = re.sub(r"-v\d+(?:-\d+)*$", "", name)
    name = name.replace("-", "_")
    return name


def is_boilerplate(path: Path) -> bool:
    if path.name.lower() in BOILERPLATE:
        return True
    import fnmatch
    for pat in BOILERPLATE_PATTERNS:
        if fnmatch.fnmatch(path.name, pat):
            return True
    return False


def section_number(section_dir: Path) -> int:
    m = re.match(r"S(\d+)_", section_dir.name)
    return int(m.group(1)) if m else 99


def rewrite_notebook_paths(nb_path: Path, old_to_new: dict, dry_run: bool) -> None:
    """
    Rewrite asset/data paths inside a notebook in-place.
    old_to_new: {old_relative_path_str: new_relative_path_str}
    """
    if not nb_path.exists():
        return

    text = nb_path.read_text(encoding="utf-8")
    original = text

    for old, new in old_to_new.items():
        # Escape for use in regex (handle slashes, dots, etc.)
        old_esc = re.escape(old)
        # Replace in both JSON-string form (forward slashes already) and raw form
        text = re.sub(old_esc, new.replace("\\", "/"), text)

    if text != original:
        if not dry_run:
            nb_path.write_text(text, encoding="utf-8")
        print(f"    [notebook paths rewritten] {nb_path.name}")


def safe_move(src: Path, dst: Path, dry_run: bool) -> Path:
    """Move src to dst, auto-resolving name conflicts by appending _2, _3 …"""
    if dst.exists():
        stem, suffix = dst.stem, dst.suffix
        counter = 2
        while dst.exists():
            dst = dst.with_name(f"{stem}_{counter}{suffix}")
            counter += 1
    print(f"    MOVE  {src}  ->  {dst}")
    if not dry_run:
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(src), str(dst))
    return dst


def safe_copy(src: Path, dst: Path, dry_run: bool) -> Path:
    if dst.exists():
        stem, suffix = dst.stem, dst.suffix
        counter = 2
        while dst.exists():
            dst = dst.with_name(f"{stem}_{counter}{suffix}")
            counter += 1
    print(f"    COPY  {src}  ->  {dst}")
    if not dry_run:
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(str(src), str(dst))
    return dst


def remove_file(path: Path, dry_run: bool) -> None:
    print(f"    DEL   {path}")
    if not dry_run:
        path.unlink(missing_ok=True)


def remove_dir(path: Path, dry_run: bool) -> None:
    if not dry_run:
        # Only remove if empty (safety)
        try:
            remaining = list(path.rglob("*"))
            if remaining:
                print(f"    WARN  directory not empty, skipping delete: {path}")
                for r in remaining[:5]:
                    print(f"          still has: {r}")
                return
            path.rmdir()
        except Exception as e:
            print(f"    WARN  could not remove {path}: {e}")
    else:
        print(f"    RMDIR {path}")


# ---------------------------------------------------------------------------
# Core logic
# ---------------------------------------------------------------------------

def process_lesson(lesson_dir: Path, section_dir: Path, section_num: int,
                   seq: int, dry_run: bool) -> bool:
    """
    Process one lesson sub-folder. Returns True if a notebook was placed.
    """
    lesson_short = clean_lesson_name(lesson_dir.name)
    print(f"\n  [{seq:02d}] {lesson_dir.name}  ->  {lesson_short}")

    # --- Find main notebook ---
    nb_src = lesson_dir / "index.ipynb"
    if not nb_src.exists():
        nb_src = lesson_dir / "README.ipynb"
    if not nb_src.exists():
        # No notebook — just clean up boilerplate
        print(f"       (no notebook — cleaning up only)")
        _cleanup_lesson(lesson_dir, section_dir, lesson_short, section_num,
                        seq, None, None, dry_run)
        return False

    assets_dst_dir = section_dir / "assets" / lesson_short
    data_dst_dir   = section_dir / "data"   / lesson_short

    # Map of path rewrites to apply to the notebook text
    path_rewrites: dict[str, str] = {}

    # --- Move asset directories (images/, index_files/, etc.) ---
    for asset_subdir_name in ASSET_DIRS:
        asset_src = lesson_dir / asset_subdir_name
        if asset_src.is_dir():
            for f in sorted(asset_src.rglob("*")):
                if f.is_file():
                    rel = f.relative_to(asset_src)
                    dst = assets_dst_dir / rel
                    moved = safe_move(f, dst, dry_run)
                    # Record path rewrite: old -> new (relative to notebook)
                    old_rel = f"{asset_subdir_name}/{rel}".replace("\\", "/")
                    new_rel = f"assets/{lesson_short}/{rel}".replace("\\", "/")
                    path_rewrites[old_rel] = new_rel

    # --- Move loose data files at lesson root ---
    for f in sorted(lesson_dir.iterdir()):
        if not f.is_file():
            continue
        if f.name in {nb_src.name}:
            continue
        if is_boilerplate(f):
            continue
        if f.suffix.lower() in DATA_EXTS:
            dst = data_dst_dir / f.name
            moved = safe_move(f, dst, dry_run)
            path_rewrites[f.name] = f"data/{lesson_short}/{f.name}"
        elif f.suffix.lower() in ASSET_EXTS and f.name not in {"index.ipynb"}:
            dst = assets_dst_dir / f.name
            moved = safe_move(f, dst, dry_run)
            path_rewrites[f.name] = f"assets/{lesson_short}/{f.name}"

    # --- Move pytests/ directory (keep for reference in data) ---
    pytests_dir = lesson_dir / "pytests"
    if pytests_dir.is_dir():
        for f in sorted(pytests_dir.rglob("*")):
            if f.is_file():
                rel = f.relative_to(pytests_dir)
                dst = data_dst_dir / "pytests" / rel
                safe_move(f, dst, dry_run)

    # --- Copy notebook to section root with new name ---
    nb_dst_name = f"S{section_num}_{seq:02d}_{lesson_short}.ipynb"
    nb_dst = section_dir / nb_dst_name
    safe_copy(nb_src, nb_dst, dry_run)

    # --- Rewrite paths inside the copied notebook ---
    if path_rewrites:
        rewrite_notebook_paths(nb_dst, path_rewrites, dry_run)

    # --- Delete original lesson folder ---
    _cleanup_lesson(lesson_dir, section_dir, lesson_short, section_num,
                    seq, nb_src, nb_dst, dry_run)
    return True


def _force_rmtree(path: Path) -> None:
    """rmtree with read-only override for Windows."""
    def _on_error(func, p, exc):
        os.chmod(p, stat.S_IWRITE)
        func(p)
    shutil.rmtree(path, onexc=_on_error)


def _cleanup_lesson(lesson_dir: Path, section_dir: Path, lesson_short: str,
                    section_num: int, seq: int, nb_src, nb_dst, dry_run: bool):
    """Delete the entire lesson_dir (all valuable content already moved out)."""
    print(f"    RMDIR {lesson_dir}")
    if not dry_run:
        _force_rmtree(lesson_dir)


def process_section(section_dir: Path, dry_run: bool) -> None:
    snum = section_number(section_dir)
    print(f"\n{'='*60}")
    print(f"SECTION {snum}: {section_dir.name}")
    print(f"{'='*60}")

    # Collect lesson folders: dsc-* subdirs only
    lesson_dirs = sorted(
        d for d in section_dir.iterdir()
        if d.is_dir() and d.name.startswith("dsc-")
    )

    if not lesson_dirs:
        print("  (no lesson sub-folders found)")
        return

    seq = 1
    for lesson_dir in lesson_dirs:
        placed = process_lesson(lesson_dir, section_dir, snum, seq, dry_run)
        seq += 1

    # Delete TOC notebooks at the section root (redundant after reorganization)
    for toc_nb in section_dir.glob("*TOC*.ipynb"):
        remove_file(toc_nb, dry_run)

    # Clean up any now-empty asset/data subdirs created for zero files
    for parent in [section_dir / "assets", section_dir / "data"]:
        if parent.exists():
            for sub in list(parent.iterdir()):
                if sub.is_dir() and not any(sub.iterdir()):
                    print(f"  RMDIR (empty) {sub}")
                    if not dry_run:
                        sub.rmdir()
            if not any(parent.iterdir()):
                print(f"  RMDIR (empty) {parent}")
                if not dry_run:
                    parent.rmdir()


def cleanup_temp_dirs(root: Path, dry_run: bool) -> None:
    """Recursively remove .ipynb_checkpoints and __pycache__ everywhere."""
    print(f"\n{'='*60}")
    print("TEMP DIR CLEANUP")
    print(f"{'='*60}")
    found = False
    for temp_name in TEMP_DIRS:
        for p in sorted(root.rglob(temp_name)):
            if p.is_dir():
                found = True
                print(f"  RMDIR {p}")
                if not dry_run:
                    _force_rmtree(p)
    if not found:
        print("  (none found)")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true",
                        help="Print what would happen without making changes")
    parser.add_argument("--root", default=None,
                        help="Path to MOD_1 directory (default: script's directory)")
    parser.add_argument("--section", default=None,
                        help="Process only this section, e.g. S4_pandas_visualization")
    args = parser.parse_args()

    root = Path(args.root) if args.root else Path(__file__).parent
    if not root.exists():
        print(f"ERROR: root directory not found: {root}")
        sys.exit(1)

    print(f"Root: {root}")
    if args.dry_run:
        print("*** DRY RUN — no files will be changed ***\n")

    section_dirs = sorted(
        d for d in root.iterdir()
        if d.is_dir() and re.match(r"S\d+_", d.name)
    )

    if args.section:
        section_dirs = [d for d in section_dirs if d.name == args.section]
        if not section_dirs:
            print(f"ERROR: section '{args.section}' not found")
            sys.exit(1)

    for section_dir in section_dirs:
        process_section(section_dir, dry_run=args.dry_run)

    # Clean up root-level TOC notebooks, scratch notebooks, and tocs/ folder
    print(f"\n{'='*60}")
    print("ROOT CLEANUP")
    print(f"{'='*60}")
    import fnmatch
    toc_patterns = ["*TOC*.ipynb", "*toc*.ipynb"]
    all_patterns = toc_patterns + ROOT_SCRATCH_PATTERNS
    for f in sorted(root.iterdir()):
        if f.is_file() and any(fnmatch.fnmatch(f.name, pat) for pat in all_patterns):
            remove_file(f, dry_run=args.dry_run)

    tocs_dir = root / "tocs"
    if tocs_dir.exists():
        print(f"  RMDIR {tocs_dir}")
        if not args.dry_run:
            _force_rmtree(tocs_dir)
    else:
        print("  (not found, skipping) tocs/")

    cleanup_temp_dirs(root, dry_run=args.dry_run)

    print("\n\nDone.")


if __name__ == "__main__":
    main()
