class Car:
    colour = "Red"

def __init__(self, n):
    self.speed = "100mph"
    self.name = n

car1 = Car("Honda")
car1.colour = "Yellow"
car2 = Car()
car2.speed = "80mph"
print(car1.colour)
print(car2.speed)
print(car1.name)
