import matplotlib.pyplot as plt
import numpy as np

time = np.arange(0, 10, 0.01)
y = np.sin(time)

plt.figure('sin 그래프')
plt.plot(time, y)
plt.show()
