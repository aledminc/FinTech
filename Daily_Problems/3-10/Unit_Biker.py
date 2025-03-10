import random
import math
import numpy

class BikerCircle:

    unit_circle = []

    for x in numpy.arange(-1, 1.01, .01):
        y = math.sqrt(1 - round(x,2)**2)
        unit_circle.append([x, y])
        unit_circle.append([x, -y])

    def TriangleAcute(pos1, pos2):
        side1 = math.sqrt((pos2[0] - pos1[0])**2 + (pos2[1] - pos1[1])**2)

        sides = sorted([side1, 1, 1])

        if sides[0]**2 + sides[1]**2 > sides[2]**2:
            return True
        else: 
            return False

class BikerSphere:

    unit_sphere = []

    for x in numpy.arange(-1, 1.01, .01):
        for y in numpy.arange(-1, 1.01, .01):
            if 1 - round(x,2)**2 - round(y,2)**2 >= 0:
                z = math.sqrt(1 - round(x,2)**2 - round(y,2)**2)
                unit_sphere.append([x, y, z])
                unit_sphere.append([x, y, -z])

    def TriangleAcute(pos1, pos2):
        side1 = math.sqrt((pos2[0] - pos1[0])**2 + (pos2[1] - pos1[1])**2 + (pos2[2] - pos1[2])**2)
        
        sides = sorted([side1, 1, 1])

        if sides[0]**2 + sides[1]**2 > sides[2]**2:
            return True
        else:
            return False

class SimBiker:

    acute_occur_circ = 0
    acute_occur_sphere = 0
    sims = 50000

    #CIRCLE SIMULATION
    for _ in range(sims):

        rider1 = random.choice(BikerCircle.unit_circle)
        rider2 = random.choice(BikerCircle.unit_circle)

        if BikerCircle.TriangleAcute(rider1, rider2):
            acute_occur_circ += 1
    
    #SPHERE SIMULATION
    for _ in range(sims):
        
        rider1 = random.choice(BikerSphere.unit_sphere)
        rider2 = random.choice(BikerSphere.unit_sphere)

        if BikerSphere.TriangleAcute(rider1, rider2):
            acute_occur_sphere += 1

    print("For unit circle: " + str(acute_occur_circ/sims) + ", for unit sphere " + str(acute_occur_sphere/sims))
    # Mathematically, I believe its 1/2 for the circle, and less for the sphere, but the simulation returns 1/2 for both