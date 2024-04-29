from colorama import Fore


class Vehicle:
    def __init__(self, vehicle_type="none"):
        self.vehicle_type = vehicle_type


class Car:
    def __init__(self, price=1000000):
        self.price = price

    def horse_powers(self):
        return 149


class Nissan(Vehicle, Car):
    def __init__(self, vehicle_type, price):
        super().__init__(vehicle_type)
        Car.__init__(self, price)

    def horse_powers(self):
        return 199


nissan = Nissan("sedan", 1200000)
print(Fore.YELLOW)
print("Тип автомобиля ", nissan.vehicle_type)
print(Fore.MAGENTA)
print("Цена автомобиля ", nissan.price)
