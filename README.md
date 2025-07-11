📊 Investment Risk Profiler (Streamlit App)
An intelligent web app that helps new and existing investors discover their personalized investment risk category and get dynamic portfolio allocation based on real-world financial behavior.

🔍 “Not every investor is the same. This app adapts to you.”

🚀 Demo
📍 Hosted Demo: [Add your Streamlit Cloud/Railway link]
🎥 Preview GIF: (optional)

🧠 How It Works
The app takes in 5 inputs:

Age

Annual Income

Investment Goal

Risk Appetite

Financial Knowledge

It uses a trained Decision Tree Classifier to:

Categorize you as a Conservative, Moderate, or Aggressive investor.

Then, based on a dynamic scoring system, it generates a personalized portfolio allocation across:

🟦 Stocks

🟨 Bonds

🟧 Gold

🟥 Crypto

🟩 Others

📈 Features
✅ Dynamic charts (bar & pie)
✅ Real-time ML-based predictions
✅ Personalized investment allocations
✅ Clean, interactive Streamlit UI
✅ Easy to deploy or extend

🛠 Tech Stack
🐍 Python

🎯 scikit-learn (Decision Tree)

📊 pandas, numpy

📈 Plotly (charts)

🌐 Streamlit (UI)

📦 joblib (model serialization)

📂 Project Structure
bash
Copy
Edit
├── app.py                      # Main Streamlit app
├── train_model.py              # Train & save model
├── generate_data.py            # Synthetic dataset generator
├── risk_model.pkl              # Trained ML model
├── *_encoder.pkl               # Label encoders
├── investment_risk_profile_dataset.csv
└── README.md
🧪 Sample Input
json
Copy
Edit
{
  "Age": 30,
  "Income": 900000,
  "Risk Appetite": "Medium",
  "Knowledge": "Intermediate",
  "Goal": "Wealth Growth"
}
📤 Sample Output
🧠 You are a Moderate investor
💼 Recommended Allocation:

52% Stocks

25% Bonds

10% Crypto

8% Gold

5% Others

💡 Future Improvements
🔐 User login & history tracking

🧾 PDF portfolio reports

🌍 Real-time market-based adjustments

🧠 Use XGBoost or deep learning models

📚 License
This project is under the MIT License – free to use, modify, and share!

💼 Author
Jemil Desai
Data Analyst | ML Enthusiast | 📍 India
🔗 LinkedIn
🔗 Portfolio (optional)
