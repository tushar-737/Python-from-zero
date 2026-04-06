
class Employeer:
    def __init__(self):
       print("Employeer constructor")
    a=1
class Programmer(Employeer):
    def __init__(self):
       print("Programmer constructor")
    b=2
class Manager(Programmer):
    def __init__(self):
       super().__init__()
       print("Manager constructor")
    c=3        

cc=Manager()
print(cc.a)    