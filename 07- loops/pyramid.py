


n=int(input("Enter the number of rows: ")) #using for loop
for i in range(1,n+1):
    print(" "* (n-i),end="")
    print("*"* (2*i-1),end="")
    print()

n = int(input("Enter the number of rows: "))  # another method using nested for loop
for i in range(1, n+1):
    for j in range(n-i):
        print(" ", end="")
    for k in range(2*i-1):
        print("*", end="")
    print()
