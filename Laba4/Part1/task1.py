# импортируем библиотеку NumPy
import numpy as np
# импортируем из matplotlib pyplot
import matplotlib.pyplot as plt

x_degrees = np.linspace(-360, 360, 100)
x_radians = np.radians(x_degrees)

f = np.exp(np.cos(x_radians)) + np.log(np.power(np.cos(0.6 * x_radians), 2) + 1) + np.sin(x_radians)
h = -np.log((np.cos(x_radians) + np.sin(x_radians))**2 + 2.5) + 10

plt.plot(x_degrees, f, label="f(x)", color="blue")
plt.plot(x_degrees, h, label="h(x)", color="orange")
plt.xticks(np.arange(-360, 361, 90))
plt.xlim(-360, 360)
plt.xlabel("x, градусы", fontsize = 12)
plt.ylabel("y", fontsize = 12)
plt.title("Графики функций f(x) и h(x) на интервале [-360°, 360°]", fontsize = 14) 
plt.legend()
plt.show()