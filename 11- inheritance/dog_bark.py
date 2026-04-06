class Animals:
    pass
     

class pets(Animals):
    pass
 

class dog(pets):
    @staticmethod
    def bark():    
        print("DOg bark by making bhooo-bhooo sound")

a=dog()
a.bark()                        