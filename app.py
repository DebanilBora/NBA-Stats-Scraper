from playwright.sync_api import sync_playwright
import pandas as pd
from bs4 import BeautifulSoup, Comment
from io import StringIO
from time import sleep
from tqdm import tqdm

BASE_URL = "https://www.basketball-reference.com/leagues/NBA_{year}_{stat}.html"
YEARS = [2020, 2021, 2022, 2023, 2024]
STAT_TYPES = ["per_game", "totals", "advanced"]
MAX_RETRIES = 3
SLEEP_BETWEEN_RETRIES = 2  # seconds

def scrape(year, stat_type, page):
    url = BASE_URL.format(year=year, stat=stat_type)

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            page.goto(url, wait_until="domcontentloaded", timeout=60000)
            sleep(2)
            html = page.content()
            soup = BeautifulSoup(html, "html.parser")

            table = None

            # 1️⃣ Wrapper + comment
            wrapper = soup.find("div", {"id": f"all_{stat_type}_stats"})
            if wrapper:
                comment = wrapper.find(string=lambda text: isinstance(text, Comment))
                if comment:
                    comment_soup = BeautifulSoup(comment, "html.parser")
                    table = comment_soup.find("table")
                else:
                    table = wrapper.find("table")

            # 2️⃣ Direct table by standard ID
            if not table:
                table = soup.find("table", {"id": f"{stat_type}_stats"})

            # 3️⃣ Specific fallback for advanced stats
            if not table and stat_type == "advanced":
                for adv_id in ["advanced_stats", "advanced"]:
                    table = soup.find("table", {"id": adv_id})
                    if table:
                        break

            # 4️⃣ Fallback any table ending with "_stats"
            if not table:
                for t in soup.find_all("table"):
                    if t.get("id") and t.get("id").endswith("_stats"):
                        table = t
                        break

            if not table:
                raise ValueError(f"No table found for {year} {stat_type}")

            df = pd.read_html(StringIO(str(table)))[0]
            df["Season"] = year
            df["StatType"] = stat_type
            return df

        except Exception as e:
            print(f"⚠️ Attempt {attempt} failed for {year} {stat_type}: {e}")
            if attempt < MAX_RETRIES:
                sleep(SLEEP_BETWEEN_RETRIES)
            else:
                print(f"❌ Failed to scrape {year} {stat_type} after {MAX_RETRIES} attempts.")
                return None

def main():
    all_data = []
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
            locale="en-US"
        )
        page = context.new_page()

        # Progress bar for total scraping
        total_tasks = len(YEARS) * len(STAT_TYPES)
        with tqdm(total=total_tasks, desc="Scraping NBA Stats") as pbar:
            for year in YEARS:
                for stat_type in STAT_TYPES:
                    df = scrape(year, stat_type, page)
                    if df is not None:
                        all_data.append(df)
                    pbar.update(1)

        browser.close()

    if all_data:
        final_df = pd.concat(all_data, ignore_index=True)
        final_df.to_csv("nba_stats.csv", index=False)
        print("💾 Data saved to nba_stats.csv")
    else:
        print("⚠️ No data collected.")

if __name__ == "__main__":
    main()
