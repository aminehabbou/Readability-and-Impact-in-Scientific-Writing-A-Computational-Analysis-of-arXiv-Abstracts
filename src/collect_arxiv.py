import arxiv
import pandas as pd
from tqdm import tqdm

FIELDS = {
    "computer_science": "cat:cs.*",
    "physics": "cat:physics.*",
    "mathematics": "cat:math.*",
}

PAPERS_PER_FIELD = 500

records = []

for field_name, query in FIELDS.items():
    print(f"Collecting {field_name} papers...")

    search = arxiv.Search(
        query=query,
        max_results=PAPERS_PER_FIELD,
        sort_by=arxiv.SortCriterion.SubmittedDate,
    )

    for result in tqdm(search.results()):
        records.append(
            {
                "paper_id": result.entry_id,
                "title": result.title,
                "field": field_name,
                "abstract": result.summary,
                "published": result.published,
            }
        )

df = pd.DataFrame(records)

output_path = "data/raw/arxiv_abstracts.csv"

df.to_csv(output_path, index=False)

print(f"\nSaved {len(df)} abstracts to {output_path}")
