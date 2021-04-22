import numpy as np
import matplotlib.pyplot as plt
import math as m

def random_point(radius):

    #R=radius, theta = angle
    R = np.random.uniform(0, radius)    #random R in range 0-R
    theta = np.random.uniform(0, 360)*(m.pi/180)   #random theta between 0-360 degrees
    return(polar_to_cart(R,theta))

def polar_to_cart(r,t):

    x = r * np.cos(t)  #x = rcos(theta)
    y = r * np.sin(t)  #y = rsin(theta)
    return((x,y))

def gen_points(l_radius):

    I = 1000     #iterations
    X = []    #list for x axis
    Y = []    #list for y axis

    #generating the lists for X and Y
    for p in range(I):
        point = random_point(l_radius)
        X.append(point[0])
        Y.append(point[1])

    print("The variance on the x-axis is " + str(np.var(X)))    #variance of x

    #Drawing the circle
    fig, axes = plt.subplots()
    circle = plt.Circle((0,0),l_radius,Fill=False)
    axes.set_aspect(1)
    axes.add_artist(circle)
    plt.title("circle")

    #Plotting X and Y
    plt.plot(X,Y,'.',color="blue")
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.title("Graph of 3.1")
    plt.show()

#Testing
R = input("Enter the radius: ")
gen_points(int(R))