import numpy as np
from scipy import integrate

print("\n1. Первый интеграл")
print("∫ от π/2 до π [sin(x)/(cos²(x) + 1)] dx")

def func1(x):
    return np.sin(x) / (np.cos(x)**2 + 1)

result1, error1 = integrate.quad(func1, np.pi/2, np.pi)
analytical1 = np.pi/4

print(f"\nРезультат: {result1:.8f}")
print(f"Погрешность: {error1:.2e}")
print(f"Аналитический результат: :{analytical1:.8f}")

print("\n2. Второй интеграл")
print("\∫ от 0 до 1 ∫ от x^2 до x [xy²] dy dx")
def func2(y, x):
    return x * y**2

result2, error2 = integrate.dblquad(func2, 0, 1, lambda x: x**2, lambda x: x)
analytical2 = 1/40

print(f"\nРезультат: {result2:.8f}")
print(f"Погрешность: {error2:.2e}")
print(f"Аналитически: {analytical2:.8f}")
