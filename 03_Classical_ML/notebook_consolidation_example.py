"""
notebook_consolidation_example.py
==================================
Reference script showing how every section of DS-notes was consolidated.
Each paired lesson + lab notebook was merged into a single integrated notebook,
reducing the file count by roughly 3:1.

The script is based on the 06_PCA section (13 source files -> 5 output files)
because it demonstrates every pattern that came up across the project.

HOW TO ADAPT FOR A NEW SECTION
  1. Change BASE to the target directory.
  2. Load all source notebooks with load().
  3. For each output notebook:
       a. Start with a new title cell: mk_md("# Title")
       b. Pull content in from source notebooks using the three helpers:
            add_lesson_cells   -- for standard lesson notebooks
            add_lab_cells      -- for lab notebooks (handles header stripping)
            extract_thin_intro -- for 1-cell "overview" notebooks
       c. Separate sections with a horizontal rule: mk_md("---")
       d. Write out with write_nb().
  4. Run git rm on the old files, git add on the new ones, then commit.
"""

import json   # Jupyter notebooks are JSON files on disk
import re     # Used for pattern-matching inside cell text
import os     # Used to build file paths

# ── Configuration ────────────────────────────────────────────────────────────
# Raw string (r"...") avoids having to double every backslash on Windows.
# Change this path when adapting the script for a different section.
BASE = r"e:\My_GitHub__projects\DS-notes\03_Classical_ML\06_PCA"


# ── I/O helpers ──────────────────────────────────────────────────────────────

def load(name):
    """
    Load a .ipynb file and return its parsed JSON as a dict.

    Jupyter notebooks are plain JSON, so json.load() is all that's needed.
    The only complication is encoding: most files are UTF-8, but a few were
    saved by older tools with a UTF-8 BOM (Byte Order Mark) header, which
    makes Python's 'utf-8' codec raise a JSONDecodeError. Trying 'utf-8-sig'
    as a fallback strips the BOM automatically.
    """
    path = os.path.join(BASE, name)
    for enc in ('utf-8', 'utf-8-sig'):
        try:
            with open(path, encoding=enc) as f:
                return json.load(f)
        except (UnicodeDecodeError, json.JSONDecodeError):
            continue   # try the next encoding
    raise ValueError(f"Cannot load {name}")


def src(cell):
    """
    Return the full text of a notebook cell as a single string.

    Inside a .ipynb file, cell["source"] is a *list* of strings — one entry
    per line, each ending with '\\n' except the last.  Joining them gives
    back the plain text you'd see in the notebook editor.
    """
    return ''.join(cell.get('source', []))


def is_empty(cell):
    """Return True if a cell has no visible content (blank or only whitespace)."""
    return not src(cell).strip()


def mk_md(text):
    """
    Build a new markdown cell dict from a plain string.

    The nbformat spec stores source as a list of lines, each ending with '\\n'
    except the very last line.  This function converts a normal multi-line
    string into that format.

    Returns None when text is empty so callers can safely append the result
    to a list and filter out None values at write time.
    """
    text = (text or '').strip()
    if not text:
        return None
    lines = text.split('\n')
    # All lines except the last get a trailing newline; the last line does not.
    source = [l + '\n' for l in lines[:-1]] + [lines[-1]]
    return {"cell_type": "markdown", "metadata": {}, "source": source}


def clone_code(cell):
    """
    Copy a code cell, keeping its source and any saved outputs.

    execution_count is reset to None because the cell hasn't been re-run
    in the new notebook yet.  Keeping the old outputs means images and
    printed results are still visible without needing to re-execute.
    """
    return {
        "cell_type": "code",
        "metadata": {},
        "source": cell.get('source', []),
        "outputs": cell.get('outputs', []),
        "execution_count": None,
    }


def clone(cell):
    """
    Dispatch to the right clone helper based on cell type.

    Returns None for raw/unknown cell types so they can be filtered out.
    """
    t = cell.get('cell_type', '')
    if t == 'markdown':
        return mk_md(src(cell))   # re-build so whitespace is normalised
    if t == 'code':
        return clone_code(cell)
    return None


