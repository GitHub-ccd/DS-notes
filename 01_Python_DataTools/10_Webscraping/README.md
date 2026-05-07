# Section 10 — Web Scraping

HTML and CSS fundamentals, BeautifulSoup for static pages, and modern browser automation for dynamic content.

## Notebooks

| Notebook | Topic |
|----------|-------|
| `01_css_code_along.ipynb` | CSS code-along |
| `02_html_css_scraping_intro.ipynb` | HTML and CSS scraping introduction |
| `03_html_css_scraping_recap.ipynb` | Section recap |
| `05_html_introduction.ipynb` | HTML structure — tags, attributes, DOM |
| `06_intro_to_css.ipynb` | CSS selectors and styling |
| `08_researching_html_elements.ipynb` | Using browser dev tools to inspect pages |
| `09_scraping_concerts_lab.ipynb` | Scraping concerts data lab |
| `10_scraping_images.ipynb` | Scraping and downloading images |
| `11_separating_content_and_presentation.ipynb` | Content vs presentation in HTML/CSS |
| `12_web_scraping_in_practice.ipynb` | Scraping in practice — real-world patterns |
| `13_web_scraping_lab.ipynb` | Web scraping lab |
| `14_web_scraping_with_beautiful_soup.ipynb` | BeautifulSoup — parsing and extracting data |

## 2026 Context

**Static pages:** `requests` + `BeautifulSoup` — unchanged, still the right tool.

**Dynamic/JavaScript-rendered pages:** **Playwright** has replaced Selenium as the modern standard for browser automation. It is async-native, has a cleaner API, and is actively maintained. `pip install playwright && playwright install`. For large-scale crawling, `Scrapy` remains the standard framework.

Always respect `robots.txt`, add delays between requests, and prefer an official API when one is available.