import random
import pandas as pd
import numpy as np
import math

# generate student data
def generate_data(n):
    data = []
    for i in range(1, n + 1):
        marks = random.randint(0, 100)
        attendance = random.randint(0, 100)
        assignment = random.randint(0, 50)
        data.append((i, marks, attendance, assignment))
    return data

# classify students
def classify_students(data):
    result = {"At Risk": [], "Average": [], "Good": [], "Top Performer": []}
    for i in range(len(data)):
        sid, marks, att, assign = data[i]
        if marks < 40 or att < 50:
            result["At Risk"].append(sid)
        elif marks <= 70:
            result["Average"].append(sid)
        elif marks <= 90:
            result["Good"].append(sid)
        elif marks > 90 and att > 80:
            result["Top Performer"].append(sid)
    return result

# analyze data
def analyze_data(dataframe):
    marks_arr = dataframe["marks"].values
    mean_calc = np.mean(marks_arr) #using NumPy
    median_calc = np.median(marks_arr)
    std_calc = np.std(marks_arr)
    # normalization
    min_val = min(marks_arr)
    max_val = max(marks_arr)
    normalized = []
    for i in range(len(marks_arr)):
        if max_val != min_val:
            normalized.append((marks_arr[i] - min_val) / (max_val - min_val))
        else:
            normalized.append(0)
    dataframe["normalized_marks"] = normalized
    # performance index
    perf = []
    for i in range(len(df)):
        m = dataframe["marks"][i]
        a = dataframe["assignment"][i]
        att = dataframe["attendance"][i]
        perf.append((m * 0.6 + a * 0.4) * math.log(att + 1))
    dataframe["performance_index"] = perf
    return mean_calc, median_calc, std_calc


num_students = 10  # based on last digit of register number=1
records = generate_data(num_students) #genrating data by randomly 
df = pd.DataFrame(records, columns=["id", "marks", "attendance", "assignment"]) #genrating data frame using pandas
categories = classify_students(records) # classifying data
mean_val, median_val, std_val = analyze_data(df) #caluclating mean,median,standard deviation 
# pattern detection
consistency = std_val < 15
attendance_issue = sum(df["attendance"] < 50) > 3
top_perf = len(categories["Top Performer"]) >= 2
# final result
if consistency and not attendance_issue and top_perf:
    insight = "Stable Academic System"
elif attendance_issue:
    insight = "Critical Attention Required"
else:
    insight = "Moderate Performance"

# output
print(df)
print("Categories:", categories)
print("Statistical Summary:")
print("Mean Marks:", round(mean_val, 2))
print("Median Marks:", round(median_val, 2))
print("Standard Deviation:", round(std_val, 2))
print("Final Insight:", insight)
