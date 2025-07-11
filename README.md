# Investment Risk Profiler 📊

An intelligent and personalized web app to help individuals assess their investment risk category and get a tailored asset allocation strategy.

> 🔍 “Not every investor is the same. This app adapts to **you**.”

---


## 🧠 How It Works

You input:

* Age
* Annual Income
* Investment Goal
* Risk Appetite
* Financial Knowledge

The app:

1. Uses a trained **Decision Tree Classifier** to predict your **Risk Category**:

   * Conservative
   * Moderate
   * Aggressive
2. Applies a dynamic scoring logic to personalize your investment allocation:

   * 🔙 Stocks
   * 🔙 Bonds
   * 🔙 Crypto
   * 🔙 Gold
   * 🔙 Others

---

## 📊 Features

* ✅ Real-time ML-based risk profiling
* ✅ Personalized portfolio allocation
* ✅ Interactive charts: Bar + Pie
* ✅ Progress bar showing risk level
* ✅ Responsive and simple Streamlit UI

---

## 🛠️ Tech Stack

* Python
* scikit-learn
* pandas, numpy
* Plotly (charts)
* Streamlit (UI)
* joblib (model saving/loading)

---


## 💪 Sample Prediction

**Input:**

```json
{
  "Age": 30,
  "Income": 900000,
  "Risk Appetite": "Medium",
  "Knowledge": "Intermediate",
  "Goal": "Wealth Growth"
}
```

**Output:**

* Risk Category: **Moderate**
* Portfolio:

  * 52% Stocks
  * 25% Bonds
  * 10% Crypto
  * 8% Gold
  * 5% Others

---

## 🧪 Future Enhancements

* 🔐 User authentication and history
* 📄 Exportable PDF reports
* 🌍 Real-time market integration
* 🧠 Deep learning models for profiling

---

## 📄 License

Licensed under the **MIT License** — use, modify, and share freely.

---

## 💼 Author

**Jemil Desai**
Aspiring Data Scientist | ML Enthusiast | India
[LinkedIn](https://www.linkedin.com/in/jemil-desai/)

