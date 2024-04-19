class Buiding:

    def __init__(self):
        self.numberOfFloors = 5
        self.buildingType = "5"

    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType

