# 🏨 Travel & Hospitality – Reinforcement Learning for Dynamic Pricing

## 📌 Overview

This project implements an AI-powered Hotel Dynamic Pricing System using Reinforcement Learning (Q-Learning). The system recommends optimal room prices by analyzing hotel occupancy, booking demand, room availability, room type, and booking horizon. The objective is to maximize hotel revenue while maintaining competitive pricing and improving occupancy.

---

## 🚀 Features

- AI-powered room price recommendations
- Q-Learning based pricing strategy
- Interactive Streamlit dashboard
- Hotel booking dataset analytics
- Training and evaluation modules
- Revenue and occupancy insights
- Hotel performance visualization

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Pandas
- NumPy
- Matplotlib
- Reinforcement Learning (Q-Learning)
- Git & GitHub

---

## 📂 Project Structure

```
dynamic-pricing/
│
├── assets/
├── data/
│   ├── hotel_bookings.csv
│   └── processed/
├── docs/
├── results/
├── src/
│   ├── baseline.py
│   ├── dashboard.py
│   ├── environment.py
│   ├── evaluate.py
│   ├── qlearning.py
│   ├── train.py
│   └── utils.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/darpana-khaspa/dynamic-pricing.git
```

Navigate to the project folder:

```bash
cd dynamic-pricing
```

Install the required packages:

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project

Launch the Streamlit dashboard:

```bash
streamlit run src/dashboard.py
```

---

## 📊 Dataset

The project uses the Hotel Booking Demand Dataset containing booking details such as:

- Hotel type
- Arrival date
- Lead time
- Room type
- Booking status
- Customer information
- Length of stay

The dataset is preprocessed before training the Reinforcement Learning agent.

---

## 🧠 Reinforcement Learning Workflow

1. Load and preprocess booking data.
2. Create the hotel pricing environment.
3. Train the Q-Learning agent.
4. Learn optimal pricing strategies.
5. Evaluate agent performance.
6. Display results in the Streamlit dashboard.

---

## 📈 Dashboard Modules

- Hotel Manager Dashboard
- Price Recommendation
- Dataset Analytics
- Training Results
- Evaluation Results

---

## 🎯 Future Enhancements

- Deep Q-Network (DQN)
- Real-time hotel booking APIs
- Seasonal demand forecasting
- Competitor price analysis
- Cloud deployment
- Multi-hotel pricing support

---

## 👩‍💻 Contributors

- Darpana Khaspa
- Srimani Deepika Krishna

---

## 📄 License

This project is developed for educational and internship purposes.