def sum(n):
    if(n==0): #base case
        return 0
    else: #recursive case
        return n+sum(n-1)
num=int(input("Enter a number: "))
print("Sum of first",num,"natural numbers is:",sum(num))