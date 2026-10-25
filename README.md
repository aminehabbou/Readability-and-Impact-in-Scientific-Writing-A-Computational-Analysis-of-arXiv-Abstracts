<div align="center">

# 📚 Readability and Impact in Scientific Writing

### A Computational Analysis of arXiv Abstracts

**Do scientific abstracts become more influential when they are easier to read? And can AI make them easier to understand?**

<p>
  <img src="https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Pandas-150458?logo=pandas&logoColor=white" alt="Pandas">
  <img src="https://img.shields.io/badge/NumPy-013243?logo=numpy&logoColor=white" alt="NumPy">
  <img src="https://img.shields.io/badge/SciPy-8CAAE6?logo=scipy&logoColor=white" alt="SciPy">
  <img src="https://img.shields.io/badge/statsmodels-Statistical%20Modeling-4051B5" alt="statsmodels">
  <img src="https://img.shields.io/badge/Matplotlib-Visualization-11557C" alt="Matplotlib">
  <img src="https://img.shields.io/badge/Seaborn-Visualization-4C72B0" alt="Seaborn">
  <img src="https://img.shields.io/badge/Jupyter-Notebook-F37626?logo=jupyter&logoColor=white" alt="Jupyter">
  <img src="https://img.shields.io/badge/arXiv-Research%20Data-B31B1B" alt="arXiv">
  <img src="https://img.shields.io/badge/Ollama-Local%20LLM-black" alt="Ollama">
</p>

<p>
  <img src="https://img.shields.io/badge/Project-Computational%20Text%20Analysis-2E8B57" alt="Computational Text Analysis">
  <img src="https://img.shields.io/badge/Focus-Readability%20%7C%20Citations%20%7C%20LLMs-6A5ACD" alt="Research Focus">
</p>

</div>

---

## 🔎 Project Overview

**Readability and Impact in Scientific Writing** is a computational research project investigating the relationship between the readability of scientific abstracts, their citation impact, and the readability of AI-rewritten abstracts.

Using arXiv research papers from **computer science, mathematics, and physics** published between **2010 and 2018**, the project combines text preprocessing, established readability formulas, citation data, statistical analysis, and local large language model (LLM) rewriting.

The analysis is organized around three research questions:

1. **Readability across disciplines:** How difficult are scientific abstracts to read across computer science, mathematics, and physics?
2. **Readability and citations:** Is abstract readability associated with citation counts?
3. **Human-written vs. AI-rewritten abstracts:** Are abstracts rewritten by a local language model easier to read than the original versions?

## ✨ Key Findings

The following headline results are reported in the accompanying project report.

| Finding | Reported result |
|---|---:|
| Final citation-linked dataset | 2,272 abstracts |
| Mean Flesch Reading Ease score | 24.18 |
| Flesch Reading Ease by field | Physics: 19.89 · Computer science: 23.34 · Mathematics: 29.26 |
| Largest absolute Spearman correlation between a readability metric and citations | \|ρ\| ≤ 0.153 |
| OLS model \(R^2\), using four readability measures | 0.041 |
| Abstracts in the human-vs-AI comparison | 150 |
| Human vs. AI readability comparison | AI rewrites were reported as harder to read; report gives \(p < 10^{-8}\) |

**Interpretation:** In this dataset, scientific abstracts were generally difficult according to conventional readability formulas. Readability metrics had only weak associations with citation counts, and the report found that the AI-generated rewrites were not easier to read than the human-written originals.

These are findings from this project's particular sample and methods; they should not be interpreted as universal claims about all scientific writing or all language models.

## 🧪 Research Workflow

