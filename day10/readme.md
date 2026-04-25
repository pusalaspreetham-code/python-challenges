# Academic Data Drift & Copy Behavior Analyzer

## Overview

This project studies how student data changes when copied and modified.
It also checks how shallow and deep copy behave.

## Key Idea

* **Shallow copy:** shares inner data → affects original
* **Deep copy:** fully separate → no effect on original

## Personalization

Roll number is used to select records:

```python
if index % 3 == roll_number % 3
```

## Output

* DataFrames of original, shallow, deep
* Drift value (mean difference)
* Tuple (mean, drift, std)
* Final status (Stable / Drift / Copy Failure)

## Conclusion

Shallow copy can cause unwanted data changes, while deep copy keeps data safe.
