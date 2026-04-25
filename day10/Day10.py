import random
import copy
import math
import numpy as np
import pandas as pd

def generate_students():
    n=12
    data = []
    for i in range(n):
        student = {
            "id": i + 1,
            "marks": random.randint(40, 100),
            "attendance": random.randint(60, 100),
            "scores": [random.randint(10, 30), random.randint(10, 30)]
        }
        data.append(student)
    return data


def mutate_data(data, roll):
    rule = roll % 3

    for i in range(len(data)):
        if i % 3 == rule:
            m = data[i]["marks"]
            data[i]["marks"] = int(m + m/5)

            data[i]["scores"][0] += 5

            data[i]["attendance"] -= 3


def analyze_stats(data):
    marks = [d["marks"] for d in data]

    mean = np.mean(marks)
    median = np.median(marks)
    std = np.std(marks)

    # manual mean (without numpy)
    manual_mean = sum(marks) / len(marks)

    return mean, median, std, manual_mean


def detect_drift(original, modified):
    orig_mean = np.mean([d["marks"] for d in original])
    mod_mean = np.mean([d["marks"] for d in modified])

    drift = abs(orig_mean - mod_mean)
    return drift


def classify(drift, threshold, original, shallow):
    if original != shallow:
        return "Copy Failure Detected"
    elif drift < threshold:
        return "Stable Data"
    elif drift < threshold * 2:
        return "Minor Drift"
    else:
        return "Critical Drift"



roll_number = 601
original = generate_students()
shallow_copy = copy.copy(original)
deep_copy = copy.deepcopy(original)
mutate_data(shallow_copy, roll_number)
mutate_data(deep_copy, roll_number)
# convert to DataFrame
df_original = pd.DataFrame(original)
df_shallow = pd.DataFrame(shallow_copy)
df_deep = pd.DataFrame(deep_copy)

# analysis
mean, median, std, manual_mean = analyze_stats(original)
drift = detect_drift(original, deep_copy)
threshold = 5   # custom threshold
result = classify(drift, threshold, original, shallow_copy)


print("\nOriginal DataFrame:\n", df_original)
print("\nShallow Copy DataFrame:\n", df_shallow)
print("\nDeep Copy DataFrame:\n", df_deep)
print("\nDrift Value:", drift)
print("\nTuple Output (mean, drift, std_dev):")
print((mean, drift, std))
print("\nManual Mean (without numpy):", manual_mean)
print("\nFinal Classification:", result)