```text
arXiv API
   │
   ▼
Collect abstracts and paper metadata
   │
   ▼
Clean text
(remove LaTeX commands, math snippets, URLs, line breaks)
   │
   ├───────────────────────────────┐
   ▼                               ▼
Calculate readability          Retrieve citation counts
(Flesch, FK Grade, Fog, SMOG)  (Semantic Scholar API)
   │                               │
   └───────────────┬───────────────┘
                   ▼
          Merge and clean dataset
                   │
          ┌────────┴────────┐
          ▼                 ▼
   RQ1: Field-level     RQ2: Readability–
   readability          citation analysis
                            │
                            ▼
                    Correlations + OLS

   Human abstracts ──► Ollama / TinyLlama
          │                    │
          └─────────┬──────────┘
                    ▼
          RQ3: Paired readability
               comparisons
```

## 🧠 Readability Metrics

The project uses four established readability formulas through the `textstat` Python package.

| Metric | What it measures | Typical interpretation |
|---|---|---|
| **Flesch Reading Ease** | A score based on sentence length and syllables per word | Lower scores indicate more difficult text |
| **Flesch–Kincaid Grade Level** | Estimated US school grade level needed to read the text | Higher scores indicate greater difficulty |
| **Gunning Fog Index** | Approximate years of education needed to understand text on first reading | Higher scores indicate greater difficulty |
| **SMOG Index** | Grade-level estimate based on polysyllabic words | Higher scores indicate greater difficulty |

Readability formulas are useful, reproducible indicators of surface-level linguistic complexity. They do not directly measure scientific correctness, conceptual difficulty, or actual reader comprehension.

## 📊 Statistical Analysis

The citation-impact analysis includes:

- **Spearman rank correlation** to examine monotonic relationships between readability metrics and citation counts.
- **Pearson correlation** where used in the analysis notebooks.
- **Log transformation** of citation counts using \(\ln(\text{citations} + 1)\) to reduce the impact of a right-skewed distribution.
- **Ordinary least squares (OLS) regression** using the four readability measures as predictors of log-transformed citations.
- **Paired-samples t-test and Wilcoxon signed-rank test** to compare readability scores for original and AI-rewritten abstracts.
- **Visual analysis** with distributions, field comparisons, scatter plots, and citation-quartile comparisons.

### Selected reported statistics

| Analysis | Result |
|---|---|
| Flesch Reading Ease vs. citation count | Spearman \(ρ = -0.153\) |
| Flesch–Kincaid Grade Level vs. citation count | Spearman \(ρ = 0.114\) |
| Gunning Fog vs. citation count | Spearman \(ρ = 0.082\) |
| SMOG vs. citation count | Spearman \(ρ = 0.094\) |
| OLS model \(R^2\) | 0.041 |
| AI vs. human readability comparison | Reported as statistically significant, \(p < 10^{-8}\) |

The small reported \(R^2\) indicates that the four readability features explain only a small share of variation in citation counts in the fitted model. Statistical significance alone does not establish a strong or practically important relationship.

## 🛠️ Tech Stack

### Core language and data analysis

<p>
  <img src="https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Pandas-150458?logo=pandas&logoColor=white" alt="Pandas">
  <img src="https://img.shields.io/badge/NumPy-013243?logo=numpy&logoColor=white" alt="NumPy">
</p>

- **Python** — data collection, preprocessing, analysis, and experiment orchestration.
- **Pandas** — tabular data cleaning, joining, filtering, and CSV input/output.
- **NumPy** — numerical operations and data analysis.

### Statistics and visualization

<p>
  <img src="https://img.shields.io/badge/SciPy-8CAAE6?logo=scipy&logoColor=white" alt="SciPy">
  <img src="https://img.shields.io/badge/statsmodels-Statistical%20Models-4051B5" alt="statsmodels">
  <img src="https://img.shields.io/badge/Matplotlib-11557C?logo=plotly&logoColor=white" alt="Matplotlib">
  <img src="https://img.shields.io/badge/Seaborn-4C72B0" alt="Seaborn">
</p>

- **SciPy** — statistical tests, correlation analysis, and paired comparisons.
- **statsmodels** — OLS regression and statistical summaries.
- **Matplotlib** — plots and figures.
- **Seaborn** — statistical visualizations.

