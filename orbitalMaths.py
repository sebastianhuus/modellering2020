# I use this module to calculate stable orbit parameters.


def orbitalVelocity(centralMass, height):
    G = 6.674e-11
    return (G*centralMass / height)**0.5


def orbitalHeight(centralMass, velocity):
    G = 6.674e-11
    return G * centralMass / velocity**2


# Stable particle orbit. I just slapped on some 10^n's until I got what I wanted.
print(orbitalHeight(1e+11, 1)) # Particle
print()

print(orbitalHeight(1.989E30, 38.86e+3)) # Mercury
print(orbitalHeight(1.989E30, 34.79e+3)) # Venus
print(orbitalHeight(1.989E30, 29.29e+3)) # Earth
print(orbitalHeight(1.989E30, 21.97e+3)) # Mars
print()

def auToMeters(au):
    return au * 149597871e+3


print(auToMeters(1.67))
