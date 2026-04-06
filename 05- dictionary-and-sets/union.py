set1={1,2,3,2,1}
set2={3,4,5,4,3}
set3=set1 | set2 # union operator
print(set3)
print(set1.union(set2)) # union method
set4= {1,2,7}
set5=set1 | set2 | set4
print(set5)
set6=set1.union(set2).union(set4)
print(set6)