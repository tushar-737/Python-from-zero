class calculator:
    def __init__(self,n):
        self.n=n
    def square(self):
        print("The square is: ",(self.n*self.n))
    def cube(self):
        print("The cube is: ",(self.n*self.n*self.n))
    def squareroot(self):
        print("The squareroot is: ",(self.n**(1/2)))

number=calculator(36)
number.square()
number.cube()
number.squareroot()