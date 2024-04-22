class Buiding:

    def __init__(self):
        self.numberOfFloors = 5
        self.buildingType = "5"

    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType


building_1 = Buiding()
building_2 = Buiding()
print(building_1.numberOfFloors == building_2.buildingType)
