class Employee:
    @property
    def name(self):
        return f"{self.fname},{self.lname}"
    
    @name.setter
    def name(self,value):
        self.fname=value.split(" ")[0]
        self.lname=value.split(" ")[1]

a=Employee()
a.name="Tushar Gupta"
print(a.fname)
print(a.lname)
print(a.fname,a.lname)
