#2
import numpy as np
import matplotlib.pyplot as plt
# y = []
# for i in range (100000) :
#     x = np . random . random ()
#     y . append ( - np . log (1 - x ) )

# bins = 1000
# binWidth = (max( y ) - min( y ) ) / bins
# plt . hist (y , bins = bins , weights = np . ones (len ( y ) ) /( len ( y ) * binWidth ) )
# values = np . linspace ( min( y ) , max( y ) , 50)
# plt . plot ( values , np . exp ( - values ) )
# plt . show ()

#2.1

#2.2
# y = []
# for i in range (100000) :
#     x = np . random . random ()
#     y . append (1 / (1 - x ) )
# y . sort ()
# ind = ( np . array ( y ) > 30) . tolist () . index (1)
# y = y [: ind ]
# bins = 100
# binWidth = (max( y ) - min( y ) ) / bins
# plt . hist (y , bins = bins , weights = np . ones (len ( y ) ) /( len ( y ) * binWidth ) )
# values = np . linspace ( min( y ) , max( y ) , 50)
# plt . plot ( values , (1 / values ** 2) )
# plt . show ()

 #2.3
#for y=(1 / (2*(1 - x )))**(1/2) 
y = []
for i in range (100000) :
    x = np . random . random ()
    y . append ((1 / (2*(1 - x )))**(1/2) )

y . sort ()
ind = ( np . array ( y ) > 10) . tolist () . index (1)
y = y [: ind ]
bins = 100
binWidth = (max( y ) - min( y ) ) / bins
plt . hist (y , bins = bins , weights = np . ones (len ( y ) ) /( len ( y ) * binWidth ) )
values = np . linspace ( min( y ) , max( y ) , 50)
plt . plot ( values , (1 / values ** 3) )
plt . show ()

# for expected values
y = []
for j in range (10000) :
    x = np . random . random (10000)
    x=(1 / (2*(1 - x )))**(1/2) 
    y.append(np.mean(x))
print(y)
bins = 100
binWidth = (max( y ) - min( y ) ) / bins
plt . hist (y , bins = bins , weights = np . ones (len ( y ) ) /( len ( y ) * binWidth ) )
values = np . linspace ( min( y ) , max( y ) , 50)
plt . plot ( values , (1 / values ** 3) )
plt . show ()
