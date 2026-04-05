a=int(input("Enter 1st subject marks="))
b=int(input("Enter 2nd subject marks="))
c=int(input("Enter 3rd subject marks="))
if(a>=33)and(b>=33)and(c>=33) and ((a+b+c)/3)>=40:
    print("You have passed the exam")
else:
    print("You have failed the exam")