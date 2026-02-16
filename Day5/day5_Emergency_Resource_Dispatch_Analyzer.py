name="PUSALA PREETHAM"
l=len(name)-name.count(" ")
PLI=l%3
n=int(input("Enter no of elements to enter: "))
arr=[0]*n
for i in range(n):
    arr[i]=int(input("Enter elements: "))

low_demand=[]
moderate_demand=[]
high_demand=[]
invalid_requests=[]
total_valid=0
#inserting elements into list
for i in range(n):
    if arr[i]<0:
        invalid_requests.append(arr[i])
    else:
        total_valid+=1

        if 0 < arr[i] <= 20:
            low_demand.append(arr[i])
        elif 20 < arr[i] <= 50:
            moderate_demand.append(arr[i])
        elif arr[i]>50:
            high_demand.append(arr[i])

print("Values before PLI implementation")
print("Invalid Requests:", invalid_requests)
print("Low Demand:", low_demand)
print("Moderate Demand:", moderate_demand)
print("High Demand:", high_demand)
#PLI logic
removed_count=0
if PLI==0:
    removed_count=len(low_demand)
    low_demand=[]
elif PLI==1:
    removed_count=len(high_demand)
    high_demand=[]
else:
    removed_count=len(low_demand)+len(high_demand)
    low_demand=[]
    high_demand=[]

print("length of name",l)
print("PLI Value:", PLI)

print("Final Report:")
print("Invalid Requests:", invalid_requests)
print("Low Demand:", low_demand)
print("Moderate Demand:", moderate_demand)
print("High Demand:", high_demand)

print("Total valid elements:",total_valid)
print("Removed count due to PLI logic",removed_count)
