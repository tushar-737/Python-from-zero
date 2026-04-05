def greet(name,ending="thanks"): # Set default value for ending
    gr="Hello "+name +", "+ending
    return gr
a=greet("Tushar","! How are you?")
print(a)
b=greet("Alice")
print(b)