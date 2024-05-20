from datetime import datetime


class InvalidDateException(Exception):
    pass


class SmallAgeException(Exception):
    pass


def input_date_of_born():
    string_date_wos_born = input("Введите Вашу дату рождения в формате гггг-мм-дд: ")
    date_was_born = datetime.strptime(string_date_wos_born, "%Y-%m-%d").date()
    if not datetime.strptime(string_date_wos_born, "%Y-%m-%d").date():
        raise InvalidDateException
    return date_was_born


def determine_the_age():
    date_now = datetime.now().date()
    age = int((date_now - input_date_of_born()).days / 365)
    if age < 18:
        raise SmallAgeException
    return age


def registration_permission():
    try:
        determine_the_age()
    except SmallAgeException:
        print("Регистрация  только 18+")
    except InvalidDateException:
        print("Введён не верный формат даты")
    except ValueError:
        print("Введён не верный формат даты")
    else:
        print("Регистрация завершена")


registration_permission()
