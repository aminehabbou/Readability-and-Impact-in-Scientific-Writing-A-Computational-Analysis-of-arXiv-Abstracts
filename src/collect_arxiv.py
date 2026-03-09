import arxiv
import pandas as pd
from tqdm import tqdm
import time

FIELDS = {
    "computer_science": "cat:cs.*",
    "physics": "cat:physics.*",
    "mathematics": "cat:math.*",
}

TARGET_START = 2010
TARGET_END = 2018

records = []

# Construct date strings for arXiv query
# arXiv uses YYYYMMDD format
start_date_str = f"{TARGET_START}0101"
end_date_str = f"{TARGET_END}1231"

for field_name, field_query in FIELDS.items():
    print(f"\nCollecting {field_name} papers...")

    # Include date range in query using submittedDate
    query = f"{field_query} AND submittedDate:[{start_date_str} TO {end_date_str}]"

    search = arxiv.Search(
        query=query,
        max_results=1000,  # large pool
        sort_by=arxiv.SortCriterion.SubmittedDate,
        sort_order=arxiv.SortOrder.Descending,  # newest first (2018 -> 2015)
    )

    count_field = 0
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
            count_field += 1

        if count_field >= 1000:  # stop when enough papers collected per field
            break

        time.sleep(0.4)  # avoid arXiv rate limits

df = pd.DataFrame(records)
print(df.head())

OUTPUT_PATH = "data/raw/arxiv_1990_2014.csv"

df.to_csv(OUTPUT_PATH, index=False)

print(f"\nSaved {len(df)} papers to {OUTPUT_PATH}")
