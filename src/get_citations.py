import pandas as pd
import requests
from tqdm import tqdm
import time

INPUT_PATH = "data/raw/arxiv_abstracts.csv"
OUTPUT_PATH = "data/processed/arxiv_with_citations.csv"

df = pd.read_csv(INPUT_PATH)


def extract_arxiv_id(url):
    return url.split("/")[-1].split("v")[0]


df["arxiv_id"] = df["paper_id"].apply(extract_arxiv_id)

citations = []

for arxiv_id in tqdm(df["arxiv_id"]):
    url = f"https://api.semanticscholar.org/graph/v1/paper/ARXIV:{arxiv_id}?fields=citationCount"

    try:
        r = requests.get(url)
        data = r.json()

        citation_count = data.get("citationCount", 0)

    except:
        citation_count = 0

    citations.append(citation_count)

    time.sleep(0.2)  # avoid rate limits

df["citation_count"] = citations

df.to_csv(OUTPUT_PATH, index=False)

print("Saved dataset with citations to:", OUTPUT_PATH)
