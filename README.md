# 🚀 Customer Churn Prediction

## 📌 Overview
This project predicts customer churn using Deep Learning techniques.  
The model is built using TensorFlow/Keras and trained on a telecom dataset to classify whether a customer will churn or not.

---

## 📊 Dataset
- Dataset: Telco Customer Churn Dataset  
- Records: ~7,000 customers  
- Target Variable: `Churn` (0 = No, 1 = Yes)

---

## ⚙️ Technologies Used
- Python  
- Pandas, NumPy  
- Scikit-learn  
- TensorFlow / Keras  

---

## 🔧 Data Preprocessing
- Removed unnecessary columns (`customerID`)  
- Encoded categorical features using Label Encoding  
- Feature scaling using StandardScaler  
- Train-test split (80/20)

---

## 🤖 Model Architecture
- Input Layer  
- Dense Layer (128 neurons, ReLU)  
- Dropout (0.3)  
- Dense Layer (64 neurons, ReLU)  
- Dropout (0.2)  
- Output Layer (Sigmoid)

---

## 📈 Model Training
- Optimizer: Adam  
- Loss Function: Binary Crossentropy  
- Epochs: 20  
- Batch Size: 32  

---

## 📊 Results
- Test Accuracy: **~80%**  
- Model shows good performance in predicting customer churn.
---

## 📌 Conclusion
This project demonstrates how deep learning can be used to predict customer churn and help businesses take proactive retention strategies.

---

## 👤 Author
Karthikeyan G
