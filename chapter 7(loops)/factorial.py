n=int(input("Enter a number:"))
fact=1
for i in  range(n):
    fact=fact+fact*i;
print("The factorial of ",n," is ",fact)

i=1
fact=1
while(i<=n):
    fact=fact*i
    i=i+1
print(f'''The factorial of {n} is {fact}''')   