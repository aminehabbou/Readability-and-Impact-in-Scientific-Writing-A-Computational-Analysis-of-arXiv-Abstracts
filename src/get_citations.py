import pandas as pd
import requests
from tqdm import tqdm
import time

# Path to your CSV
INPUT_PATH = "data/raw/arxiv_2010_2018.csv"
OUTPUT_PATH = "data/processed/arxiv_2010_2018_with_citations.csv"

df = pd.read_csv(INPUT_PATH)
DEFAULT_CATEGORY = "cs"


def extract_arxiv_id_from_url(url, category=DEFAULT_CATEGORY):
    url = str(url).strip()
    if url.startswith("http"):
        url = url.split("/")[-1]
    if "/" in url:
        cat, paper_id = url.split("/")
    else:
        cat = category
        paper_id = url
    paper_id = paper_id.split("v")[0]  # remove version suffix
    if len(paper_id) <= 7:
        return f"{cat.upper()}:{paper_id}"
    else:
        return paper_id


# Clean arXiv IDs
df["arxiv_id_full"] = df["paper_id"].apply(
    lambda x: extract_arxiv_id_from_url(x, DEFAULT_CATEGORY)
)

citations = []

for idx, arxiv_id in enumerate(tqdm(df["arxiv_id_full"], desc="Fetching citations")):
    citation_count = None
    retries = 3
    wait_time = 2
    for attempt in range(retries):
        try:
            url = f"https://api.semanticscholar.org/graph/v1/paper/ARXIV:{arxiv_id}?fields=citationCount"
            r = requests.get(url)
            if r.status_code == 200:
                data = r.json()
                citation_count = data.get("citationCount", 0)
                break
            elif r.status_code == 404:
                citation_count = None
                break
            elif r.status_code == 429:
                print(f"Rate limit hit for {arxiv_id}, waiting {wait_time}s...")
                time.sleep(wait_time)
                wait_time *= 2  # exponential backoff
            else:
                print(f"API error {r.status_code} for {arxiv_id}")
                break
        except Exception as e:
            print(f"Request failed for {arxiv_id}: {e}")
            break

    citations.append(citation_count)
    print(f"{idx+1}/{len(df)}: {arxiv_id} -> {citation_count}")
    time.sleep(1)  # small delay to avoid hitting API limits

# Save updated CSV
df["citation_count"] = citations
df.to_csv(OUTPUT_PATH, index=False)
print(f"Saved dataset with citation counts to {OUTPUT_PATH}")
