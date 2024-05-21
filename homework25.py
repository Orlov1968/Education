my_list = [1, 2, 5, 7, 12, 11, 35, 4, 89, 10]


def odd_numbers(x):
    return x % 2


def exponentiation_two(x):
    return x ** 2


result = map(exponentiation_two, filter(odd_numbers, my_list))
print(list(result))
