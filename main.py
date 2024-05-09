file_name = "poem.txt"
with open(file_name, "r", encoding="utf8") as file_poem:
    content = file_poem.read()
    print(content)
print("Проерка")