with open("poem.txt","r") as f:
    text=f.read()
    print(text)
if "twinkle" in text.lower():
    print("The word 'twinkle' is present in the poem.")
else:
    print("The word 'twinkle' is not present in the poem.")