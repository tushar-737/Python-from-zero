a=int(input("Enter a number="))
b=int(input("Enter another number="))
c=int(input("Enter one more number="))
d=int(input("Enter the last number="))
if((a>b)and(a>c)and(a>d)):
    print("Greatest number is=",a)
elif((b>a)and(b>c)and(b>d)):
    print("Greatest number is=",b)
elif((c>a)and(c>b)and(c>d)):
    print("Greatest number is=",c)
else:
    print("Greatest number is=",d)