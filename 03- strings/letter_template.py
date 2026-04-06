name=input("Enter your name: ")
date=input("Enter the date: ")
Letter = ''' 
Dear  Name,
You are selected!
Date : Date'''
a=Letter.replace("Name",name).replace("Date",date)
print(a)