file_name = "poem.txt"
file = open(file_name, "r")
content_poem = file.read()
file.close()
print(content_poem)