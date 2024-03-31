def test(a, *args, **kwargs):
    print(a)
    print(args)
    print(kwargs)
    print(a, args, kwargs)


test(2, "helloy", 24, name="Boris", adress="Moscow")

def factorial(n):
    if n == 1:
        return 1
    number_n_min_1 = factorial(n=n -1)
    return number_n_min_1 * n

print("________________")
print(factorial(5))