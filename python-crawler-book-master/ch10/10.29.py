import matplotlib.pyplot as plt

data = [10, 20, 30, 5]
labels = ['A', 'B', 'C', 'D']

plt.pie(data, labels=labels, startangle=90, autopct='%1.1f%%')
plt.show()
