try :
    a=int(input("Enter a number:-")) 
    print(a)
except ValueError as c:
    print("heyy",c)
except Exception as e:
    print(e)
print("Thank you")    
