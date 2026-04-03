# Simple Pandas Auto-Cleaner

A lightweight Python utility to automate the most repetitive parts of data preprocessing. 

### What it does:
* **Smart Dropping:** Automatically removes columns with >50% missing values or zero variation.
* **Auto-Imputation:** Fills numerical gaps with the `mean` and categorical gaps with the `mode`.
* **Date Splitting:** Detects date columns and breaks them into Year/Month/Day/Weekday features for better machine learning compatibility.
* **Audit Trail:** Returns a report dictionary detailing every change made to the dataset.

### Usage:
```python
import pandas as pd
from cleaner import auto_clean

df = pd.read_csv("your_messy_data.csv")
cleaned_df, report = auto_clean(df)

print(report)
