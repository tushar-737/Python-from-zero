def table(n):
    for i in range(1,11):
        print(f'''{i}x{n}={i*n}''')
num=int(input("Enter a number to print its table: "))
table(num)