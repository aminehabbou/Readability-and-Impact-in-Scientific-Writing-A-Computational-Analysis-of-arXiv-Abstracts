import arxiv
import pandas as pd
from tqdm import tqdm
import time

FIELDS = {
    "computer_science": "cat:cs.*",
    "physics": "cat:physics.*",
    "mathematics": "cat:math.*",
}

TARGET_START = 1990
TARGET_END = 2014

records = []

for field_name, query in FIELDS.items():
    print(f"\nCollecting {field_name} papers...")

    search = arxiv.Search(
        query=query,
        max_results=2000,  # large pool
        sort_by=arxiv.SortCriterion.SubmittedDate,
        sort_order=arxiv.SortOrder.Ascending,
    )

    for result in tqdm(search.results()):
        year = result.published.year

        if TARGET_START <= year <= TARGET_END:
            records.append(
                {
                    "paper_id": result.entry_id,
                    "title": result.title,
                    "field": field_name,
                    "abstract": result.summary,
                    "published": result.published,
                    "year": year,
                }
            )

        # stop when enough papers collected
        if len([r for r in records if r["field"] == field_name]) >= 1000:
            break

        time.sleep(0.4)  # avoid arXiv rate limits


df = pd.DataFrame(records)

OUTPUT_PATH = "data/raw/arxiv_1990_2014.csv"

df.to_csv(OUTPUT_PATH, index=False)

print(f"\nSaved {len(df)} papers to {OUTPUT_PATH}")
