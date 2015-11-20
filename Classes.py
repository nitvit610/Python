class Squarea:
    def __init__(self, x):
        self.x = x
    def area(self):
        area_total = self.x * self.x
        print(area_total)

square = Squarea(50)

square.area()