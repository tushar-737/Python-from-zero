dict={
    "name":"Tushar",
    "age":21,
    "city":"Delhi"
}
print(dict.items())
print(dict.keys())
print(dict.values())
print(dict.get("name"))
dict.update({"age":22}) # updating existing key-value pair
print(dict)
dict.update({"country":"India"}) # adding new key-value pair
print(dict)
print(len(dict))
print(type(dict))