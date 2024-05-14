def add_everything_up(a, b):
    try:
        return a + b


    except TypeError:
        if isinstance(b, str) or (a, str):
            print(f"{a}{b}")


print(add_everything_up(123.456, "строка"))
print(add_everything_up("яблоко", 4215))
print(f"{add_everything_up(123.456, 7):3.3f}")

