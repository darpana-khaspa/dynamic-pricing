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


if __name__ == "__main__":

    data = load_dataset()

    dataset_summary(data)