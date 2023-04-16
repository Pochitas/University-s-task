import numpy as np
import matplotlib.pyplot as plt

# создаем переменные
x0 = 1
v0 = 0
omega = 2

t = np.linspace(0, 10, 100)
x = x0 * np.cos(omega * t) + v0 / omega * np.sin(omega * t)

plt.plot(t, x)
plt.xlabel('Время С.')
plt.ylabel('Смещение М.')
plt.show()