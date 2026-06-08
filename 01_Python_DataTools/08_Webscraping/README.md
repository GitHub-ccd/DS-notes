# Section 08 — Web Scraping

HTML/CSS foundations and Beautiful Soup — extracting structured data from web pages.

## Notebooks

| # | Notebook | Topic |
|---|----------|-------|
| 01 | `01_html_and_css.ipynb` | HTML tags, document structure, CSS selectors and declaration blocks |
| 02 | `02_beautifulsoup_basics.ipynb` | DOM, `find`/`find_all`, `.attrs`, tree navigation, ethics and limits |
| 03 | `03_scraping_in_practice.ipynb` | Inspect element workflow, books.toscrape full pipeline, regex class matching, pagination, image downloading |

## 2026 Notes

Beautiful Soup handles static HTML. For JavaScript-rendered pages (increasingly common), use **Playwright** (modern, async-native) or **Selenium** (older, widely documented). Many large-scale scraping targets now use Cloudflare or similar bot-detection — always check `robots.txt` and terms of service before scraping. For large-scale crawling, `Scrapy` remains the standard framework.