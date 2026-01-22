# Budget vs Actual Analysis using Python

"""
Variance Analysis Script
------------------------
This script performs Budget vs Actual analysis.
It is designed to be reusable and production-ready.

Author: Business Analytics Project
"""

import pandas as pd


def load_data(file_path: str) -> pd.DataFrame:
    """
    Load budget vs actual data from CSV file.
    """
    return pd.read_csv(file_path)


def calculate_variance(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate variance and variance percentage.
    """
    df = df.copy()
    df["Variance"] = df["Actual_Amount"] - df["Budgeted_Amount"]
    df["Variance_Percent"] = (df["Variance"] / df["Budgeted_Amount"]) * 100
    return df


def classify_variance(df: pd.DataFrame) -> pd.DataFrame:
    """
    Classify variance as Favorable, Unfavorable, or On Budget.
    """
    def status(row):
        if row["Variance"] > 0:
            return "Unfavorable"
        elif row["Variance"] < 0:
            return "Favorable"
        return "On Budget"

    df = df.copy()
    df["Variance_Status"] = df.apply(status, axis=1)
    return df


def summarize_by_category(df: pd.DataFrame) -> pd.DataFrame:
    """
    Aggregate total variance by category.
    """
    summary = (
        df.groupby("Category")["Variance"]
        .sum()
        .reset_index()
        .sort_values(by="Variance", ascending=False)
    )
    return summary


if __name__ == "__main__":
    # Example execution
    data_path = "../data/budget_actual_data.csv"

    df = load_data(data_path)
    df = calculate_variance(df)
    df = classify_variance(df)

    summary = summarize_by_category(df)

    print("Full dataset with variance:")
    print(df)

    print("\nVariance summary by category:")
    print(summary)






