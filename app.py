# app.py
import streamlit as st
import joblib
import numpy as np
import pandas as pd
import plotly.express as px

# Load model & encoders
model = joblib.load("risk_model.pkl")
le_goal = joblib.load("goal_encoder.pkl")
le_risk = joblib.load("risk_encoder.pkl")
le_knowledge = joblib.load("knowledge_encoder.pkl")
le_category = joblib.load("category_encoder.pkl")

st.set_page_config(page_title="Investment Risk Profiler", layout="centered")
st.title("📊 Investment Risk Profiler")
st.markdown(
    "Get your **risk category** and a **visual investment strategy** instantly."
)


# Define asset allocation mapping
def get_dynamic_allocation(age, income, risk_appetite, knowledge):
    # Normalize scores: 0 to 1
    age_score = 1 - ((age - 18) / (65 - 18))  # Younger = riskier
    income_score = min(income / 2000000, 1)  # Higher income = more risk capacity

    # Risk appetite score
    risk_map = {"Low": 0.2, "Medium": 0.5, "High": 0.8}
    risk_score = risk_map.get(risk_appetite, 0.5)

    # Knowledge score
    knowledge_map = {"Beginner": 0.2, "Intermediate": 0.5, "Expert": 0.8}
    knowledge_score = knowledge_map.get(knowledge, 0.5)

    # Total risk profile score (0 to 1)
    total_score = (age_score + income_score + risk_score + knowledge_score) / 4

    # Asset allocation logic
    stocks = round(30 + (total_score * 40), 2)  # 30% to 70%
    crypto = round(total_score * 20, 2)  # 0% to 20%
    bonds = round(50 - (total_score * 30), 2)  # 50% to 20%
    gold = round(15 - (total_score * 10), 2)  # 15% to 5%
    others = round(100 - (stocks + crypto + bonds + gold), 2)  # Remainder

    # Fix rounding errors
    total = stocks + crypto + bonds + gold + others
    if total != 100:
        others += 100 - total

    return {
        "Stocks": stocks,
        "Crypto": crypto,
        "Bonds": bonds,
        "Gold": gold,
        "Others": others,
    }


# Define risk score for progress bar
risk_score = {"Conservative": 30, "Moderate": 60, "Aggressive": 90}

# Input Form
with st.form("risk_form"):
    age = st.slider("📅 Age", 18, 65, 30)
    income = st.number_input("💰 Annual Income (INR)", min_value=100000, step=50000)
    goal = st.selectbox("🎯 Investment Goal", le_goal.classes_)
    risk_appetite = st.selectbox("⚠️ Risk Appetite", le_risk.classes_)
    knowledge = st.selectbox("📚 Financial Knowledge", le_knowledge.classes_)

    submitted = st.form_submit_button("Predict My Risk Profile")

# Main output (triggered on submit)
if submitted:
    # Prepare input for model
    input_data = np.array(
        [
            age,
            income,
            le_goal.transform([goal])[0],
            le_risk.transform([risk_appetite])[0],
            le_knowledge.transform([knowledge])[0],
        ]
    ).reshape(1, -1)

    prediction = model.predict(input_data)
    risk_label = le_category.inverse_transform(prediction)[0]

    st.success(f"🧠 You are categorized as a **{risk_label}** investor.")

    # Get allocation
    allocation = get_dynamic_allocation(age, income, risk_appetite, knowledge)
    alloc_df = pd.DataFrame(
        {"Asset Type": list(allocation.keys()), "Percentage": list(allocation.values())}
    )

    # 📊 Bar Chart
    st.subheader("💼 Recommended Investment Allocation")
    fig_bar = px.bar(
        alloc_df,
        x="Asset Type",
        y="Percentage",
        color="Asset Type",
        title=f"{risk_label} Investor Allocation",
        text="Percentage",
        labels={"Percentage": "% Allocation"},
    )
    fig_bar.update_traces(texttemplate="%{text}%", textposition="outside")
    fig_bar.update_layout(yaxis_range=[0, 100])
    st.plotly_chart(fig_bar, use_container_width=True)

    # 📈 Pie Chart
    st.subheader("📌 Allocation Breakdown")
    fig_pie = px.pie(
        alloc_df,
        names="Asset Type",
        values="Percentage",
        hole=0.4,
        title="Portfolio Composition",
    )
    st.plotly_chart(fig_pie, use_container_width=True)

    # 📍 Risk Progress Indicator
    st.subheader("📍 Risk Indicator")
    st.progress(risk_score[risk_label] / 100)

    # 📝 Summary
    st.markdown(
        f"""
    ### 🧾 Your Input Summary
    - **Age**: {age}
    - **Annual Income**: ₹{income:,}
    - **Investment Goal**: {goal}
    - **Risk Appetite**: {risk_appetite}
    - **Financial Knowledge**: {knowledge}
    """
    )
