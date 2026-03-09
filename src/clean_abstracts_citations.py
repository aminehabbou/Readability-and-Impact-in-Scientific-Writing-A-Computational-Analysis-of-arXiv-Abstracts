import pandas as pd

df = pd.read_csv("data/processed/arxiv_2010_2018_with_citations.csv")

df_clean = df.dropna(subset=["citation_count"])
df_clean["citation_count"] = df_clean["citation_count"].astype(int)

df_clean.to_csv("data/processed/arxiv_2010_2018_clean_citations.csv", index=False)
