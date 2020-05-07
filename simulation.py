# ___NOTES TO SELF___ #
# velocity is change of position:
# position += velocity * time
# v = at + v0
# a = f / m1
# f = unitVector * G * m1 * m2 / r^2
# r = (pos2 - pos1).magnitude
# magnitude = m.sqrt(x**2 + y**2 + z**2)

import math
from vector3class import *

# THIS FILE IS A LITTLE DIFFERENT THAN THE NOTEBOOK BECAUSE IT IS ALSO USED FOR TESTING.
# "___SOMETHING SOMETHING___" is header comments.


# ___CLASSES___ #

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


# ___THE PHYSICS___ #

# F = G * m1 * m1 / r^2
# a = F / m1
def UpdateAcceleration(body, objectList, timeStep):
    G = 6.674E-11

    acceleration = Vector3(0,0,0)
    for otherBody in objectList:
        if otherBody != body:
            distance = otherBody.position - body.position
            unitVector = distance.Normalize()
            r = distance.Magnitude()
            acceleration += unitVector * G * otherBody.mass / r ** 2
    return acceleration


# v = a * t
def UpdatePosition(body, objectList, timeStep=1):
    # Multiply by time squared to get final and longest distance possibly traveled in x amount of time.
    body.velocity += UpdateAcceleration(body, objectList, timeStep) * timeStep
    body.position += body.velocity * timeStep


# This is the main loop that stores our points.
def Simulate(objectList, iterations=100, timeStep=1):
    orbits = []
    for body in objectList:
        orbits.append(BodyData(body.name, [body.position]))

    for iteration in range(iterations):
        for index, body in enumerate(objectList):
            UpdatePosition(body, objectList, timeStep)
            orbits[index].positions.append(body.position)

    return orbits

# ___THE PLOTTING___ #
# We make the graphs here :)
from matplotlib import pyplot as plt


# Plots the actual data.
# *Slaps roof of function* "This bad boy can fit so many cool graphs in it"
def PlotTheData(systemData, rotate=True, zdir="z"):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    axisRange = 0

    # Each bodyData contains a name and a list of vectors3's.
    for bodyData in systemData:
        positions = bodyData.positions
        xValues = []
        yValues = []
        zValues = []
        for vector in positions:
            xValues.append(vector.x)
            yValues.append(vector.y)
            zValues.append(vector.z)

        # Used to stretch the axes so they are the same length.
        largestPositionValue = max([max(xValues), abs(min(xValues)),
                                    max(yValues), abs(min(yValues)),
                                    max(zValues), abs(min(zValues))])
        if axisRange < largestPositionValue: axisRange = largestPositionValue

        # The centre of the system is usually the first object in the list and may not move much.
        # Therefore we make it a dot.
        if bodyData is systemData[0]:
            ax.scatter(xValues[0], yValues[0], zValues[0], label=bodyData.label, zdir=zdir, color="r")
        else:
            ax.plot(xValues, yValues, zValues, label=bodyData.label, zdir=zdir)

    # These lines just name the axes. Doesn't account for the occasional run where I swap the z direction.
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")
    ax.legend()

    # Here I set the axis ranges.
    #ax.set_xlim(-axisRange,axisRange)
    #ax.set_ylim(-axisRange,axisRange)
    #ax.set_zlim(-axisRange,axisRange)

    # This part rotates the thing around for a while.
    if rotate:
        rotatePlot(ax)

    plt.show()  # Shows interactive figure until we exit.


def rotatePlot(ax):
    framePause = 1 / 60**2
    for loopAmount in range(2):
        # Rotates it to view from top.
        for angle in range(10, 90):
            ax.view_init(angle, 45)
            plt.draw()
            plt.pause(framePause)
        # Rotates it down.
        for angle in range(90, -30, -1):
            ax.view_init(angle, 45)
            plt.draw()
            plt.pause(framePause)
        # Rotates it back up again so we can loop.
        for angle in range(-30, 10):
            ax.view_init(angle, 45)
            plt.draw()
            plt.pause(framePause)


