list = []
list.append(int(input("Enter first number: ")))
list.append(int(input("Enter second number: ")))
list.append(int(input("Enter third number: ")))
list.append(int(input("Enter fourth number: ")))
list.append(int(input("Enter fifth number: ")))
sum1 = list[0] + list[1] + list[2] + list[3] + list[4]
print("The sum of the numbers is:", sum1)
print("the sum using sum() function is:", sum(list))