class student:
    name="Tushar"
    age=21
    
    def get_info(self): #method definition
        return f"Name: {self.name}, Age: {self.age}"
    @staticmethod 
    def greet(): 
        return "Hello, welcome to the student portal!"
tushar=student()
print(tushar.name)
print(tushar.age)
print(tushar.get_info()) #calling method using object
print(tushar.greet())