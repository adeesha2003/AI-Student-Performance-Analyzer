# AI Student Performance Analyzer

## Project Overview

This project is a Machine Learning application developed using Python. It collects student performance data, analyzes it, and predicts whether a student will pass or fail using a Decision Tree Machine Learning model.

---

## Features

- Collect student information
- Store data in a CSV file
- Analyze student performance
- Train a Decision Tree model
- Predict Pass/Fail
- Display prediction confidence
- Show feature importance
- Visualize the Decision Tree
- Evaluate the model using Accuracy and Confusion Matrix

---

## Technologies Used

- Python
- Pandas
- Scikit-learn
- Matplotlib

---

## Project Structure

AI-Student-Performance-Analyzer/

├── main.py

├── analyze_data.py

├── train_model.py

├── students.csv

├── requirements.txt

└── README.md

---

##  How to Run

1. Install the required libraries

```
pip install -r requirements.txt
```

2. Run the data collection program

```
python main.py
```

3. Analyze the dataset

```
python analyze_data.py
```

4. Train the Machine Learning model

```
python train_model.py
```

---

## Machine Learning Model

Algorithm:

- Decision Tree Classifier

Features:

- Attendance
- Assignment Marks
- Quiz Marks

Target:

- Student Status (Pass / Fail)

---

## Future Improvements

- Increase dataset size
- Compare multiple ML algorithms
- Build a web application using Streamlit
- Improve prediction accuracy

---