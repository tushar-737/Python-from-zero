class employee: #parent class
    company= "itc"
    def show(self,name,salary):
        self.name=name
        self.salary=salary
        print(f"The name of the employer is: {self.name}. His salary is {self.salary}")

class programmer(employee): #inherited class
    company="itc infosysis"
    def showlanguage(self):
        print(f"The name of the employeer is: {self.name}. His salary is {self.salary}")

a=employee()
b=programmer()
print(a.company,b.company) 
a.show("Tushar",56555)
b.show("tushar",677666) #child class uses parent class method
