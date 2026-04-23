```markdown
# 🧹 Simple Pandas Auto-Cleaner

A lightweight Python utility to automate the most repetitive parts of data preprocessing — now with a live web app!

🌐 **[Try the live app here](https://simple-pandas-cleaner.streamlit.app/)**

---

## What it does

- **Smart Dropping:** Automatically removes columns with >50% missing values or zero variation.
- **Auto-Imputation:** Fills numerical gaps with the `mean` and categorical gaps with the `mode`.
- **Date Splitting:** Detects date columns and breaks them into Year/Month/Day/Weekday features for better machine learning compatibility.
- **Audit Trail:** Returns a report dictionary detailing every change made to the dataset.

---

## Installation

Make sure you have the required libraries installed:

```bash
pip install -r requirements.txt
```

---

## Usage (Python)

```python
import pandas as pd
from cleaner import auto_clean

df = pd.read_csv("your_messy_data.csv")
cleaned_df, report = auto_clean(df)

print(report)
```

## Advanced Usage

```python
# Protect important columns from being dropped
cleaned_df, report = auto_clean(df, important_cols=['id', 'target'])

# Disable date splitting
cleaned_df, report = auto_clean(df, split_dates=False)

# Change the missing value threshold (default is 50%)
cleaned_df, report = auto_clean(df, missing_threshold=0.3)
```

---

## Web App

Don't want to code? Use the live Streamlit app to upload your CSV or Excel file and download a cleaned version instantly.

🌐 **[simple-pandas-cleaner.streamlit.app](https://simple-pandas-cleaner.streamlit.app/)**

---

## Tech Stack

- Python
- Pandas
- Streamlit

---

## License

MIT
```
