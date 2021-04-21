import random
from matplotlib import pyplot as plt

def cointoss():
    #assuming 0 = T & 1 = H
    return(random.randint(0,1)) 

# rejected: all heads/all tails + 1 head/1 tail 
        # prob x < 0 + x >= 10 
        # 1 head == 1 tail >= 0 heads >= 0 tails
        # x = no. of heads
        # P(X <= x) + P(X <= n-x) < threshold

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

    #calculate expected of 100 hypothesis accepted or rejected --> 1 expected value
    #repeat 

simulate_tosses()

