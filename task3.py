import numpy as np
import matplotlib.pyplot as plt

# создаем переменные
m = 1
omega = np.sqrt(1 / m)
gamma = 0.2 * omega
u0, v0 = 1, 0
stop = 8

t = np.linspace(stop, 50, 500)
u1 = np.exp(-gamma / (2 * m) * t)
u2 = np.cos(omega * np.sqrt(1 - (gamma / (2 * m * omega)) ** 2) * t)
u3 = np.sin(omega * np.sqrt(1 - (gamma / (2 * m * omega)) ** 2) * t)
u = u1 * (u0 * u2 + (v0 + gamma / (2 * m) * u0) * u3)
t_stop = np.insert(t, 0, np.linspace(1, stop, stop//1))
u_stop = np.insert(u, 0, [0] * stop)

plt.plot(t_stop, u_stop)
plt.plot([stop, stop], [-1, 1], 'r--')
plt.xlabel('Время, с')
plt.ylabel('Смещение, м')
plt.show()