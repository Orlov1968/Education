class House:
    def __init__(self):
        self.numberOfFloors = 10


hours = House()
for i in range(hours.numberOfFloors):
    print("Текущий этаж равен ", i + 1)