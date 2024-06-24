import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1,1,100)
y = 2*x**2 +3

plt.figure()
plt.plot(x,y,'ro-')