# ___THE SIMULATION PART___ #
# __PRESET SYSTEM CONFIGURATIONS__ #

# https://nssdc.gsfc.nasa.gov/planetary/factsheet/
# Solar System:
sun = Body(position=Vector3(0,0),
           velocity=Vector3(0,0),
           mass=1.989E30,
           name="sun")
mercury = Body(position=Vector3(0,46.00e+9),
            velocity=Vector3(-58980,0),
            mass=3.3011E+23,
            name="mercury")
venus = Body(position=Vector3(0,107.48e+9),
            velocity=Vector3(-35260,0),
            mass=4.87e+24,
            name="venus")
earth = Body(position=Vector3(0,147098074e+3),
             velocity=Vector3(-30290,0),
             mass=5.97e24,
             name="earth")
mars = Body(position=Vector3(0,206.7e+9),
            velocity=Vector3(-26500,0),
            mass=6.39e+23,
            name="mars")
jupiter = Body(position=Vector3(0,740.52e+9),
               velocity=Vector3(-13720, 0),
               mass=1898.19e+24,
               name="jupiter")
saturn = Body(position=Vector3(0,1352e+9),
              velocity=Vector3(-10180, 0),
              mass=568.34e+24,
              name="saturn")
uranus = Body(position=Vector3(0, 2741.30e+9),
              velocity=Vector3(-7.11e+3, 0),
              mass=86.813e+24,
              name="uranus")
neptune = Body(position=Vector3(0,4444.45e+9),
               velocity=Vector3(-5.50e+3, 0),
               mass=102.413e+24,
               name="neptune")

solarSystem = [sun, earth]

# 1 earth circular orbit = 365 days in this simulation (365 iterations)
# 1 mars circular orbit = 669 days in this simulation

# Particle system:
particle1 = Body(position=Vector3(0, 0),
                 mass=1e+11,
                 name="particle1")
particle2 = Body(position=Vector3(0, 6.674),
                 velocity=Vector3(1, 0),
                 mass=1,
                 name="particle2")

particleSystem = [particle1, particle2]

# __Safe-to-touch data and stuff__ #
# More iterations means more time to compute.
# Larger timeStep means less time to compute but more inaccuracy.
# timeStep is basically just changing the time unit in our physical formulas from
# seconds to something else (e.g. like hours or days).

# E.g. if we have 100 years between each "jump" in position, it will be
# super-duper-mega inaccurate.
hour = 60*60
day = 24*hour

# Below is the "standard" parameters I have found out to work pretty nice.
# We have a timestep of one hour and by changing "669", we can change the amount
# of days we simulate. I.e. one year is 365 days, so we can simulate only one year
# if we want.
bodiesInSystem = solarSystem
iterations = 687*24
timeStep = 60*60
dataToPlot = Simulate(bodiesInSystem, iterations, timeStep)
PlotTheData(dataToPlot, False, "z")

# ___TESTING___ #
testingMode = False

# We will just stop execution here when not testing stuff.
if not testingMode: quit()


def GetCirclePoints(xOffset=0, yOffset=0, zOffset=0):
    points = []
    for i in range(1, 100):
        sin = math.sin(i/10) + xOffset + yOffset + zOffset
        cos = math.cos(i/10) + xOffset + yOffset + zOffset
        vectorPoint = Vector3(cos, sin)
        points.append(vectorPoint)
    return points


dataToPlot = [BodyData("circle", GetCirclePoints()), BodyData("circle2", GetCirclePoints(1))]

PlotTheData(dataToPlot)

# TODO USE APOAPSIS / PERIAPSIS DATA AND SPEED SO THE ORBITS DONT GET CIRCULAR (AT LEAST I HOPE THAT'LL SOLVE IT)
