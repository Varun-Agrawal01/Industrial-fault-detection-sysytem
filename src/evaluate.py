from sklearn.metrics import classification_report, confusion_matrix
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split

df= pd.read_csv("C:\\Users\\varun\\Desktop\\Proj\\Scada\\Dataset\\industrial_fault_dataset.csv")
x = df[["Temperature", "Vibration", "Current", "RPM"]]
y = df["Fault"]
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.4, random_state=48)

with open("C:\\Users\\varun\\Desktop\\Proj\\Scada\\Model\\rf_model.pkl", "rb") as f:
    rf_classifier = pickle.load(f)
    y_pred = rf_classifier.predict(x_test)

report = classification_report(y_test, y_pred)
print("Classification Report:")
print(report)