### Text analysis and data sources

<p>
  <img src="https://img.shields.io/badge/textstat-Readability%20Metrics-6A5ACD" alt="textstat">
  <img src="https://img.shields.io/badge/arXiv-API-B31B1B" alt="arXiv API">
  <img src="https://img.shields.io/badge/Semantic%20Scholar-Citation%20Data-1769AA" alt="Semantic Scholar">
  <img src="https://img.shields.io/badge/Requests-HTTP%20API-2CA5E0" alt="Requests">
</p>

- **textstat** — Flesch Reading Ease, Flesch–Kincaid, Gunning Fog, and SMOG scores.
- **arxiv Python package** — collecting paper metadata and abstracts from arXiv.
- **Semantic Scholar API** — retrieving citation counts.
- **Requests** — HTTP requests to external APIs.
- **Regular expressions (`re`)** — removing selected LaTeX commands, math snippets, URLs, and whitespace patterns.

### AI-assisted text generation and workflow

<p>
  <img src="https://img.shields.io/badge/Ollama-Local%20LLM-black" alt="Ollama">
  <img src="https://img.shields.io/badge/TinyLlama-Text%20Rewriting-8A2BE2" alt="TinyLlama">
  <img src="https://img.shields.io/badge/Jupyter-Notebooks-F37626?logo=jupyter&logoColor=white" alt="Jupyter">
  <img src="https://img.shields.io/badge/tqdm-Progress%20Bars-FFC107" alt="tqdm">
</p>

- **Ollama** — running a language model locally for the abstract-rewriting experiment.
- **TinyLlama** — the local model named in the project report for generating rewritten abstracts.
- **Jupyter Notebook** — exploratory analysis, experiments, and visual reporting.
- **tqdm** — progress bars for long-running data collection tasks.
- **time** — delays and retry pacing for API requests.

## 🗂️ Repository Structure

```text
Readability-and-Impact-in-Scientific-Writing/
├── data/
│   ├── raw/
│   │   └── arxiv_2010_2018.csv
│   └── processed/
│       ├── arxiv_abstracts_clean.csv
│       ├── arxiv_2010_2018_with_citations.csv
│       ├── arxiv_2010_2018_clean_citations.csv
│       ├── arxiv_with_readability.csv
│       ├── arxiv_ai_rewritten.csv
│       └── rq3_readability_comparison.csv
├── src/
│   ├── collect_arxiv.py
│   ├── clean_abstracts.py
│   ├── get_citations.py
│   ├── clean_abstracts_citations.py
│   ├── readability_analysis.ipynb
│   ├── correlation_readability_citations.ipynb
│   ├── generate_ai_rewritten_abstracts.ipynb
│   └── ai_abstracts_analysis_and_comparison_with_human_abstracts.ipynb
├── Readability and Impact In scientific writing-- Project Report.pdf
└── README.md
```

*The archive includes a local Python environment directory (`acad_w/Lib/site-packages`). It is intentionally omitted from this suggested repository tree; virtual environments are normally recreated locally rather than committed to Git.*

## 🚀 Getting Started

### 1. Prerequisites

- Python 3.10 or a compatible Python version.
- Git (optional, if cloning the repository).
- Internet access for arXiv and Semantic Scholar API calls.
- Ollama installed and a TinyLlama model pulled locally for the AI-rewriting workflow.

### 2. Clone the repository

Replace the placeholders with your own GitHub username and repository name:

```bash
git clone https://github.com/<your-username>/<your-repository>.git
cd <your-repository>
```

### 3. Create a virtual environment

**Windows PowerShell**
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

**macOS / Linux**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 4. Install the Python dependencies

```bash
python -m pip install --upgrade pip
pip install pandas numpy matplotlib seaborn scipy statsmodels textstat arxiv requests tqdm ollama jupyter
```

