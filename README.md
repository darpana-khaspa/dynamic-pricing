# 🏨 Travel & Hospitality – Reinforcement Learning for Dynamic Pricing

## 📌 Overview

This project implements an AI-powered **Hotel Dynamic Pricing System** using **Reinforcement Learning (Q-Learning)**. The system recommends optimal hotel room prices by analyzing booking demand, occupancy rate, room availability, room type, and booking horizon. The objective is to maximize hotel revenue while maintaining competitive pricing and improving customer satisfaction.

The project includes a simulated hotel pricing environment, Q-Learning model training, performance evaluation, and an interactive Streamlit dashboard for hotel managers to make intelligent pricing decisions.

---

# 🚀 Features

- 🤖 AI-powered room price recommendations
- 🏨 Hotel Manager Dashboard
- 📊 Hotel booking dataset analytics
- 📈 Q-Learning model training and evaluation
- 💰 Revenue and occupancy insights
- 📋 Booking summary and pricing recommendations
- 📉 Training reward visualization
- 🎯 Interactive Streamlit web application

---

# 🛠️ Tech Stack

- Python
- Streamlit
- Pandas
- NumPy
- Matplotlib
- Reinforcement Learning (Q-Learning)
- Git & GitHub

---

# 📂 Project Structure

```
dynamic-pricing/
│
├── assets/
│   └── hotel_logo.png
│
├── data/
│   ├── hotel_bookings.csv
│   └── processed/
│
├── docs/
│
├── results/
│   ├── training_results.txt
│   ├── evaluation_report.txt
│   └── training_rewards.png
│
├── src/
│   ├── baseline.py
│   ├── dashboard.py
│   ├── dqn.py
│   ├── environment.py
│   ├── evaluate.py
│   ├── qlearning.py
│   ├── train.py
│   └── utils.py
│
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/darpana-khaspa/dynamic-pricing.git
```

Move into the project directory:

```bash
cd dynamic-pricing
```

Install the required packages:

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Project

Launch the Streamlit dashboard:

```bash
streamlit run src/dashboard.py
```

---

# 📊 Dataset

The project uses the **Hotel Booking Demand Dataset**, which contains booking information collected from hotels. The dataset includes attributes such as:

- Hotel Type
- Arrival Date
- Lead Time
- Room Type
- Booking Status
- Customer Details
- Length of Stay
- Reservation Information

The dataset is preprocessed before training the Reinforcement Learning agent to simulate realistic hotel pricing scenarios.

---

# 🧠 Reinforcement Learning Workflow

1. Load and preprocess the hotel booking dataset.
2. Create the hotel pricing environment.
3. Initialize the Q-Learning agent.
4. Train the agent over multiple episodes.
5. Update Q-values using the reward mechanism.
6. Evaluate the learned pricing strategy.
7. Generate intelligent room price recommendations.
8. Display analytics and results through the Streamlit dashboard.

---

# 📅 Week-wise Implementation

## ✅ Week 1 – Project Setup & Environment Development

- Understood project objectives and workflow.
- Explored the Hotel Booking Demand dataset.
- Organized the project directory structure.
- Developed the Hotel Pricing Environment to simulate pricing scenarios.
- Implemented the baseline pricing strategy.
- Configured the GitHub repository and pushed initial commits.

---

## ✅ Week 2 – Reinforcement Learning Implementation

- Implemented the Q-Learning algorithm.
- Defined states, actions, rewards, learning rate, and discount factor.
- Trained the Q-Learning agent using multiple episodes.
- Updated the Q-table for optimal pricing decisions.
- Evaluated training performance using cumulative rewards.

---

## ✅ Week 3 – Dashboard Development & Analytics

- Developed an interactive Streamlit dashboard.
- Designed the Hotel Manager Dashboard.
- Added AI-powered Price Recommendation module.
- Implemented Dataset Analytics with visualizations.
- Added Training Results and Evaluation Results modules.
- Improved dashboard layout and user experience.

---

## ✅ Week 4 – Testing, Documentation & Deployment

- Tested the complete pricing workflow.
- Fixed dashboard syntax and runtime errors.
- Improved project structure and code readability.
- Resolved Git merge conflicts and merged feature branches into the main branch.
- Prepared the project report and technical documentation.
- Updated the README with project information and usage instructions.
- Finalized the project for internship submission.

---

# 📊 Dashboard Modules

### 🏨 Hotel Manager Dashboard

Displays important hotel performance indicators including:

- Occupancy Rate
- Room Availability
- Daily Revenue
- Weekly Revenue Trends
- Hotel Status

---

### 💰 Price Recommendation

Allows hotel managers to enter booking details and receive AI-generated room pricing recommendations using the trained Q-Learning model.

---

### 📈 Dataset Analytics

Provides visual insights into:

- Booking distribution
- Hotel types
- Reservation status
- Monthly booking trends
- Occupancy statistics

---

### 🎯 Training Results

Displays:

- Training summary
- Episode rewards
- Learning performance
- Training statistics

---

### 📋 Evaluation Results

Shows:

- Average Reward
- Best Reward
- Worst Reward
- Model Evaluation Summary

---

# 🎯 Future Enhancements

- Implement Deep Q-Network (DQN)
- Integrate real-time hotel booking APIs
- Add seasonal demand forecasting
- Perform competitor price analysis
- Deploy on cloud platforms
- Support multi-hotel pricing optimization
- Develop a mobile application
- Integrate customer feedback into pricing decisions

---

# 👩‍💻 Contributors

- Darpana Khaspa
- Srimani Deepika Krishna

---

# 📄 License

This project is developed for **educational and internship purposes**.