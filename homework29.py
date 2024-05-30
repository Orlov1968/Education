import math


def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        if result < 1:
            raise Exception("Значение должно быть натуральным числом")
        if result == 2:
            print("Простое")
            return
        elif result % 2 == 0:
            print("Составное")
            return
        for i in range(3, math.ceil(result ** 0.5), 2):
            if result % i == 0:
                print("Составное")
        else:
            print("Простое")
    return wrapper


@is_prime
def sum_three(num_1, num_2, num_3):
    result = num_1 + num_2 + num_3
    return result


sum_three(0, 8, 2)