def write_nb(cells, name):
    """
    Write a list of cell dicts to disk as a valid .ipynb file.

    None values are filtered out first — this lets callers append the return
    value of mk_md() / extract_thin_intro() directly without checking for None.

    The nbformat metadata block is the minimum required for Jupyter to open
    the file.  indent=1 keeps the JSON readable; ensure_ascii=False preserves
    any non-ASCII characters (maths symbols, accented letters, etc.).
    """
    cells = [c for c in cells if c is not None]
    nb = {
        "nbformat": 4,
        "nbformat_minor": 2,
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3",
            },
            "language_info": {
                "name": "python",
                "version": "3.8.0",
            },
        },
        "cells": cells,
    }
    with open(os.path.join(BASE, name), 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=1, ensure_ascii=False)
    print(f"  {name}: {len(cells)} cells")


# ── Content-extraction helpers ────────────────────────────────────────────────

def add_lesson_cells(dest, nb, start_from=1):
    """
    Append all meaningful lesson cells from a source notebook into dest.

    WHAT IT SKIPS
      - cell[0] is always the title cell (# Heading + optional intro text),
        which is replaced by a fresh title in the integrated notebook.
        start_from=1 skips it.
      - Empty cells are skipped entirely.
      - The ## Summary and ## Additional Resources sections are stripped:
        they were useful in standalone files but become redundant noise when
        lessons are embedded inside a larger notebook.

    EDGE CASE — content before Summary
      If a Summary heading appears mid-cell (after real content), the text
      before it is kept and the rest is discarded.

    TYPICAL CALL
      add_lesson_cells(cells, nb_lesson, start_from=1)

    SPLIT PATTERN
      Some notebooks separate the title from the intro text across two cells:
        cell[0] = "# Title"  (title only)
        cell[1] = "## Introduction"  (intro text)
        cell[2] = "## Objectives"
        cell[3] = objectives list
        cell[4] = first real content cell
      In that case pass start_from=1 to include the intro, or start_from=3/4
      to skip it.  Check the inspect script output to decide.
    """
    for cell in nb['cells'][start_from:]:
        if is_empty(cell):
            continue
        text = src(cell).strip()
        if cell.get('cell_type') == 'markdown':
            # Stop at Summary or Additional Resources headings
            m = re.search(r'^## *(Summary|Additional Resources)\b', text, re.MULTILINE)
            if m:
                # Preserve any content that appeared before the heading
                before = text[:m.start()].strip()
                if before:
                    dest.append(mk_md(before))
                break   # discard the summary section and everything after it
            dest.append(mk_md(text))
        else:
            dest.append(clone(cell))


def add_lab_cells(dest, nb, start_from=0, cell0_extract='AUTO'):
    """
    Append lab cells into dest, with smart stripping of the lab header cell.

    Lab notebooks always open with a header cell that looks like:
        ## Lab Title
        ## Introduction
        In the previous lesson you saw...
        ## Objectives
        You will be able to...

    That boilerplate is useful in a standalone file but redundant inside an
    integrated notebook that already has the lesson above it.  This function
    strips it automatically via the cell0_extract logic.

    PARAMETERS
      dest          : list to append cells into
      nb            : source notebook dict
      start_from    : index of the first cell to consider (default 0)
      cell0_extract : controls how the first cell (at index start_from) is handled

    CELL0_EXTRACT VALUES
      'AUTO' (default)
          Searches the first cell for the pattern  \\n## <heading>  where the
          heading is NOT Introduction, Objectives, or Summary.  If found,
          everything from that heading onwards is kept and the title/intro
          prefix is discarded.

          If no such heading exists (the cell is just a title + intro
          paragraph with no content sub-sections), the entire cell is
          skipped.  This is the right behaviour for most labs whose intro
          text duplicates what the lesson just explained.

      '## Some Heading'  (explicit string)
          Finds that exact string inside the first cell and extracts from
          that point.  Use when AUTO picks the wrong heading or you want to
          start from a specific known section.

      None
          The first cell is cloned as-is, with no extraction.  Rarely needed;
          use it when the first cell genuinely starts with real content.

    STOPPING
      Like add_lesson_cells, this function stops when it encounters a
      ## Summary or ## Additional Resources heading.

    TYPICAL CALLS
      add_lab_cells(cells, nb_lab)                         # AUTO header strip
      add_lab_cells(cells, nb_lab, start_from=4)           # SPLIT pattern lab
      add_lab_cells(cells, nb_lab, cell0_extract=None)     # keep first cell
    """
    for i, cell in enumerate(nb['cells']):
        if i < start_from:
            continue
        if is_empty(cell):
            continue
        text = src(cell).strip()

        # Stop at Summary / Additional Resources
        if re.search(r'^## *(Summary|Additional Resources)\b', text, re.MULTILINE):
            break

        if i == start_from and cell0_extract is not None:
            # ── Special handling for the first cell ──────────────────────
            raw = src(cell)
            if cell0_extract == 'AUTO':
                # Find the first ## heading that is NOT a boilerplate section.
                # The negative lookahead (?!Introduction|Objectives|Summary)
                # rejects those three heading names.
                # The \\n before ## is intentional: it ensures we only match
                # headings that start on their own line (not ## at position 0).
                m_real = re.search(r'\n## +(?!Introduction|Objectives|Summary)', raw)
                if m_real:
                    # Keep from that heading onwards; discard the title prefix
                    dest.append(mk_md(raw[m_real.start() + 1:].strip()))
                # If no non-boilerplate heading found, the whole cell is skipped
            else:
                # Explicit extract: find the given string and keep from there
                idx = raw.find(cell0_extract)
                if idx >= 0:
                    dest.append(mk_md(raw[idx:].strip()))
        else:
            # All cells after the first are cloned without modification
            dest.append(clone(cell))


