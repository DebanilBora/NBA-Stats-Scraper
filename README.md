# NBA Stats Scraper 🏀

A **Python-based web scraper** that collects NBA player statistics from [Basketball-Reference](https://www.basketball-reference.com/) for multiple seasons and stat types.  
This project demonstrates **web scraping with Playwright**, **data extraction with BeautifulSoup**, and **data handling with pandas**.

---

## Features

- Scrapes **per game, totals, and advanced stats** for multiple NBA seasons.  
- Handles **different table structures** (commented tables, direct tables, and new advanced stats table IDs).  
- **Retries failed requests** up to 3 times for robust scraping.  
- **Progress bar** with `tqdm` to track scraping progress.  
- Saves all data to a **CSV file (`nba_stats.csv`)** for further analysis.  
- Future-proof `pandas.read_html` implementation to avoid warnings.

---

## Technologies Used

- Python 3.13+  
- [Playwright](https://playwright.dev/python/) for headless browser automation  
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) for HTML parsing  
- [pandas](https://pandas.pydata.org/) for data handling  
- [tqdm](https://github.com/tqdm/tqdm) for progress visualization  

---


