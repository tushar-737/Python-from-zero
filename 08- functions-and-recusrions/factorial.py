def fact(n):
    if n==0 or n==1: #base case
        return 1
    else: #recursive case
        return n*fact(n-1)
n=int(input("Enter a number to find its factorial: "))
print(fact(n))    