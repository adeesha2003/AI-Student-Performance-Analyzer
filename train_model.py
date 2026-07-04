import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree
from sklearn.metrics import confusion_matrix

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

importance = model.feature_importances_

print("\nFeature Importance")
print("=" * 40)

for feature, score in zip(X.columns, importance):
    print(f"{feature}: {score:.4f}")

plt.figure(figsize=(12, 8))
plot_tree(
    model,
    feature_names=X.columns,
    class_names=model.classes_,
    filled=True,
)
plt.show()

predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print("Actual:")
print(y_test)

print("\nPredicted:")
print(predictions)

print(f"\nAccuracy: {accuracy * 100:.2f}%")

cm = confusion_matrix(y_test, predictions, labels=["Fail", "Pass"])

print("\nConfusion Matrix:")
print("=" * 40)
print(cm)
print("Labels: [Fail, Pass]")

print("Training Data:", len(X_train))
print("Testing Data:", len(X_test))

print("="*40)
print("New Student Prediction")
print("="*40)

attendance = int(input("Enter your attendance (%): "))
assignment = int(input("Enter your assignment marks: "))
quiz = int(input("Enter quiz marks: "))

new_student = pd.DataFrame({
    "Attendance": [attendance],
    "Assignment": [assignment],
    "Quiz": [quiz]
})

prediction = model.predict(new_student)

print("\nPrediction:", prediction[0])

probabilities = model.predict_proba(new_student)
print(f"Confidence: {probabilities.max() * 100:.2f}%")