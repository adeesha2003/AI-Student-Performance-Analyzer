import pandas as pd

data = pd.read_csv("students.csv")
print(data)

print("\nAverage Marks:", data["Marks"].mean())
print("Highest Marks:", data["Marks"].max())
print("Lowest Marks:", data["Marks"].min())
print("\nTotal Students:", len(data))
print("Number of Pass Students:", len(data[data["Status"] == "Pass"]))
print("Number of Fail Students:", len(data[data["Status"] == "Fail"]))