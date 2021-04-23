import random
from matplotlib import pyplot as plt
import  fishCImport  as f
import statistics

# --------------------------- 5.1 ------------------------------
def cointoss():
    #assuming 0 = T & 1 = H
    return(random.randint(0,1)) 

'''rejected: all heads/all tails + 1 head/1 tail 
prob x < 0 + x >= 10 
1 head == 1 tail >= 0 heads >= 0 tails
x = no. of heads
P(X <= x) + P(X <= n-x) < threshold'''

def simulate_tosses():
    expected = []
    for n in range(50):
        rejected = []
        for j in range(100):
            outcomes = []
            for i in range(10):
                outcomes.append(cointoss())
            #check hypothesis accepted or rejected
            if sum(outcomes) == 0 or sum(outcomes) == 1 or sum(outcomes) == 10 or sum(outcomes) == 9:
                rejected.append(1) #hypothesis rejected
            else:
                rejected.append(0) #hypothesis accepted
        expected.append(sum(rejected)/100)
    #plotting histogram
    fig, ax = plt.subplots(figsize =(10, 7))
    ax.hist(expected, bins = [0,0.1,0.2,0.3,0.4,0.5,1,1.5,2,2.5,3,3.5,4,4.5,5,5.5,6])
    # plt.title('n = '+str(n)+', p = '+str(p))
    # plt.savefig("Q1_histograms/q1"+'n = '+str(n)+', p = '+str(p)+'.png')
    plt.show()

# simulate_tosses()

# ------------------------------------ 5.2 ---------------------------------------------

def hypothesis_test(u_0, n):
    s = []
    for i in range(n): #catching a sample of 30 fish
        s.append(f.fish())
    u = round(sum(s)/n,3) #sample mean
    var = statistics.variance(s) #sample variance 
    prob = 0
    for i in s:
        if abs(s - u_0) >= abs(u-u_0):
            prob += (1/30)
    print(prob)
    if prob < 0.05:
        return 1 # 1 == rejected
    else:
        return 0


hypothesis_test(23,30)

def experiments():
    u_0 = 23
    n = 30
    expected = []
    
    for j in range(100):
        outcomes = []
        for i in range(20):
            outcomes.append(hypothesis_test(u_0,n))
        expected.append(sum(outcomes)/20)
    
    #plotting histogram
    fig, ax = plt.subplots(figsize =(10, 7))
    ax.hist(expected, bins = [0,0.1,0.2,0.3,0.4,0.5,1,1.5,2,2.5,3,3.5,4,4.5,5,5.5,6])
    # plt.title('n = '+str(n)+', p = '+str(p))
    # plt.savefig("Q1_histograms/q1"+'n = '+str(n)+', p = '+str(p)+'.png')
    plt.show()