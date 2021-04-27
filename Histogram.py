import math as m
import matplotlib.pyplot as plt

x = [1.3,2.5,2.7,1.6,3.7,7.4,3.2,4.3,3.3,3.4]

n = len(x)
rng = max(x)-min(x)
i = int(m.sqrt(n))
width = rng/i

bin_lst = [a*width for a in range(i+1)]

arr=plt.hist(x,bins=bin_lst)
plt.ylim(rng+1)
for a in range(i):
        plt.text(arr[1][a],arr[0][a],str(arr[0][a]))
plt.show()

print(n)
print(rng)
print(i)
print(width)
print(bin_lst)
