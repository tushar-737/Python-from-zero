class TwoDvector:
    def __init__(self,i,j):
        self.i=i
        self.j=j
    def show(self):
        print(f"The value of 2D vector is:- {self.i},{self.j}")
class ThreeDvector(TwoDvector):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k=k
    def show(self):
        print(f"The value of 3D vector is:- {self.i},{self.j},{self.k}")    
o=TwoDvector(3,7)
o.show()
i=ThreeDvector(28,7,88)
i.show()

