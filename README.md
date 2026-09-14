# Industrial Fault Detection using Machine Learning

A machine-learning-based industrial fault detection system that classifies machine operating conditions into **Good, Warning, or Critical** states using sensor parameters such as temperature, vibration, current, and RPM.

The project uses a **Random Forest Classifier** for fault classification and is designed to integrate with **LabVIEW** for real-time monitoring and visualization.

---

## Overview

Industrial machines generate multiple sensor signals during operation. Changes in parameters such as temperature, vibration, electrical current, and rotational speed can indicate abnormal operating conditions.

This project demonstrates a software-based fault detection pipeline:

```text
Sensor / Simulated Sensor Data
            ↓
Temperature, Vibration, Current, RPM
            ↓
      Machine Learning Model
            ↓
     Random Forest Classifier
            ↓
       Fault Classification
            ↓
     0 / 1 / 2
            ↓
        LabVIEW HMI
            ↓
    GOOD / WARNING / CRITICAL
```

The current implementation uses **simulated sensor data** rather than physical industrial sensors. This allows the complete ML and LabVIEW pipeline to be developed and tested without requiring additional hardware.

---

## Fault Classes

| Label | Fault State | Meaning                                           |
| ----: | ----------- | ------------------------------------------------- |
|     0 | Good        | Machine operating under normal conditions         |
|     1 | Warning     | Abnormal conditions detected; monitoring required |
|     2 | Critical    | Severe abnormal conditions detected               |

---

## Input Parameters

The Random Forest model uses four sensor parameters:

| Parameter   | Description                             |
| ----------- | --------------------------------------- |
| Temperature | Machine/component temperature           |
| Vibration   | Measured vibration level                |
| Current     | Electrical current drawn by the machine |
| RPM         | Rotational speed                        |

The model receives these four values as input and predicts the corresponding fault class.

---

## Machine Learning Model

### Random Forest Classifier

The project uses a **Random Forest Classifier** from Scikit-learn.

Random Forest is an ensemble learning algorithm that combines multiple decision trees to produce a final prediction.

For classification, each decision tree produces a class prediction and the Random Forest combines these predictions to determine the final class.

### Why Random Forest?

Random Forest was selected because it:

* Handles nonlinear relationships between features.
* Works well with numerical sensor data.
* Does not require feature scaling for this dataset.
* Can model interactions between multiple sensor parameters.
* Provides feature importance information.
* Is relatively simple to deploy for real-time inference.

---

## Dataset

The current dataset is **synthetically generated** for development and testing.

The dataset contains:

* Temperature
* Vibration
* Current
* RPM
* Fault

The generated dataset contains approximately **10,000 samples** with the following class distribution:

| Fault | Class    | Samples | Approx. Percentage |
| ----: | -------- | ------: | -----------------: |
|     0 | Good     |    6972 |             69.72% |
|     1 | Warning  |    2008 |             20.08% |
|     2 | Critical |    1020 |             10.20% |

The data generation process creates different operating ranges for each fault state.

> **Important:** This dataset is synthetic and should not be interpreted as real industrial sensor data or real-world fault statistics. The high classification performance is partly due to the relatively well-separated operating ranges used during dataset generation.

---

## Project Structure

```text
industrial-fault-detection/
│
├── data/
│   └── industrial_fault_dataset.csv
│
├── src/
│   ├── generate_dataset.py
│   ├── train_model.py
│   ├── evaluate_model.py
│   └── predict_fault.py
│
├── models/
│   └── fault_model.pkl
│
├── requirements.txt
│
└── README.md
```

### File Description

#### `generate_dataset.py`

Generates the synthetic industrial sensor dataset.

The generated dataset contains the four sensor features and their corresponding fault labels.

#### `train_model.py`

Loads the dataset, separates features and target labels, performs the train/test split, trains the Random Forest model, and saves the trained model.

#### `evaluate_model.py`

Evaluates the trained model using:

* Accuracy
* Precision
* Recall
* F1-score
* Classification report
* Confusion matrix
* Cross-validation / additional evaluation where applicable

#### `predict_fault.py`

Loads the saved Random Forest model and performs fault prediction on new sensor values.

This file is intended to become the interface between the machine-learning model and LabVIEW.

#### `fault_model.pkl`

Serialized trained Random Forest model used for inference.

---

## Model Training

The model uses:

```text
Features:
Temperature
Vibration
Current
RPM

Target:
Fault
```

The dataset is divided into training and testing data before model training.

The trained Random Forest model is then saved and reused for prediction rather than retraining every time a new sensor reading is received.

---

## Model Evaluation

