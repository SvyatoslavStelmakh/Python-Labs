# импортируем библиотеку NumPy
import numpy as np
# импортируем из matplotlib pyplot
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 1000)
y = 5 / (x**2 - 9)

plt.plot(x, y, label="f(x)", color="blue", linewidth = 2)
plt.xticks(np.arange(-10, 11, 1))
plt.xlim(-10, 10)

plt.xlabel("x", fontsize = 12)
plt.ylabel("y", fontsize = 12)
plt.title("График функции f(x) на интервале [-10, 10]", fontsize = 14) 
plt.legend(fontsize = 10)
plt.show()