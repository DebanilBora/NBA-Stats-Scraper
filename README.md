🏀 NBA Stats Scraper (2020–2024)

A Python script that scrapes NBA player statistics (per game, totals, advanced) from Basketball Reference
 using Playwright + BeautifulSoup + Pandas and saves them into a single CSV file.

🚀 Features

📊 Scrapes per game, totals, and advanced stats

📅 Covers multiple seasons (2020–2024)

🔄 Retry mechanism with delays to handle failed requests

⏳ Progress bar with tqdm for tracking scraping progress

🖥 Headless Chromium browser automation with Playwright

💾 Saves results to nba_stats.csv

🛠 Tech Stack

Python 3

Libraries:

playwright – headless browser automation

beautifulsoup4 – parse HTML & comments (hidden tables)

pandas – tabular data processing & CSV export

tqdm – progress bar

io.StringIO, time.sleep – retries & parsing support

⚙️ Setup & Installation
1️⃣ Clone the repository
git clone https://github.com/DebanilBora/NBA-Stats-Scraper.git
cd nba-stats-scraper

2️⃣ Create & activate a virtual environment
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Install Playwright browsers
playwright install

▶️ Usage

Run the script:

python app.py


✅ Opens Chromium in headless mode

✅ Scrapes NBA player stats for 2020–2024 seasons

✅ Extracts per game, totals, advanced stats

✅ Saves final dataset into nba_stats.csv

📂 Example Output (CSV)
Player	Team	G	PTS	TRB	AST	Season	StatType
LeBron James	LAL	67	25.3	7.8	10.2	2020	per_game
Giannis Ant.	MIL	63	28.1	11.0	5.9	2020	advanced
🏷 Tags

#Python #WebScraping #NBA #Basketball #DataScience #Playwright #BeautifulSoup #Pandas
