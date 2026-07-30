"""
Utility Functions
Travel & Hospitality - Reinforcement Learning for Dynamic Pricing
"""

import os
import pandas as pd


DATA_PATH = "data/hotel_bookings.csv"
PROCESSED_PATH = "data/processed/hotel_bookings_processed.csv"


def load_dataset():

    df = pd.read_csv(DATA_PATH)

    return df


def dataset_summary(df):

    print("\nDataset Shape:")
    print(df.shape)

    print("\nColumns:")
    print(df.columns.tolist())

    print("\nMissing Values:")
    print(df.isnull().sum())


def preprocess_dataset(df):

    original_rows = len(df)

    # Handle missing values
    df["children"] = df["children"].fillna(0)
    df["country"] = df["country"].fillna("Unknown")
    df["agent"] = df["agent"].fillna(0)
    df["company"] = df["company"].fillna(0)

    # Remove duplicates
    df = df.drop_duplicates()

    removed_duplicates = original_rows - len(df)

    # Convert reservation status date
    df["reservation_status_date"] = pd.to_datetime(
        df["reservation_status_date"]
    )

    # Create booking duration feature
    df["booking_duration"] = (
        df["stays_in_weekend_nights"]
        + df["stays_in_week_nights"]
    )

    # Create processed folder if it doesn't exist
    os.makedirs("data/processed", exist_ok=True)

    # Save processed dataset
    df.to_csv(PROCESSED_PATH, index=False)

    print("\nDataset preprocessing completed successfully!")
    print(f"Duplicates Removed : {removed_duplicates}")
    print(f"Processed Dataset Saved : {PROCESSED_PATH}")

    return df


if __name__ == "__main__":

    df = load_dataset()

    dataset_summary(df)

    df = preprocess_dataset(df)

    print("\nProcessed Dataset Shape:")
    print(df.shape)