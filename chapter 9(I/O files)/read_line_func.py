f=open("text2.txt")
#line=f.readlines()   #reads all lines and stores in a list
#print(line,type(line))
line=f.readline()  #reads only one line at a time
print(line,type(line))
line=f.readline()
print(line,type(line))
line=f.readline()
print(line,type(line))
f.close()