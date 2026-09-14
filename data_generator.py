import pandas as pd
import numpy as np

np.random.seed(42)

rows = []

n_samples = 10000

for _ in range(n_samples):

    # Choose machine condition
    state = np.random.choice(
        [0, 1, 2],
        p=[0.70, 0.20, 0.10]
    )

    if state == 0:
        temp = np.random.uniform(40, 65)
        vibration = np.random.uniform(1, 5)
        current = np.random.uniform(5, 12)
        rpm = np.random.uniform(1350, 1500)

    elif state == 1:

        temp = np.random.uniform(55, 85)
        vibration = np.random.uniform(3, 9)
        current = np.random.uniform(8, 16)
        rpm = np.random.uniform(1280, 1450)

    else:

        temp = np.random.uniform(75, 110)
        vibration = np.random.uniform(8, 15)
        current = np.random.uniform(15, 25)
        rpm = np.random.uniform(1100, 1320)

    rows.append([
        round(temp, 2),
        round(vibration, 2),
        round(current, 2),
        round(rpm, 2),
        state
    ])

df = pd.DataFrame(
    rows,
    columns=[
        "Temperature",
        "Vibration",
        "Current",
        "RPM",
        "Fault"
    ]
)

df = df.sample(
    frac=1,
    random_state=42
).reset_index(drop=True)

df.to_csv(
    "industrial_fault_dataset.csv",
    index=False
)

print("Dataset generated successfully.\n")

print("Shape:")
print(df.shape)

print("\nFault Distribution:")
print(df["Fault"].value_counts().sort_index())

print("\nLabels:")
print("0 = Good")
print("1 = Warning")
print("2 = Critical")
print(df.groupby("Fault").mean())