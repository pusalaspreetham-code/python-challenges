n=int(input("enter number of transaction"))
transactions=[]
#input of transactions
for i in range(n):
    t = int(input("enter transaction: "))
    transactions.append(t)
# Dictionary to store categorized transactions
categories = {
    "normal": [],
    "large": [],
    "high_risk": [],
    "invalid": []
}
#categorisation
for i in transactions:
    if i<=0:
        categories["invalid"].append(i)
    elif i<=500:
        categories["normal"].append(i)
    elif i<=2000:
        categories["large"].append(i)
    else:
        categories["high_risk"].append(i)

# getting only valid transactions by list comprehension method
valid=[t for t in transactions if t>0]

count=len(transactions)
total_sum=sum(valid)
high_risk_count=len(categories["high_risk"])

frequent_transactions= False
large_spending_transactions = False
suspicious_transactions = False
#Pattern Detection
if count>5:
    frequent_transactions=True
if total_sum>5000:
    large_spending_transactions=True
if high_risk_count>2:
    suspicious_transactions=True
#risk classification logic
score = 0
if frequent_transactions:
    score += 1
if large_spending_transactions:
    score += 1
if suspicious_transactions:
    score += 2

if score >= 3:
    risk = "High Risk"
elif score == 2:
    risk = "Moderate Risk"
else:
    risk = "Low Risk"

# transaction summary by using tuple
summary=(count,total_sum,risk)
#output
print("Categorized transactions")
print(categories)

print("Total transaction value:", total_sum)
print("Total number of transactions:", count)

print("Risk level:", risk)
print("Tuple Summary:", summary)
