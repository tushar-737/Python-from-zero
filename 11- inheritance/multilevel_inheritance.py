class grandfather:
    work="Goldsmith"
    def company(self):
        print(f"My business is {self.work}")

class father(grandfather): #father class has inherited property of grandfather
    workk="Blacksmith"
    def job(self):
        
        print(f"My business is {self.workk}")

class son(father): #son class has inherited property of father  MULTILEVEL INHERITANCE
    workkk="IT Company"
    def workkkk(self):
        
        print(f"My business is {self.workkk}")
 
a=grandfather()
b=father()
c=son()
c.job()
c.company()
c.workkkk()

