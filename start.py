import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1,1,100)
y = 5*x**4 -5*x**2 +3

plt.figure()
plt.scatter(x,y)
