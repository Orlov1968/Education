def string_to_int(s):  # добавить обработку ValueError
    try:
        return int(s)
    except ValueError:
        print(f"Ошибка: Значение переменной {s} не является целым числом.")


def read_file(filename):  # добавить обработку FileNotFoundError, IOError
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Ошибка: Файл {filename} не существует. Проверьте правильный путь до файла {filename}.")
    except IOError:
        print(f"Ошибка: Файл {filename} не найден или заполнен диск.")


def divide_numbers(a, b):  # добавить обработку ZeroDivisionError, TypeError
    try:
        return a / b
    except ZeroDivisionError:
        print(f"Ошибка: Делить на ноль запрещено. Замените значение {b} на отличное от ноля число.")
    except TypeError:
        print(f"Ошибка: Тип значений {a} или {b} не являются числом. Замените значения на требуемый тип.")


def access_list_element(lst, index):  # добавить обработку IndexError, TypeError
    try:
        return lst[index]
    except IndexError:
        print(f"Ошибка: {index} Индекс последовательности lst находится вне допустимого диапазона.")
    except TypeError:
        print(f"Ошибка: Тип значения {index} не являются целым числом. Замените значение на требуемый тип.")
