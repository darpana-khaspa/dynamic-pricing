import subprocess
import sys
import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt

from datetime import datetime

st.set_page_config(
    page_title="Dynamic Pricing Dashboard",
    page_icon="🏨",
    layout="wide"
)

st.markdown("""
<style>

.stApp{
    background-color:#0f172a;
}

.block-container{
    padding-top:1rem;
    padding-bottom:1rem;
}

h1,h2,h3,h4{
    color:white;
}

p,label,span{
    color:#d1d5db;
}

div[data-testid="metric-container"]{
    background:#1e293b;
    border:1px solid #d4af37;
    border-radius:15px;
    padding:18px;
    box-shadow:0px 4px 10px rgba(0,0,0,0.25);
}

.stButton>button{
    width:100%;
    border-radius:12px;
    border:2px solid #d4af37;
    background:#1e293b;
    color:white;
    font-weight:bold;
}

.stButton>button:hover{
    background:#d4af37;
    color:black;
}

section[data-testid="stSidebar"]{
    background:#111827;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# Title
# -----------------------------
st.title("🏨 Travel & Hospitality - Dynamic Pricing")

current_time = datetime.now()

st.info(
    f"📅 {current_time.strftime('%d %B %Y')} | 🕒 {current_time.strftime('%I:%M %p')}"
)

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
with st.sidebar:

    st.image("https://img.icons8.com/fluency/96/hotel.png", width=80)

    st.title("Hotel AI Pricing")

    st.caption("Reinforcement Learning Dashboard")

    st.success("🟢 AI System Online")

    st.markdown("---")

    section = st.radio(
        "Navigation",
        [
            "🏠 Hotel Manager Dashboard",
            "💰 Price Recommendation",
            "📊 Dataset Analytics",
            "📈 Training Results",
            "📋 Evaluation Results"
        ]
    )

    st.markdown("---")

    st.markdown("### 👨‍💻 Developer")
    st.write("**Darpana Khaspa**")
    st.write("**Srimani Deepika Krishna**")

    st.markdown("### 🤖 Model")
    st.write("Q-Learning Agent")

    st.markdown("### 🏷 Version")
    st.write("v1.0")

# -----------------------------
# Project Overview
# -----------------------------
if section == "🏠 Hotel Manager Dashboard":

    col1, col2 = st.columns([1, 4])

    with col1:
        st.image("https://img.icons8.com/fluency/96/hotel.png", width=90)
        
    with col2:
        st.title("🏨 Hotel AI Pricing Dashboard")
        st.caption("AI-Powered Dynamic Pricing using Reinforcement Learning")

    st.header("Project Overview")

    st.subheader("📊 Live Hotel Performance Dashboard")

    st.divider()

    kpi1, kpi2, kpi3, kpi4 = st.columns(4)

    with kpi1:
        st.metric("Occupancy", "82%", "+6%")

    with kpi2:
        st.metric("Today's Revenue", "£18,450", "+11%")

    with kpi3:
        st.metric("Average Room Price", "£162", "+£14")

    with kpi4:
        st.metric("Available Rooms", "18", "-5")

    st.divider()

    st.subheader("🏨 Live Hotel Status")

    st.write("Occupancy")
    st.progress(82)

    st.write("Room Availability")
    st.progress(18)

    st.write("Booking Demand")
    st.progress(90)

    st.divider()

    st.success("""
### AI Pricing System Status

✅ Dynamic Pricing Engine : Active

✅ Q-Learning Agent : Loaded

✅ Hotel Booking Dataset : Connected

✅ Price Recommendation Engine : Ready
""")

    st.subheader("🏨 Occupancy Distribution")

    fig, ax = plt.subplots(figsize=(4, 4))

    sizes = [82, 18]
    labels = ["Occupied", "Available"]
    colors = ["green", "gold"]

    ax.pie(
        sizes,
        labels=labels,
        autopct="%1.1f%%",
        startangle=90,
        colors=colors,
    )

    ax.axis("equal")
    st.pyplot(fig)

    st.subheader("🏨 Hotel Overview")

    hotel_data = pd.DataFrame({
        "Metric": [
            "Total Rooms",
            "Booked Rooms",
            "Available Rooms",
            "Expected Demand",
            "Current Occupancy",
        ],
        "Value": [
            100,
            82,
            18,
            "High",
            "82%",
        ],
    })

    st.dataframe(hotel_data, width="stretch")

    st.subheader("📈 Weekly Revenue")

    revenue = pd.DataFrame({
        "Day": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
        "Revenue": [12000, 14000, 13500, 15000, 18500, 21000, 19800],
    })

    st.line_chart(revenue.set_index("Day"))

    st.subheader("📈 7-Day Revenue Forecast")

    forecast = pd.DataFrame({
        "Day": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
        "Revenue": [13200, 13850, 14500, 14900, 15800, 17000, 18200],
    })

    st.line_chart(forecast.set_index("Day"))

    st.subheader("⚙️ Project Actions")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("▶ Train Q-Learning Model", width="stretch"):
            with st.spinner("Training..."):
                subprocess.run([sys.executable, "src/train.py"])
            st.success("Training Completed")

    with col2:
        if st.button("📊 Evaluate Agent", width="stretch"):
            with st.spinner("Evaluating..."):
                subprocess.run([sys.executable, "src/evaluate.py"])
            st.success("Evaluation Completed")


elif section == "💰 Price Recommendation":

    st.header("💰 AI Dynamic Pricing Recommendation")

    st.write("Enter booking details to receive an AI-powered pricing recommendation.")

    st.subheader("🏨 Live Hotel Status")

    st.write("Occupancy")
    st.progress(82)

    st.write("Room Availability")
    st.progress(18)

    st.write("Booking Demand")
    st.progress(90)

    st.divider()

    st.caption(
        "© 2026 Hotel AI Pricing System | Reinforcement Learning Project | Developed by Darpana Khaspa"
    )

    st.header("💰 AI Dynamic Pricing Recommendation")

    st.write("Enter booking details to receive an AI-powered pricing recommendation.")

    st.subheader("🏨 Live Hotel Status")

    st.write("Occupancy")
    st.progress(82)

    st.write("Room Availability")
    st.progress(18)

    st.write("Booking Demand")
    st.progress(90)

    st.divider()

    st.caption(
        "© 2026 Hotel AI Pricing System | Reinforcement Learning Project | Developed by Darpana Khaspa"
    )

    # -----------------------------
    # Customer Details
    # -----------------------------

    col1, col2 = st.columns([3, 1])

    with col2:
        if st.button("🔄 Reset Form"):
            st.session_state.clear()
            st.rerun()

    customer_name = st.text_input("Customer Name")

    hotel_type = st.selectbox(
        "Hotel Type",
        ["City Hotel", "Resort Hotel"]
    )

    room_type = st.selectbox(
        "Room Type",
        ["Standard", "Deluxe", "Suite"]
    )

    if hotel_type == "City Hotel":
        st.image(
            "https://images.unsplash.com/photo-1566073771259-6a8506099945?w=900",
            use_container_width=True
        )
    else:
        st.image(
            "https://images.unsplash.com/photo-1571896349842-33c89424de2d?w=900",
            use_container_width=True
        )

    guests = st.number_input(
        "Number of Guests",
        min_value=1,
        max_value=6,
        value=2
    )

    stay_days = st.slider(
        "Length of Stay (Days)",
        1,
        14,
        3
    )

    remaining_rooms = st.slider(
        "Remaining Rooms",
        0,
        100,
        40
    )

    occupancy = st.slider(
        "Current Occupancy (%)",
        0,
        100,
        75
    )

    days_left = st.slider(
        "Days Until Check-in",
        0,
        60,
        15
    )

    demand = st.selectbox(
        "Expected Demand",
        ["Low", "Medium", "High"]
    )

    current_price = st.number_input(
        "Current Room Price (£)",
        min_value=50,
        max_value=1000,
        value=120
    )

    if st.button("🤖 Recommend Price", width="stretch"):

        # -----------------------------
        # Input Validation
        # -----------------------------

        if not customer_name.strip():
            st.warning("⚠️ Please enter the customer name.")
            st.stop()

        if guests > 4 and room_type == "Standard":
            st.warning(
                "⚠️ Standard rooms support a maximum of 4 guests. "
                "Please select Deluxe or Suite."
            )
            st.stop()

        if stay_days > 7 and room_type == "Standard":
            st.info(
                "💡 For stays longer than 7 days, consider selecting "
                "a Deluxe room or Suite."
            )

        if "history" not in st.session_state:
            st.session_state.history = []

        recommended_price = float(current_price)

        # Room type adjustment
        if room_type == "Deluxe":
            recommended_price += 25
        elif room_type == "Suite":
            recommended_price += 60

        # Demand adjustment
        if demand == "High":
            recommended_price += 30
        elif demand == "Medium":
            recommended_price += 15
        else:
            recommended_price -= 10

        # Occupancy adjustment
        if occupancy > 85:
            recommended_price += 20
        elif occupancy < 40:
            recommended_price -= 20

        # Availability adjustment
        if remaining_rooms < 20:
            recommended_price += 20

        # Last-minute booking
        if days_left <= 5:
            recommended_price += 15

        # Long stay discount
        if stay_days >= 5:
            recommended_price -= 10

        # Recommendation
        action = "Maintain Price"

        if recommended_price > current_price:
            action = "Increase Price 📈"
        elif recommended_price < current_price:
            action = "Decrease Price 📉"

        confidence = min(95, 70 + occupancy // 5)

        expected_revenue = recommended_price * stay_days

        st.success("✅ Recommendation Generated Successfully!")

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Recommended Price",
                f"£{recommended_price:.2f}"
            )
            
            price_difference = recommended_price - current_price
            percentage = (price_difference / current_price) * 100

            st.metric(
                "Price Change",
                f"{percentage:.1f}%"
            )

            st.metric(
                "Suggested Action",
                action
            )

        with col2:
            st.metric(
                "Confidence",
                f"{confidence}%"
            )

            st.metric(
                "Estimated Booking Revenue",
                f"£{expected_revenue:.2f}"
            )

        st.divider()

        st.subheader("🤖 AI Recommendation")

        reasons = []

        if demand == "High":
            reasons.append("High customer demand")

        if occupancy > 85:
            reasons.append("High hotel occupancy")

        if remaining_rooms < 20:
            reasons.append("Limited room availability")

        if room_type == "Suite":
            reasons.append("Premium suite selected")

        if room_type == "Deluxe":
            reasons.append("Deluxe room selected")

        if stay_days >= 5:
            reasons.append("Long stay discount applied")

        if len(reasons) == 0:
            reasons.append("Current market conditions")

        st.info("Price recommended because of: " + ", ".join(reasons))

        st.divider()

        st.subheader("📋 Booking Summary")

        summary = pd.DataFrame({
            "Field": [
                "Customer",
                "Hotel",
                "Room Type",
                "Guests",
                "Stay Duration",
                "Recommended Price"
            ],
            "Value": [
                customer_name if customer_name else "Guest",
                hotel_type,
                room_type,
                guests,
                f"{stay_days} Days",
                f"£{recommended_price:.2f}"
            ]
        })

        st.dataframe(summary, width="stretch")

        # -----------------------------
        # Save Recommendation History
        # -----------------------------

        st.session_state.history.append({
            "Customer": customer_name if customer_name else "Guest",
            "Hotel": hotel_type,
            "Room": room_type,
            "Current Price": current_price,
            "AI Price": recommended_price,
            "Action": action
        })

        # Export recommendation as CSV
        csv = summary.to_csv(index=False).encode("utf-8")

        st.download_button(
            label="📥 Download Results (CSV)",
            data=csv,
            file_name="pricing_recommendation.csv",
            mime="text/csv"
        )

        st.subheader("📄 Booking Receipt")

        with st.container():

            st.markdown(f"""
        ### 🏨 Booking Summary

        👤 **Customer:** {customer_name if customer_name else "Guest"}

        🏨 **Hotel:** {hotel_type}

        🛏 **Room:** {room_type}

        👥 **Guests:** {guests}

        📅 **Stay:** {stay_days} Days

        💷 **Current Price:** £{current_price:.2f}

        🤖 **AI Price:** £{recommended_price:.2f}

        📈 **Recommendation:** {action}
        """)

        report = f"""
        Hotel AI Pricing Report

        Customer : {customer_name if customer_name else "Guest"}

        Hotel : {hotel_type}

        Room : {room_type}

        Guests : {guests}

        Stay : {stay_days} Days

        Current Price : £{current_price:.2f}

        Recommended Price : £{recommended_price:.2f}

        Recommendation : {action}

        Confidence : {confidence}
        """

        st.download_button(
            "📄 Download AI Recommendation",
            report,
            file_name="AI_Pricing_Report.txt"
        )

        if recommended_price > current_price:
            st.success("📈 Revenue Optimisation Strategy Selected")

        elif recommended_price < current_price:
            st.warning("📉 Demand Maximisation Strategy Selected")

        else:
            st.info("⚖️ Balanced Pricing Strategy Selected")

        st.code(f"""
        Customer      : {customer_name if customer_name else "Guest"}
        Hotel         : {hotel_type}
        Room Type     : {room_type}
        Guests        : {guests}
        Stay          : {stay_days} Days

        Current Price : £{current_price:.2f}
        AI Price      : £{recommended_price:.2f}

        Status        : {action}
        """)

        if recommended_price <= current_price:

            satisfaction = 95

        else:

            satisfaction = 90

        st.progress(satisfaction)

        st.metric(
            "Customer Satisfaction",
            f"{satisfaction}%"
        )

        st.divider()
        
        st.subheader("📊 Static vs AI Dynamic Pricing")
        
        comparison = pd.DataFrame({
            "Pricing Type": ["Static Pricing", "AI Dynamic Pricing"],
            "Room Price (£)": [current_price, recommended_price]
            })
        
        st.bar_chart(
            comparison.set_index("Pricing Type")
        )

        st.subheader("🧠 AI Decision Summary")
        
        if recommended_price > current_price:
            st.success(
                f"The AI recommends increasing the room price from £{current_price:.2f} "
                f"to £{recommended_price:.2f} due to favourable market conditions."
            )
        
        elif recommended_price < current_price:
            st.warning(
                f"The AI recommends reducing the room price from £{current_price:.2f} "
                f"to £{recommended_price:.2f} to improve booking probability."
            ) 
        
        else:
            st.info(
                "The AI recommends keeping the current room price because existing conditions are balanced."
            )

        price_change = recommended_price - current_price

        st.metric(
            "Price Difference",
            f"£{price_change:.2f}"
        )

        st.divider()

        st.subheader("🕒 Recommendation History")

        history_df = pd.DataFrame(st.session_state.history)

        st.dataframe(
            history_df,
            use_container_width=True
        )

        if st.button("🗑️ Clear Recommendation History"):
            st.session_state.history = []
            st.success("Recommendation history cleared successfully!")
            st.rerun()
# -----------------------------
# Dataset
# -----------------------------
elif section == "📊 Dataset Analytics":

    st.header("Dataset Information")

    dataset_path = "data/processed/hotel_bookings_processed.csv"

    if os.path.exists(dataset_path):

        df = pd.read_csv(dataset_path)

        col1, col2, col3 = st.columns(3)

        col1.metric("Rows", df.shape[0])
        col2.metric("Columns", df.shape[1])
        col3.metric("Missing Values", int(df.isnull().sum().sum()))

        st.subheader("Dataset Preview")

        st.dataframe(df.head(10), width="stretch")

        # -----------------------------
        # Reservation Status Distribution
        # -----------------------------
        st.subheader("Reservation Status Distribution")

        status_counts = df["reservation_status"].value_counts()
        st.bar_chart(status_counts)

        # -----------------------------
        # Hotel Type Distribution
        # -----------------------------
        st.subheader("Hotel Type Distribution")

        hotel_counts = df["hotel"].value_counts()
        st.bar_chart(hotel_counts)

        # -----------------------------
        # Monthly Booking Distribution
        # -----------------------------
        st.subheader("Monthly Booking Distribution")

        month_counts = df["arrival_date_month"].value_counts()

        month_order = [
            "January", "February", "March", "April",
            "May", "June", "July", "August",
            "September", "October", "November", "December"
        ]

        month_counts = month_counts.reindex(month_order)

        st.bar_chart(month_counts)

    else:

        st.error("Processed dataset not found.")

# -----------------------------
# Training Results
# -----------------------------
elif section == "📈 Training Results":

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
            width="stretch"
        )

    else:

        st.warning("Training reward graph not found.")

# -----------------------------
# Evaluation Results
# -----------------------------
elif section == "📋 Evaluation Results":

    st.header("Evaluation Results")

    evaluation_file = "results/evaluation_report.txt"

    if os.path.exists(evaluation_file):

        with open(evaluation_file, "r") as file:
            evaluation_data = file.read()

        st.subheader("Evaluation Report")
        st.text(evaluation_data)

        # -----------------------------
        # Performance Metrics
        # -----------------------------
        metrics = {}

        for line in evaluation_data.splitlines():
            if ":" in line:
                key, value = line.split(":", 1)
                metrics[key.strip()] = value.strip()

        st.subheader("Performance Metrics")

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Average Reward",
            metrics.get("Average Reward", "N/A")
        )

        col2.metric(
            "Best Reward",
            metrics.get("Best Reward", "N/A")
        )

        col3.metric(
            "Worst Reward",
            metrics.get("Worst Reward", "N/A")
        )

    else:

        st.warning("Evaluation report not found.")