def extract_thin_intro(nb):
    """
    Extract the body text from a single-cell 'overview' notebook.

    Some notebooks exist purely to introduce a section with a few sentences.
    Their entire content is one markdown cell structured like this:

        # Section Title

        ## Introduction

        In this section you will learn about X, Y, and Z...

        ## Summary          <-- sometimes present, sometimes not
        Key takeaways...

    We want only the body paragraph(s) — not the title, not the ## Introduction
    header, and not the ## Summary.  This function strips all three.

    FALLBACK
      If no ## Introduction heading is found, the function skips just the
      title line (line[0]) and returns the rest.  This handles notebooks that
      omit the ## Introduction subheading.

    Returns None if nothing meaningful remains after stripping.
    """
    raw = src(nb['cells'][0])

    # Locate the ## Introduction heading to find where the body starts
    m = re.search(r'\n## Introduction\n', raw)
    if m:
        body = raw[m.end():].strip()
    else:
        # No ## Introduction found — skip only the title line
        body = '\n'.join(raw.split('\n')[1:]).strip()

    # Remove trailing ## Summary or ## Additional Resources sections
    for pat in (r'\n## *Summary\b', r'\n## *Additional Resources\b'):
        m2 = re.search(pat, body)
        if m2:
            body = body[:m2.start()].strip()

    return mk_md(body) if body else None


# ═══════════════════════════════════════════════════════════════════════════════
# MAIN — Build the five integrated notebooks for 06_PCA
# ═══════════════════════════════════════════════════════════════════════════════
#
# Source layout (13 files):
#   01  curse_of_dimensionality_lab          16 cells  lab
#   02  curse_of_dimensionality               2 cells  lesson (thin)
#   03  pca_and_digital_image_processing_lab 28 cells  lab
#   04  pca_and_digital_image_processing     36 cells  lesson
#   05  pca_and_pipelines                    52 cells  lab  ← SPLIT pattern, in-place overwrite
#   06  pca_covariance_matrix_eigendecomp    15 cells  lesson (empty code cell at [1])
#   07  pca_in_scikitlearn_lab               29 cells  lab
#   08  pca_in_scikitlearn                   31 cells  lesson (starts with code at [1])
#   09  pca_introduction                      1 cell   thin overview  → extract_thin_intro
#   10  pca_numpy_lab                        14 cells  lab
#   11  pca_summary                           1 cell   recap  → DROPPED
#   12  performing_principal_component_analysis 18 cells  lesson
#   13  unsupervised_learning                 2 cells  thin overview  → extract_thin_intro

# Load all source notebooks before writing anything.
# This matters for nb05: we load the old version first, then overwrite the file
# with the consolidated version — if we wrote first and loaded second we'd read
# our own output.
nb13    = load("13_unsupervised_learning.ipynb")
nb09    = load("09_pca_introduction.ipynb")
nb02    = load("02_curse_of_dimensionality.ipynb")
nb01    = load("01_curse_of_dimensionality_lab.ipynb")
nb12    = load("12_performing_principal_component_analysis.ipynb")
nb06    = load("06_pca_covariance_matrix_eigendecomp.ipynb")
nb10    = load("10_pca_numpy_lab.ipynb")
nb08    = load("08_pca_in_scikitlearn.ipynb")
nb07    = load("07_pca_in_scikitlearn_lab.ipynb")
nb04    = load("04_pca_and_digital_image_processing.ipynb")
nb03    = load("03_pca_and_digital_image_processing_lab.ipynb")
nb05_src = load("05_pca_and_pipelines.ipynb")   # loaded before the file is overwritten below