The model achieved approximately **99%+ accuracy** on the generated dataset.

An additional evaluation using a different train/test split produced the following results:

```text
Classification Report:

              precision    recall  f1-score   support

0                1.00      1.00      1.00      2823
1                1.00      0.99      1.00       764
2                1.00      1.00      1.00       413

accuracy                           1.00      4000
macro avg       1.00      1.00      1.00      4000
weighted avg    1.00      1.00      1.00      4000
```

### Confusion Matrix

```text
                Predicted
              0     1     2

Actual  0   2823    0     0
        1      5   759    0
        2      0     0   413
```

The model correctly classified **3995 out of 4000 samples**, with only 5 Warning samples incorrectly classified as Good.

### Important Interpretation

The high performance should be interpreted in the context of the dataset.

The synthetic data was generated with relatively distinct operating ranges for Good, Warning, and Critical conditions. Therefore, the classes are highly separable.

This means the current results demonstrate that the ML pipeline works correctly, but they **do not represent expected real-world industrial fault detection accuracy**.

---

## LabVIEW Integration

The eventual real-time architecture is:

```text
              LABVIEW
                 │
                 │
       Simulated / Sensor Data
                 │
                 ↓
    ┌─────────────────────────┐
    │ Temperature             │
    │ Vibration               │
    │ Current                 │
    │ RPM                     │
    └─────────────────────────┘
                 │
                 ↓
           Python Node
                 │
                 ↓
       Random Forest Model
                 │
                 ↓
          Prediction
        0 / 1 / 2
                 │
                 ↓
           LabVIEW HMI
                 │
       ┌─────────┼─────────┐
       ↓         ↓         ↓
     GOOD     WARNING    CRITICAL
```

LabVIEW is responsible for the user interface, sensor simulation/data acquisition, and visualization.

Python is responsible for machine-learning inference.

This separation keeps the ML model independent from the visualization layer.

---

## Software-Only Sensor Simulation

The current project does not require physical sensors.

LabVIEW can generate simulated values for:

* Temperature
* Vibration
* Current
* RPM

These values can then be passed to the Python model.

In a future hardware implementation, the simulated values can be replaced with actual sensor measurements obtained through a suitable data-acquisition system.

---

## Technologies Used

* **Python**
* **Pandas**
* **NumPy**
* **Scikit-learn**
* **Joblib / Pickle**
* **LabVIEW**
* **Machine Learning**
* **Random Forest Classification**

---

## Installation

Clone the repository and install the required Python packages.

```bash
pip install -r requirements.txt
```

Example `requirements.txt`:

```text
numpy
pandas
scikit-learn
matplotlib
joblib
```

---

## Running the Project

### 1. Generate the dataset

Run:

```bash
python src/generate_dataset.py
```

This creates the synthetic sensor dataset.

### 2. Train the model

Run:

```bash
python src/train_model.py
```

The trained Random Forest model is saved for later inference.

### 3. Evaluate the model

Run:

```bash
python src/evaluate_model.py
```

This generates the classification metrics and confusion matrix.

### 4. Perform a prediction

Run:

```bash
python src/predict_fault.py
```

The prediction script can be used to test the model with new sensor values.

---

## Future Improvements

The current implementation is a prototype intended to demonstrate the complete machine-learning and LabVIEW integration pipeline.

Possible improvements include:

* Replace synthetic data with real industrial sensor data.
* Introduce more realistic sensor noise.
* Include overlapping operating conditions between fault classes.
* Add additional fault types.
* Perform hyperparameter optimization.
* Compare Random Forest with other ML algorithms.
* Implement real-time streaming sensor data.
* Add historical fault logging.
* Add fault trend visualization in LabVIEW.
* Add alert/notification mechanisms.
* Deploy the model for continuous monitoring.
* Explore fuzzy logic or ANFIS for more advanced fault reasoning.

---

## Limitations

The current system has several limitations:

1. The dataset is synthetically generated.
2. Sensor ranges are relatively well separated between fault classes.
3. The model has not been validated against real industrial equipment.
4. The current fault labels represent simulated operating states rather than experimentally verified physical faults.
5. Real industrial environments may contain sensor noise, missing values, drift, outliers, and overlapping fault signatures.

Therefore, the current results should be considered **proof-of-concept ML performance rather than production-level industrial reliability**.

---

## Project Goal

The primary goal of this project is to demonstrate the integration of:

```text
Machine Learning
        +
Sensor Data
        +
Python
        +
LabVIEW
        =
Industrial Fault Detection System
```

The project provides a foundation that can later be extended from simulated sensor data to real-time industrial monitoring using physical sensors and data-acquisition hardware.
