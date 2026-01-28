name=input("enter your name")
email=input("enter your email")
mobile=input("enter your mobile number")
age=int(input("enter your age"))
valid=0

if name.count(" ")>=1 and name[0]!=" " and name[len(name)-1]!=" ":
    valid+=1

if email.count("@")==1 and email.count(".")>=1 and email[0]!="@":
    valid+=1

if len(mobile)==10 and mobile.isdigit() and mobile[0]!="0":
    valid+=1

if age>=18 and age<=60:
    valid+=1

if(valid==4):
    print("User Profile is VALID")

else:
    print("User Profile is INVALID")
