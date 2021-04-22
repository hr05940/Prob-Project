import matplotlib.pyplot as plt
import numpy as np
import math as m

def random_point(lmt_rad):

    x = np.random.uniform(-lmt_rad,lmt_rad) #random point x
    y = np.random.uniform(-lmt_rad,lmt_rad) #random point y
    return((x,y))

def dist_from_origin(x,y):
    return(m.sqrt(x**2+y**2))

def gen_points(l_r):

    X = []       #list for x-axis
    Y = []       #list for y-axis
    I = 1000     #iterations

    for x in range(I):
        point = random_point(l_r)
        if dist_from_origin(point[0],point[1]) <= l_r:  #if distance is smaller than or equal to R
            X.append(point[0])
            Y.append(point[1])
        else:               #if distance is greater than R
            x = x-1
    
    print("The variance on the x-axis is " + str(np.var(X)))    #variance of X

    #Drawing the circle
    fig, axes = plt.subplots()
    circle = plt.Circle((0,0),l_r,Fill=False)
    axes.set_aspect(1)
    axes.add_artist(circle)
    plt.title("circle")

    #Plotting the points
    plt.plot(X,Y,'.',color="red")
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.title("Graph of 3.2")
    plt.show()

#Testing
R = input("Enter the radius: ")
gen_points(int(R))