import matplotlib.pyplot as plt

x = [2, 3, 5, 8, 13, 16]
y = [2, 3, 6, 3, 3, 16]

plt.plot(x, y, label='Line 1')

x1 = [2, 3, 5, 8, 18]
y1 = [4, 4, 7, 14, 17]

plt.plot(x1, y1, label='Line2', color='green', linestyle='dashed',
         linewidth=2, marker='o', markerfacecolor='red', markersize=4)

plt.ylim(1, 20)
plt.xlim(1, 20)

plt.xlabel('X Axis')
plt.ylabel('Y Axis')

plt.title('Demo Graph')

plt.legend()

plt.show()
