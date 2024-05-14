file_name = "poem.txt"
with open(file_name, "r", encoding="utf8") as file_poem:
    for line in file_poem:
        print(line, end="")
