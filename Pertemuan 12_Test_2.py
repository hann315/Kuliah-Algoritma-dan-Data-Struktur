from cProfile import label
import matplotlib.pyplot as plt

x1 = [1, 2, 3]
y1 = [2, 4, 1]

plt.plot(x1, y1, label = 'Graph 1')

x2 = [1, 4, 5]
y2 = [2, 6, 4]

plt.plot(x2, y2, label = 'Graph 2')

plt.xlabel('Axis X')
plt.ylabel('Axis Y')

plt.title('Graph')

plt.legend()

plt.show()