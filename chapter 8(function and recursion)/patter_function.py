def pattern(n):
    if(n==0): #base case
        return 
    else:
        print('* '*n) #print current row
        pattern(n-1) #recursive call for next row
n=int(input("Enter number of rows: "))
pattern(n)        