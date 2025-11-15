import math

class Circle:
    def __init__(self, r):
        self.r = r
        self.area = math.pi * r ** 2
        self.perimeter = 2 * math.pi * r

    def geometry(self):
        print(f"Area of the circle = {self.area} and Perimeter of the circle = {self.perimeter}")


# Example usage
r = int(input("Enter the radius: "))
circle = Circle(r)
circle.geometry()
