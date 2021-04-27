import numpy as np
import matplotlib.pyplot as plt
import math as m

def random_point(R):

    #r=radius, theta=angle
    r = R*m.sqrt(np.random.uniform(0,1))     #random r using R(CDF)**1/2
    theta = np.random.uniform(0, 360)*(m.pi/180)   #random theta between 0-360 degrees
    return(polar_to_cart(r,theta))

def polar_to_cart(r,t):

    x = r * np.cos(t)  #x = rcos(theta)
    y = r * np.sin(t)  #y = rsin(theta)
    return((x,y))

def gen_points(R):

    I = 1000     #iterations
    X = []    #list for x axis
    Y = []    #list for y axis

    #generating the lists for X and Y
    for _ in range(I):
        point = random_point(R)
        X.append(point[0])
        Y.append(point[1])

    """Drawing the circles and plotting the points"""
    
    #Outer Circle of radius R
    fig, axes = plt.subplots()
    axes.axis([-R-1,R+1,-R-1,R+1])
    circle1 = plt.Circle((0,0),R,Fill=False,color="red")
    axes.set_aspect(1)
    axes.add_artist(circle1)

    #inner circle of radius R/2
    circle2 = plt.Circle((0,0),R/2,Fill=False,color="green")
    axes.set_aspect(1)
    axes.add_artist(circle2)
    fig.legend([circle1,circle2],["outer circle", "inner circle"])

    #Plotting X and Y
    plt.plot(X,Y,'.',color="blue")
    fig.suptitle("Graph 3.3", fontsize=13,fontweight='bold')
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.title("Radius = {}, Variance of x = {}".format(R, np.var(X)),fontsize=10)
    plt.savefig("Q3/Q3(3).png")
    plt.show()

#Testing
x = gen_points(5)