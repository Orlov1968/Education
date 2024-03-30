def print_params(a: int = 1, b: str = 'строка', c: bool = True):
    print(a, b, c)



print_params()
print_params(b = 25)
print_params(c = [1, 2, 3])

values_list = [9, "string", 3.14]
values_dict = {"a": "helloy ", "b": 7, "c": False}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [True, "Bank"]
print_params(*values_list_2, 42) # Работает