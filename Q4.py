import matplotlib.pyplot as plt
import numpy as np
import math as m
import random as rndm

# 4.1 -------------------------------------------------------------------------------------------
def random_theta():
    theta1 = np.random.uniform(0,360)*(m.pi/180)
    theta2 = np.random.uniform(0,360)*(m.pi/180)
    return (theta1,theta2)

def cord(R):
    angle = random_theta()
    theta = abs(angle[0] - angle[1])
    l = 2*R*m.sin(theta/2)  #length of cord = 2rsin(theta/2)
    return(l)

def find_cords1(R):

    cord_len = []
    I = 1000    #iterations

    for _ in range(I):
        cord_len.append(cord(R))

    plt.hist(cord_len, bins = range(0,R))
    plt.title("Histogram of 4.1")
    plt.savefig("Q4/Q4(1).png")
    plt.show()

# 4.2 -------------------------------------------------------------------------------------------
def random_cord(R):

    theta = np.random.uniform(0,360)*(m.pi/180)
    point_at_radius = np.random.uniform(0,R)    #point at R

    #cartesian cordinates at the picked point
    x = point_at_radius*m.cos(theta)
    y = point_at_radius*m.sin(theta)

    #finding base line from center to point_at_radius using distance formula
    base = m.sqrt(x**2+y**2)

    #perpendicular using pythagorean theorem, p = sqrt(h^2-b^2)
    perp = m.sqrt(R**2-base**2)

    #length of the cord
    l = 2*perp

    return l

def find_cords2(R):

    cord_len = []
    I = 1000    #iterations

    for _ in range(I):
        cord_len.append(random_cord(R))
    
    plt.hist(cord_len, bins = range(0,R))
    plt.title("Histogram of 4.2")
    plt.savefig("Q4/Q4(2).png")
    plt.show()

# 4.3 -------------------------------------------------------------------------------------------
