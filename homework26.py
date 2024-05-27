# Фабрика функций. Сложение двух списков
from math import sqrt


def act(number):
    if number == "1":
        def mult(x, y):
            return x * y

        return mult
    elif number == "0":
        def division(x, y):
            return x / y

        return division
    else:
        raise Exception("Использован не верный код")


new_func = act("0")
result = new_func(25, 5)
print(result)
print("=====")

# Лямбда функции
root = (lambda x: sqrt(x))
print(root(36))


def root_1(x):
    return sqrt(x)


print(root_1(81))
print("=====")


# Вызываемые объекты
class Rect:
    def __init__(self, a):
        self.a = a

    def __call__(self, b):
        return self.a * b


length_side = Rect(4)
square_rect = length_side(6)
print(square_rect)
