with open("blank.txt", encoding = "utf-8") as file:
    text = file.read()
    print(text)


with open("blank.txt", encoding = "utf-8") as file:
    for line in file:
        print(f"Строчка: {line}")

with open("blank.txt", "w" , encoding = "utf-8") as file:
