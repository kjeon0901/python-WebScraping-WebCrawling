import matplotlib.pyplot as plt

data1 = [10, 20, 30, 5]
data2 = [5, 10, 15, 2.5]

x = [1, 2, 3, 4]

plt.bar(x, data1, width = 0.3)
plt.bar(x, data2, bottom=data1, width = 0.3)

plt.show()
