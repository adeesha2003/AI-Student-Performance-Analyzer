import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

data = pd.read_csv("students.csv")

print(data.head())

X = data[["Attendance", "Assignment", "Quiz"]]
y = data["Status"]

print(X.head())
print(y.head())

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)
predictions = model.predict(X_test)

print("Actual:")
print(y_test)

print("\nPredicted:")
print(predictions)

print("Training Data:", len(X_train))
print("Testing Data:", len(X_test))