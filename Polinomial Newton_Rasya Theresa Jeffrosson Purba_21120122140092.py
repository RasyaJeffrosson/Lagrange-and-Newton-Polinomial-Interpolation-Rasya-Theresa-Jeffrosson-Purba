print("Rasya Theresa Jeffrosson Purba (21120122140092)")
print('    ')
print("Tugas Iterpolasi Metode Newton Polinomial Metode Numerik Kelas B")


import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

class NewtonInterpolator:
    def __init__(self, x_points, y_points):
        self.x_points = x_points
        self.y_points = y_points
        self.divided_differences = self.compute_divided_differences()
    
    def compute_divided_differences(self):
        n = len(self.x_points)
        table = np.zeros((n, n))
        table[:, 0] = self.y_points
        for j in range(1, n):
            for i in range(n - j):
                table[i, j] = (table[i + 1, j - 1] - table[i, j - 1]) / (self.x_points[i + j] - self.x_points[i])
        return table[0, :]
    
    def interpolate(self, x):
        n = len(self.x_points)
        result = self.divided_differences[0]
        for i in range(1, n):
            term = self.divided_differences[i]
            for j in range(i):
                term *= (x - self.x_points[j])
            result += term
        return result

    def get_polynomial(self):
        x = sp.symbols('x')
        n = len(self.x_points)
        polynomial = self.divided_differences[0]
        for i in range(1, n):
            term = self.divided_differences[i]
            for j in range(i):
                term *= (x - self.x_points[j])
            polynomial += term
        return sp.simplify(polynomial)
    
    def plot(self, x_values):
        y_values = [self.interpolate(xi) for xi in x_values]
        plt.plot(self.x_points, self.y_points, 'ro', label='Data points')
        plt.plot(x_values, y_values, label='Newton Interpolation')
        plt.xlabel('Stress (kg/mm^2)')
        plt.ylabel('Time to Failure (hours)')
        plt.legend()
        plt.suptitle('Newton Interpolation Metode Numerik B')
        plt.title("By Rasya Theresa Jeffrosson Purba")
        plt.show()

# Data points
stress = np.array([5, 10, 15, 20, 25, 30, 35, 40])
time_to_failure = np.array([40, 30, 25, 40, 18, 20, 22, 15])

# Newton Interpolation
newton_test_points = np.linspace(5, 40, 100)
newton_interpolator = NewtonInterpolator(stress, time_to_failure)
newton_interpolator.plot(newton_test_points)

# Polynomial function from Newton interpolation
newton_polynomial = newton_interpolator.get_polynomial()
print(f"Newton Interpolation Polynomial:\n {newton_polynomial.expand()}")
