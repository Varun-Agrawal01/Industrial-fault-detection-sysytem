import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

df = pd.read_csv("C:\\Users\\varun\\Desktop\\Proj\\Scada\\Dataset\\industrial_fault_dataset.csv")
x = df[["Temperature", "Vibration", "Current", "RPM"]]
y = df["Fault"]
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2, random_state=42)
rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)
rf_classifier.fit(x_train, y_train)

y_pred = rf_classifier.predict(x_test)


with open("C:\\Users\\varun\\Desktop\\Proj\\Scada\\Model\\rf_model.pkl", "wb") as f:
    pickle.dump(rf_classifier, f)