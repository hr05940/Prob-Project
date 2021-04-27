import random
from matplotlib import pyplot as plt
import  fishC  as f
from scipy import stats
import math
import statistics
import numpy as np

# --------------------------- 5.1 ------------------------------
def cointoss():
    #assuming 0 = T & 1 = H
    return(random.randint(0,1)) 


def simulate_tosses():
    expected = []
    for n in range(100): #to get 100 expected values
        rejected = []
        for j in range(100): #to get 1 expected value
            outcomes = []
            for i in range(10): #to get 10 outcomes/1 rejected value
                outcomes.append(cointoss())
            #check hypothesis accepted or rejected
            if sum(outcomes) == 0 or sum(outcomes) == 1 or sum(outcomes) == 10 or sum(outcomes) == 9:
                rejected.append(1) #hypothesis rejected
            else:
                rejected.append(0) #hypothesis accepted
        expected.append(sum(rejected)/100)
    #plotting histogram
    fig, ax = plt.subplots(figsize =(10, 7))
    ax.hist(expected, bins = [-0.01,0,0.01,0.02,0.03,0.04,0.05,0.06,0.07,0.08,0.09,0.1])
    ax.set_xlabel('Times the null hypothesis is rejected')
    ax.set_ylabel('Frequency')
    plt.title('Mean: '+str(round(statistics.mean(expected),3))+', Variance: '+str(round(statistics.variance(expected),3)))
    plt.savefig("Q5_histograms/Q5.1(1).png")
    plt.show()

# simulate_tosses()

# ------------------------------------ 5.2 ---------------------------------------------

def hypothesis_test(u_0, n):
    s = []
    for i in range(n): #catching a sample of 30 fish
        s.append(f.fish())
    s = np.array(s)
    std = s.std() #sample standard deviation
    mean = s.mean() #sample mean
    a = abs(mean - u_0)
    prob = 2*(stats.norm(u_0, std/math.sqrt(n)).cdf(u_0 - a))
    if prob < 0.05:
        return 1 #rejected
    else:
        return 0 #accepted


def experiments():
    u_0 = 23
    n = 30
    expected = []
    for j in range(100):
        outcomes = []
        for i in range(50):
            outcomes.append(hypothesis_test(u_0,n))
        expected.append(sum(outcomes)/50)
    #plotting histogram
    fig, ax = plt.subplots(figsize =(10, 7))
    a = np.arange(0.8,1.1,0.015)
    ax.hist(expected, bins = a)
    ax.set_xlabel('Times the null hypothesis is rejected')
    ax.set_ylabel('Frequency')
    plt.title('Population Mean: '+str(u_0)+', Sample Size: '+str(n)+'\n Mean: '+str(round(statistics.mean(expected),3))+', Variance: '+str(round(statistics.variance(expected),3)))
    plt.savefig("Q5_histograms/Q5.2.1(3).png")
    plt.show()


def experiments_2():
    u_0 = 23
    n = 70
    expected = []
    for j in range(100):
        outcomes = []
        for i in range(50):
            outcomes.append(hypothesis_test(u_0,n))
        expected.append(sum(outcomes)/50)
    #plotting histogram
    fig, ax = plt.subplots(figsize =(10, 7))
    ax.hist(expected, bins = [0.5,0.6,0.7,0.8,0.9,1,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8])
    ax.set_xlabel('Times the null hypothesis is rejected')
    ax.set_ylabel('Frequency')
    plt.title('Population Mean: '+str(u_0)+', Sample Size: '+str(n)+'\n Mean: '+str(round(statistics.mean(expected),3))+', Variance: '+str(round(statistics.variance(expected),3)))
    plt.savefig("Q5_histograms/Q5.2.2.png")
    plt.show()

# experiments()

# ------------------------------------------------- 5.2.3---------------------------------------------
def my_fish():
    return np.random.normal(23,3)

def testing(u_0,n):
    s = []
    for i in range(n): #catching a sample of 30 fish
        s.append(my_fish())
    s = np.array(s)
    std = s.std() #sample standard deviation
    mean = s.mean() #sample mean
    a = abs(mean - u_0)
    prob = 2*(stats.norm(u_0, std/math.sqrt(n)).cdf(u_0 - a))
    if prob < 0.1:
        return 1 #rejected
    else:
        return 0 #accepted

def simulation():
    u_0 = 23 #population mean 
    n = 40
    expected = []
    for j in range(100):
        outcomes = []
        for i in range(50):
            outcomes.append(testing(u_0,n))
        expected.append(sum(outcomes)/50)
    #plotting histogram
    fig, ax = plt.subplots(figsize =(10, 7))
    a = np.arange(0,2,0.1)
    ax.hist(expected, bins = a)
    ax.set_xlabel('Times the null hypothesis is rejected')
    ax.set_ylabel('Frequency')
    plt.title('Population Mean: '+str(u_0)+', Sample Size: '+str(n)+'\n Mean: '+str(round(statistics.mean(expected),3))+', Variance: '+str(round(statistics.variance(expected),3)))
    plt.savefig("Q5_histograms/Q5.2.3_"+str(n)+"(3).png")
    plt.show()

simulation()

# 5.2.1:
# - is mean supposed to be equal to null hypothesis

# 5.1:
# - hist looks odd

# 5.2.2:
# - is this it?

# 5.2.3:
# - mean isnt going to 10...