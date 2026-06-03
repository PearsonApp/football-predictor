from dotenv import load_dotenv
import os
import requests
from pathlib import Path
import pandas as pd


BASE_DIR = Path(__file__).parent
ROOT_DIR = BASE_DIR.parent
load_dotenv(dotenv_path=ROOT_DIR / ".env")
api_key = os.environ.get("API_KEY")
response = requests.get("https://v3.football.api-sports.io/fixtures?league=39&season=2024", headers={"x-apisports-key": api_key})
data = response.json()
df = pd.json_normalize(data["response"])
print(df.head())
print(df.columns)
print(df.shape)

df.to_csv(ROOT_DIR / "data" / "raw_matches.csv", index=False)

