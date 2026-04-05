class student:
    name="Tushar"
    age="20"

    def __init__(self,name,age,study): #init are called first
        self.name=name
        self.age=age
        self.study=study
        print("Hello")

student1=student("Rahul",23,"B.com")
print(student1.name,student1.age,student1.study)
