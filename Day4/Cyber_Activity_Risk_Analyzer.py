d=1
print("Register Digit(D):",d)
n=int(input("enter the number of elements"))
scores=[0]*n
for i in range(n):
    scores[i]=int(input("enter the scores"))

a = b = c = e = 0
for i in range(n):
    if 0<=scores[i]<=30:
        a += 1
    elif 31<=scores[i]<=60:
        b += 1
    elif 61<=scores[i]<=100:
        c += 1
    elif scores[i] > 100:
        e += 1
low_scores=[0]*a
medium_risk=[0]*b
high_scores=[0]*c
critical_risk=[0]*e
a=b=c=e=0
valid_scores_count=0
invalid_scores_count=0
for i in range(n):
    if scores[i]<0:
        invalid_scores_count+=1
    else:
        valid_scores_count+=1
        if scores[i] <= 30:
            low_scores[a]=scores[i]
            a=a+1
        elif scores[i] <= 60:
            medium_risk[b]=scores[i]
            b=b+1
        elif scores[i] <= 100:
            high_scores[c] = scores[i]
            c=c+1
        else:
            critical_risk[e]=scores[i]
            e=e+1

print("Low Risk:",low_scores)
print("Medium Risk:",medium_risk)
print("High Risk:",high_scores)
print("Critical Risk:",critical_risk)
removed_count=0

if d%2==0:
    removed_count=len(low_scores)
    low_scores=[]
else:
    removed_count=len(critical_risk)
    critical_risk=[]

print("After Personalized Filtering:")
print("Low Risk:",low_scores)
print("Medium Risk:",medium_risk)
print("High Risk:",high_scores)
print("Critical Risk:",critical_risk)

print("Total Valid Entries:", valid_scores_count)
print("Ignored Entries:", invalid_scores_count)
print("Removed Due to Personalization:", removed_count)
