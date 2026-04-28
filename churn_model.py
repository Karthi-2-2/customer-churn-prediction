# 1) Imports and load data
import pandas as pd, numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout

df = pd.read_csv("/content/WA_Fn-UseC_-Telco-Customer-Churn.csv")
df.drop(["customerID"], axis=1, inplace=True)

# 2) Preprocess: encode categorical columns
cat_cols = df.select_dtypes(include=['object']).columns.tolist()
for c in cat_cols:
    df[c] = LabelEncoder().fit_transform(df[c].astype(str))

X = df.drop("Churn", axis=1)
y = df["Churn"].astype(int)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 3) Build model
model = Sequential([
    Dense(128, activation='relu', input_shape=(X_train.shape[1],)),
    Dropout(0.3),
    Dense(64, activation='relu'),
    Dropout(0.2),
    Dense(1, activation='sigmoid')
])
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# 4) Train
history = model.fit(X_train, y_train, epochs=20, batch_size=32, validation_split=0.1)

# 5) Evaluate
loss, acc = model.evaluate(X_test, y_test)
print('Test accuracy:', acc)

# 6) Save model (optional)
model.save('churn_model.h5')
