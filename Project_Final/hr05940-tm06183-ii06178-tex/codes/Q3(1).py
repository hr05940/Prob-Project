import numpy as np
import matplotlib.pyplot as plt
import math as m

def random_point(R):

    #R=R, theta = angle
    r = np.random.uniform(0, R)    #random R in range 0-R
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

    """Drawing the circle and plotting the points"""
    
    #Drawing the circle
    fig, ax = plt.subplots()
    ax.axis([-R-1,R+1,-R-1,R+1])
    circle = plt.Circle((0,0),R,Fill=False)
    ax.set_aspect(1)
    ax.add_artist(circle)
    plt.title("circle")

    #Plotting X and Y
    plt.plot(X,Y,'.',color="blue")
    fig.suptitle("Graph 3.1",fontsize=13,fontweight='bold')
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.title("Radius = {}, Variance of x = {}".format(R,np.var(X)),fontsize=10)
    plt.savefig("Q3/Q3(1).png")
    plt.show()

#Testing
gen_points(5)