# ── Output notebook 1: 01_curse_of_dimensionality.ipynb ──────────────────────
#
# Sources used: nb13 (thin), nb09 (thin), nb02 (thin lesson), nb01 (lab)
#
# Both nb13 and nb09 are single-cell overview notebooks, so we use
# extract_thin_intro instead of add_lesson_cells.
# nb02 has only 2 cells (title + one content cell), so start_from=1 picks up
# that single content cell.

cells1 = [mk_md("# The Curse of Dimensionality")]  # fresh title for the merged file

cells1.append(extract_thin_intro(nb13))  # "In this section you'll learn about unsupervised learning..."
cells1.append(mk_md("---"))              # horizontal rule to visually separate sections

cells1.append(extract_thin_intro(nb09))  # "In this section you'll learn about PCA..."
cells1.append(mk_md("---"))

# nb02 lesson — start_from=1 skips the title cell [0]
add_lesson_cells(cells1, nb02, start_from=1)
cells1.append(mk_md("---"))

# nb01 lab — AUTO strips the "## The Curse of Dimensionality - Lab / ## Introduction" header cell
add_lab_cells(cells1, nb01, start_from=0, cell0_extract='AUTO')

write_nb(cells1, "01_curse_of_dimensionality.ipynb")


# ── Output notebook 2: 02_performing_pca.ipynb ───────────────────────────────
#
# Sources: nb12 (lesson), nb06 (lesson: covariance + eigendecomp), nb10 (lab)
#
# nb06 has an empty code cell at index 1; is_empty() inside add_lesson_cells
# skips it automatically, so start_from=1 still works correctly.

cells2 = [mk_md("# Performing Principal Component Analysis")]

add_lesson_cells(cells2, nb12, start_from=1)  # step-by-step PCA lesson
cells2.append(mk_md("---"))

add_lesson_cells(cells2, nb06, start_from=1)  # covariance matrix + eigendecomposition
cells2.append(mk_md("---"))

# nb10 lab — AUTO skips "# Performing PCA - Lab / ## Introduction" header
add_lab_cells(cells2, nb10, start_from=0, cell0_extract='AUTO')

write_nb(cells2, "02_performing_pca.ipynb")


# ── Output notebook 3: 03_pca_in_scikitlearn.ipynb ───────────────────────────
#
# Sources: nb08 (lesson), nb07 (lab)
#
# nb08 lesson starts with a code cell at [1] (no Objectives section),
# so start_from=1 picks up the code directly after the title.

cells3 = [mk_md("# PCA in Scikit-Learn")]

add_lesson_cells(cells3, nb08, start_from=1)
cells3.append(mk_md("---"))

add_lab_cells(cells3, nb07, start_from=0, cell0_extract='AUTO')

write_nb(cells3, "03_pca_in_scikitlearn.ipynb")


# ── Output notebook 4: 04_pca_image_recognition.ipynb ────────────────────────
#
# Sources: nb04 (lesson: Olivetti faces dataset), nb03 (lab: MNIST digits)

cells4 = [mk_md("# PCA for Image Recognition")]

add_lesson_cells(cells4, nb04, start_from=1)
cells4.append(mk_md("---"))

add_lab_cells(cells4, nb03, start_from=0, cell0_extract='AUTO')

write_nb(cells4, "04_pca_image_recognition.ipynb")


# ── Output notebook 5: 05_pca_and_pipelines.ipynb (in-place overwrite) ───────
#
# Source: nb05_src (lab only — no paired lesson exists)
#
# This is the one case where the output filename is the SAME as the source.
# That is why nb05_src was loaded at the top before any writes happened.
#
# nb05 uses the SPLIT pattern — the intro is spread across four cells:
#   cell[0] = "# Integrating PCA in Pipelines - Lab"   (title only)
#   cell[1] = "## Introduction"                         (header only)
#   cell[2] = intro paragraph text
#   cell[3] = "## Objectives\nIn this lab you will:..."
#   cell[4] = first real content cell  ← start_from=4
#
# Passing start_from=4 to add_lab_cells skips all four boilerplate cells.
# cell0_extract is irrelevant here because start_from=4 means there is no
# "special first cell" to strip — every cell from index 4 onward is cloned
# normally.

cells5 = [mk_md("# Integrating PCA in Pipelines")]

add_lab_cells(cells5, nb05_src, start_from=4)  # SPLIT: skip title + intro + objectives

write_nb(cells5, "05_pca_and_pipelines.ipynb")  # overwrites the original source file


print("Done.")
