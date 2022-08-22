import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,8,5,7,])
y = np.array([3,10,4,6])

# 'o' represent ring ...only shows points 
plt.plot(x,y,'o')
plt.show()

# you can draw multiple line 

plt.plot(x,y)
plt.show()

