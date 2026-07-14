"""
Utility Functions
Travel & Hospitality - Reinforcement Learning for Dynamic Pricing
"""

import pandas as pd


def load_dataset(file_path="data/hotel_bookings.csv"):
    """
    Load the hotel booking dataset.
    """
    df = pd.read_csv(file_path)
    return df


def dataset_summary(df):
    """
    Display basic dataset information.
    """
    print("\nDataset Shape:", df.shape)
    print("\nColumns:\n", df.columns.tolist())
    print("\nMissing Values:\n", df.isnull().sum())

def preprocess_dataset(df):
    """
    Perform basic preprocessing on the hotel booking dataset.
    """

    # Fill missing values
    df["children"] = df["children"].fillna(0)
    df["country"] = df["country"].fillna("Unknown")
    df["agent"] = df["agent"].fillna(0)
    df["company"] = df["company"].fillna(0)

    # Remove duplicate rows
    df = df.drop_duplicates()

    return df

if __name__ == "__main__":

 data = load_dataset()

 data = preprocess_dataset(data)

 dataset_summary(data)

 print("\nDataset preprocessing completed successfully!")