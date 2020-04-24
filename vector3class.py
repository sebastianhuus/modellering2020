import math


# This bad boy is super useful. Not fully-fledged because I don't need all possible vector operations.
class Vector3:
    def __init__(self, x, y, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __truediv__(self, scalar):
        if scalar == 0: print("Vector division by zero.")
        return Vector3(self.x/scalar, self.y/scalar, self.z/scalar)

    def __mul__(self, scalar):
        return Vector3(self.x*scalar, self.y*scalar, self.z*scalar)

    def Magnitude(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def Normalize(self):
        return self / self.Magnitude()

    def __str__(self):
        return str(self.x) + ", " + str(self.y) + ", " + str(self.z)
