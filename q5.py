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
            #check if hypothesis is accepted or rejected
            if sum(outcomes) == 0 or sum(outcomes) == 1 or sum(outcomes) == 10 or sum(outcomes) == 9:
                rejected.append(1) #hypothesis rejected
            else:
                rejected.append(0) #hypothesis accepted
        expected.append(sum(rejected)/100)
    #plotting histogram
    fig, ax = plt.subplots(figsize =(10, 7))
    ax.hist(expected,width = 0.01)
    ax.set_xlabel('Times the null hypothesis is rejected')
    ax.set_ylabel('Frequency')
    plt.title('Mean: '+str(round(statistics.mean(expected),3))+', Variance: '+str(round(statistics.variance(expected),3)))
    plt.savefig("Q5_histograms/Q5.1.png")
    plt.show()

# simulate_tosses()

# --------------------------- 5.2.1 ------------------------------

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
    u_0 = 23 #population mean 
    n = 30 #sample size
    expected = []
    for j in range(100): #getting 100 expected values
        outcomes = []
        for i in range(50): #conducting 50 hypothesis tests
            outcomes.append(hypothesis_test(u_0,n))
        expected.append(sum(outcomes)/50) #calculating one expected value from the 50 tests
    #plotting histogram of expected values
    fig, ax = plt.subplots(figsize =(10, 7))
    ax.hist(expected, width = 0.04)
    ax.set_xlabel('Times the null hypothesis is rejected')
    ax.set_ylabel('Frequency')
    plt.title('Population Mean: '+str(u_0)+', Sample Size: '+str(n)+'\n Mean: '+str(round(statistics.mean(expected),3))+', Variance: '+str(round(statistics.variance(expected),3)))
    plt.savefig("Q5_histograms/Q5.2.1.png")
    plt.show()

# --------------------------- 5.2.2 ------------------------------

def experiments_updated():
    u_0 = 23 #population mean
    n = 70 #sample size
    expected = []
    for j in range(100): #getting 100 expected values
        outcomes = []
        for i in range(50): #conducting 50 hypothesis tests
            outcomes.append(hypothesis_test(u_0,n))
        expected.append(sum(outcomes)/50)
    #plotting histogram
    fig, ax = plt.subplots(figsize =(10, 7))
    ax.hist(expected, width = 0.1)
    ax.set_xlabel('Times the null hypothesis is rejected')
    ax.set_ylabel('Frequency')
    plt.title('Population Mean: '+str(u_0)+', Sample Size: '+str(n)+'\n Mean: '+str(round(statistics.mean(expected),3))+', Variance: '+str(round(statistics.variance(expected),3)))
    plt.savefig("Q5_histograms/Q5.2.2.png")
    plt.show()

# experiments_updated()

# --------------------------- 5.2.3 ------------------------------

def my_fish():
    return np.random.normal(23,3)

def testing(u_0,n):
    s = []
    for i in range(n): #catching a sample of 30 fish using the new fish function
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
    n = 90 #sample size
    expected = []
    for j in range(100): #getting 100 expected values
        outcomes = []
        for i in range(50):  #conducting 50 hypothesis tests
            outcomes.append(testing(u_0,n))
        expected.append(sum(outcomes)/50)
    #plotting histogram
    fig, ax = plt.subplots(figsize =(10, 7))
    ax.hist(expected, width = 0.03)
    ax.set_xlabel('Times the null hypothesis is rejected')
    ax.set_ylabel('Frequency')
    plt.title('Population Mean: '+str(u_0)+', Sample Size: '+str(n)+'\n Mean: '+str(round(statistics.mean(expected),3))+', Variance: '+str(round(statistics.variance(expected),3)))
    plt.savefig("Q5_histograms/Q5.2.3_"+str(n)+".png")
    plt.show()

# simulation()

