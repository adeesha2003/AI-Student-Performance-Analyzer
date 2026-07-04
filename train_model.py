import pandas as pd
from sklearn.model_selection import train_test_split

data = pd.read_csv("students.csv")

print(data.head())

X = data[["Attendance", "Assignment", "Quiz"]]
y = data["Status"]

print(X.head())
print(y.head())