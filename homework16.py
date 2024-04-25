class Car:
    price = 1000000

    def horse_powers(self):
        self.horse_powers = 149
        return self.horse_powers


class Nissan(Car):
    price = 1200000

    def horse_powers(self):
        self.horse_powers = 179
        return self.horse_powers


class Kia(Car):
    price = 900000

    def horse_powers(self):
        self.horse_powers = 105
        return self.horse_powers


car = Car()
print("Абстрактная машина")
print("Цена ", car.price, " ", "Мощность ", car.horse_powers())
print("Nissan ======================")
nissan = Nissan()
print("Цена ", nissan.price, " ", "Мощность ", nissan.horse_powers())
print("Kia ==========================")
kia = Kia()
print("Цена ", kia.price, " ", "Мощность ", kia.horse_powers())
