with open("text_file_with_donkey.txt", "r") as f:
    text = f.read()
    if "donkey" in text.lower():
        text = text.replace("donkey", "#######")
with open("text_file_with_donkey.txt", "w") as f:
    f.write(text)        