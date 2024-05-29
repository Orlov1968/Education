def all_variants(string):
    length = len(string)
    for x in range(length):
        for y in range(x + 1, length + 1):
            yield string[x:y]


a = all_variants("abc")
for letter in a:
    print(letter)
