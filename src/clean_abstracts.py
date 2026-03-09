import pandas as pd
import re

INPUT_PATH = "data/raw/arxiv_2010_2018.csv"
OUTPUT_PATH = "data/processed/arxiv_abstracts_clean.csv"

df = pd.read_csv(INPUT_PATH)


def clean_text(text):
    if pd.isna(text):
        return ""

    # remove line breaks
    text = text.replace("\n", " ")

    # remove latex math expressions ($...$)
    text = re.sub(r"\$.*?\$", "", text)

    # remove latex commands (\alpha, \beta, etc.)
    text = re.sub(r"\\[a-zA-Z]+", "", text)

    # remove URLs
    text = re.sub(r"http\S+", "", text)

    # remove multiple spaces
    text = re.sub(r"\s+", " ", text)

    return text.strip()


df["clean_abstract"] = df["abstract"].apply(clean_text)

df.to_csv(OUTPUT_PATH, index=False)

print("Cleaned dataset saved to:", OUTPUT_PATH)
