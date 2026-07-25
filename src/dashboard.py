import streamlit as st
import pandas as pd
import os

st.set_page_config(
    page_title="Dynamic Pricing Dashboard",
    page_icon="🏨",
    layout="wide"
)

# -----------------------------
# Title
# -----------------------------
st.title("🏨 Travel & Hospitality - Dynamic Pricing")

st.markdown("""
### Reinforcement Learning for Hotel Dynamic Pricing

This project uses a Q-Learning agent to learn optimal hotel room pricing
based on customer demand, room availability, and booking horizon.
""")

st.divider()

col1, col2, col3 = st.columns(3)

col1.metric("Algorithm", "Q-Learning")
col2.metric("Environment", "Hotel Pricing")
col3.metric("Framework", "Streamlit")

st.divider()

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("Navigation")

section = st.sidebar.radio(
    "Select Section",
    [
        "Project Overview",
        "Dataset",
        "Training Results",
        "Evaluation Results"
    ]
)

# -----------------------------
# Project Overview
# -----------------------------
if section == "Project Overview":

    st.header("Project Overview")

    st.info("""
This project applies Q-Learning to optimize hotel room pricing.

The agent learns pricing strategies based on:

• Remaining rooms

• Days remaining

• Customer demand

The objective is to maximize hotel revenue while reducing unsold inventory.
""")

# -----------------------------
# Dataset
# -----------------------------
elif section == "Dataset":

    st.header("Dataset Information")

    dataset_path = "data/processed/hotel_bookings_processed.csv"

    if os.path.exists(dataset_path):

        df = pd.read_csv(dataset_path)

        col1, col2, col3 = st.columns(3)

        col1.metric("Rows", df.shape[0])
        col2.metric("Columns", df.shape[1])
        col3.metric("Missing Values", int(df.isnull().sum().sum()))

        st.subheader("Dataset Preview")

        st.dataframe(df.head(10), use_container_width=True)

    else:

        st.error("Processed dataset not found.")

# -----------------------------
# Training Results
# -----------------------------
elif section == "Training Results":

    st.header("Training Results")

    training_file = "results/training_results.txt"
    reward_plot = "results/training_rewards.png"

    if os.path.exists(training_file):

        with open(training_file, "r") as file:
            training_data = file.read()

        st.subheader("Training Summary")

        st.text(training_data)

    else:

        st.warning("Training results not found.")

    st.divider()

    if os.path.exists(reward_plot):

        st.subheader("Training Reward Visualization")

        st.image(
            reward_plot,
            caption="Reward per Episode",
            use_container_width=True
        )

    else:

        st.warning("Training reward graph not found.")

# -----------------------------
# Evaluation Results
# -----------------------------
elif section == "Evaluation Results":

    st.header("Evaluation Results")

    evaluation_file = "results/evaluation_report.txt"

    if os.path.exists(evaluation_file):

        with open(evaluation_file, "r") as file:
            evaluation_data = file.read()

        st.subheader("Evaluation Report")

        st.text(evaluation_data)

    else:

        st.warning("Evaluation report not found.")