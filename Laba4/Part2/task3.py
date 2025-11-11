import numpy as np
from scipy import linalg

def solve_system_equations(A, B):
    det_A = np.linalg.det(A)
    
    print(f"Определитель матрицы коэффициентов: {det_A}")

    if abs(det_A) < 1e-10:
        print("Матрица вырожденная, решение не существует")
        X = None
        return
    else:
        A_inv = linalg.inv(A)    # вычисляем обратную матрицу
    
        X = np.dot(A_inv, B)        # вычисляем вектор-решение системы
    
        return X

if __name__ == "__main__":

    A = np.array([
    [-2, -8.5, -3.4, 3.5],
    [0, 2.4, 0, 8.2],
    [2.5, 1.6, 2.1, 3],
    [0.3, -0.4, -4.8, 4.6]
                ])
    
    B = np.array([-1.88, -3.28, -0.5, -2.83])

    result = solve_system_equations(A, B)

    if result.any():
        print("\nРешение системы:")
        print(f"X = {np.round(result, 1)}")

    