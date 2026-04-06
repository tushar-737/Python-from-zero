class employee:
    a=10
    def print(self):
        print(f"The value is :- {self.a}")
b=employee()
b.a=65 
print(b.a)

class class_method:
    d=10
    @classmethod
    def show(cls):
        print(f"the value is:- {cls.d}")
c=class_method()
c.d=45
c.show()      


