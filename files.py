with open("blank.txt", encoding = "utf-8") as file:
    text = file.read()
    print(text)


with open("blank.txt", encoding = "utf-8") as file:
    for line in file:
        print(f"Строчка: {line}")

#with open("blank.txt", "w" , encoding = "utf-8") as file:
    #file.write("Так")

with open("blank.txt", "a", encoding = "utf-8") as file:
    file.write(" \n Уманы умана мы танцуем до утра")