def add_everything_up(a, b):
    try:
        return a + b


    except TypeError:
        if isinstance(b, str) or (a, str):
            print(f"{a}{b}")


print(add_everything_up("vvv", 9.4))
