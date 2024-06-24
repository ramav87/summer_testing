import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1,1,100)

y = -3*x**3 +2 *x**2 +4

plt.figure()
plt.plot(x,y,'ko-')

