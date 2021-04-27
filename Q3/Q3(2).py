import matplotlib.pyplot as plt
import numpy as np
import math as m

def random_point(R):

    x = np.random.uniform(-R,R) #random point x
    y = np.random.uniform(-R,R) #random point y
    return((x,y))

def dist_from_origin(x,y):
    return(m.sqrt(x**2+y**2))

def gen_points(R):

    X = []       #list for x-axis
    Y = []       #list for y-axis
    I = 1000     #iterations

    for a in range(I):
        point = random_point(R)
        if dist_from_origin(point[0],point[1]) <= R:  #if distance is smaller than or equal to R
            X.append(point[0])
            Y.append(point[1])
        else:               #if distance is greater than R
            a = a-1
    
    """Drawing the circle and plotting the points"""
    
    #Drawing the circle
    fig, ax = plt.subplots()
    ax.axis([-R-1,R+1,-R-1,R+1])
    circle = plt.Circle((0,0),R,Fill=False)
    ax.set_aspect(1)
    ax.add_artist(circle)
    plt.title("circle")

    #Plotting the points
    plt.plot(X,Y,'.',color="red")
    fig.suptitle("Graph 3.2",fontsize=13,fontweight='bold')
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.title("Radius = {}, Variance of x = {}".format(R,np.var(X)),fontsize=10)
    plt.savefig("Q3/Q3(2).png")
    plt.show()

#Testing
gen_points(5)