registration_no=601
N=int(input("enter the number of elements:"))
marks=[0]*N
for i in range(N):
    marks[i] = int(input(f"enter the marks at index {i}:"))
total_valid=0
total_failed=0
for i in range(N):
    if registration_no % 2 != 0 and 30<=marks[i]<=90:
        marks[i] += 7
    if registration_no % 2 == 0 and 30 <= marks[i] <= 90:
        marks[i] += 5
    if marks[i] > 100 or marks[i] < 0:
        print(marks[i], "-> Invalid")
    else:
        total_valid += 1
        if 90 <= marks[i] <= 100:
            print(marks[i], "-> Excellent")
        elif marks[i] >= 75:
            print(marks[i], "-> Very Good")
        elif marks[i] >= 60:
            print(marks[i], "-> Good")
        elif marks[i] >= 40:
            print(marks[i], "-> Average")
        else:
            print(marks[i], "-> Fail")
            total_failed += 1

print("Total valid Students", total_valid)
print("Total Failed Students", total_failed)