> Dependency versions are not pinned in this README because a project-level requirements file was not present in the supplied archive. For reproducible setup, test the workflow in a clean environment and save the working versions in `requirements.txt`.

### 5. Set up the local language model

Install Ollama from [ollama.com](https://ollama.com/), then pull TinyLlama:

```bash
ollama pull tinyllama
```

Ensure Ollama is running before executing the AI-rewriting notebook. The exact model name used in code should match the model installed locally.

### 6. Run the analysis

From the repository root, launch Jupyter:

```bash
jupyter notebook
```

Suggested workflow:

1. `src/collect_arxiv.py` — collect paper metadata and abstracts.
2. `src/clean_abstracts.py` — clean abstract text.
3. `src/get_citations.py` — retrieve citation counts from Semantic Scholar.
4. `src/clean_abstracts_citations.py` — remove records without citation data.
5. `src/readability_analysis.ipynb` — calculate readability metrics and examine differences across fields.
6. `src/correlation_readability_citations.ipynb` — investigate associations between readability and citation impact.
7. `src/generate_ai_rewritten_abstracts.ipynb` — generate AI rewrites using the local Ollama model.
8. `src/ai_abstracts_analysis_and_comparison_with_human_abstracts.ipynb` — compare original and AI-rewritten abstracts.

**Important:** Some scripts use fixed relative paths and expect to be run from the repository root. Check the input/output paths at the top of each script before rerunning it. API availability, rate limits, and changes to external services may affect data collection.

## 📂 Data and Reproducibility

The project archive includes raw and processed CSV files. The main analysis uses arXiv abstracts from 2010–2018 in three broad areas:

- Computer science
- Mathematics
- Physics

Citation counts are retrieved from Semantic Scholar. Citation counts can change over time, so a fresh API run may not reproduce the exact values used in the original report.

For a reproducible rerun, record the collection date, package versions, model name, preprocessing choices, and analysis parameters. The original report describes an AI rewrite comparison using a subset of 150 papers and a locally run TinyLlama model.

## ⚠️ Limitations and Considerations

- **Readability is not comprehension:** formula-based scores do not measure factual accuracy, scientific depth, or actual reader understanding.
- **Citation counts have many drivers:** field norms, paper age, collaboration, topic popularity, venue, and research quality may all affect citations.
- **Association is not causation:** the correlation and regression analyses do not show that changing readability causes citation impact to change.
- **Disciplinary comparability:** technical vocabulary and mathematical notation may affect readability formulas differently across fields.
- **Text preprocessing matters:** removing LaTeX can alter sentence length and syllable counts, influencing readability scores.
- **LLM generalizability:** the AI comparison uses a limited sample and a specific local model; results should not be generalized to all AI systems.
- **External API constraints:** arXiv and Semantic Scholar can change their APIs, enforce rate limits, or return incomplete data.
- **Reproduction details:** exact package versions and all runtime settings should be recorded before treating the reported results as a fully reproducible benchmark.

## 📖 References and Data Sources

- **arXiv** — research paper repository: https://arxiv.org/
- **Semantic Scholar API** — citation metadata: https://www.semanticscholar.org/product/api
- **Ollama** — local model runner: https://ollama.com/
- **textstat** — text readability statistics: https://pypi.org/project/textstat/

Please respect the data sources' terms of use and API policies when collecting or redistributing data.

## 👨‍💻 Author

**Amine Habbou**
Master's Student in Data Engineering
Constructor University
Bremen, Germany

**Project:** *Readability and Impact in Scientific Writing: A Computational Analysis of arXiv Abstracts*  
**Context:** Academic research project · 15 May 2026

This project was conducted and documented by me, combining data collection, text preprocessing, readability analysis, statistical modeling, citation analysis, and an AI-assisted abstract comparison.

---

<div align="center">

**If this project is useful, consider giving the repository a ⭐**

*Built with Python, open research data, statistical analysis, and curiosity about how science communicates.*

</div>
