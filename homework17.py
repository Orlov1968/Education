from colorama import Fore


class Vehicle:
    vehicle_type = "none"


class Car(Vehicle):
    price = 1000000

    def horse_powers(self, horse_powers):
        self.horse_powers = horse_powers
        return self.horse_powers


class Nissan(Car):
    vehicle_type = "sedan"
    price = 1200000

    def horse_powers(self, horse_powers):
        self.horse_powers = horse_powers
        return self.horse_powers


nissan = Nissan()
print(Fore.YELLOW)
print("Тип автомобиля ", nissan.vehicle_type)
print(Fore.MAGENTA)
print("Цена автомобиля ", nissan.price)
