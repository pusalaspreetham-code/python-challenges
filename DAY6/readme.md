# Digital Payment Risk Detection

## Problem Description
This program analyzes a list of daily transaction amounts and detects suspicious spending patterns.  
Each transaction is classified into categories and the overall risk level is calculated based on given rules.

---

## Logic / Approach Used
Firstly, I took the transaction values as input and saved them in a list.and later on i classified by for loops and conditional statements.
I used list comprehension to get only valid transactions and calculated the total amount and count.
Then I checked conditions like many transactions, high total amount, and high-risk transactions.I used my own personalization method to decide the final risk level.Finally, I stored the result in a tuple and printed the report.

---

## Personalization Applied
I used my own personalisation logic to decide the risk level instead of directly assigning it.
Each suspicious condition adds points, and the total score determines whether the result is Low, Moderate, or High Risk.

---

## Test Case 1
Input:
6
100,2500,500,300,-8,455
Output:
Low Risk  
Total = 3855
Count = 6

---

## Test Case 2
Input:
2
100,4500
Output:
Low Risk  
Total = 4600  
Count = 2

---

## Test Case 3
Input:
4
100,4258,75,-8
Output:
Low Risk
Total = 16550  
Count = 7  

## How to run the code
1. Install Python on your system.
2. Save the program as risk_detection.py.
3. Open terminal or command prompt.
4. Go to the folder where the file is saved.
5. Run the command:python risk_detection.py
6. Enter the transaction values when asked.
7. The program will display the categorized transactions and risk level.
