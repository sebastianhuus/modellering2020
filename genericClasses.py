from vector3class import *

# Basically planets. Can possibly be other stuff if we want to.
# Note that we don't track size and such (for now)
class Body:
    def __init__(self, position, velocity=Vector3(0,0), mass=0.0, name="unknown"):
        self.position = position
        self.velocity = velocity
        self.mass = mass
        self.name = name


# Holds the actual data to be plotted, with a label attached so we know what it is.
# This is really just because I think dictionaries and lists can become quite messy sometimes.
# Also, classes are cool :)
class BodyData:
    def __init__(self, label, positions = []):
        self.positions = positions  # Holds vector3's
        self.label = label

    def __str__(self):
        return "Name: " + self.label + ", " + str(self.positions)
