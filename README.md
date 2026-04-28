# customer-churn-prediction
Customer churn prediction using Deep Learning (TensorFlow) with preprocessing and model evaluation
📌 Overview
This project predicts customer churn using a Deep Learning model built with TensorFlow/Keras.
It helps businesses identify customers likely to leave and take proactive retention actions.
🎯 Objective
Predict customer churn (Yes/No)
Identify key factors affecting churn
Improve customer retention strategies
📂 Dataset
Telco Customer Churn Dataset
~7,000 customer records
Target variable: Churn (0 = No, 1 = Yes)
🛠️ Technologies Used
Python
Pandas, NumPy
Scikit-learn
TensorFlow / Keras
⚙️ Workflow
Data Cleaning
Encoding categorical variables
Feature scaling
Train-test split
Neural Network model building
Model evaluation
🧠 Model Architecture
Dense (128, ReLU)
Dropout (0.3)
Dense (64, ReLU)
Dropout (0.2)
Output (Sigmoid)
📊 Model Performance
Training Accuracy: ~81%
Validation Accuracy: ~81%
Test Accuracy: 80.19%
🔍 Key Insights
Customers with short tenure are more likely to churn
Higher monthly charges increase churn probability
Contract type plays a major role in retention
▶️ How to Run
pip install -r requirements.txt
python churn_model.py
📁 Project Structure
customer-churn-prediction/
│── data/
│── churn_model.py
│── requirements.txt
│── README.md
🚀 Future Improvements
Hyperparameter tuning
Improve model performance
Deploy using Streamlit
🙌 Author
Karthikeyan
