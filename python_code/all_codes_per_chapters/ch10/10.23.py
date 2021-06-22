import matplotlib.pyplot as plt
import numpy as np

time = np.arange(0, 10, 0.01)
sin_y = np.sin(time)
cos_y = np.cos(time)

plt.figure('sin, cos 그래프')
plt.plot(time, sin_y)
plt.plot(time, cos_y)
plt.show()
