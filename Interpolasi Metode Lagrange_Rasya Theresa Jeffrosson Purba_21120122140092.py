print("Rasya Theresa Jeffrosson Purba (21120122140092)")
print('    ')
print("Tugas Iterpolasi Metode Lagrange Metode Numerik Kelas B")

import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

x = np.array([5, 10, 15, 20, 25, 30, 35, 40])
y = np.array([40, 30, 25, 40, 18, 20, 25, 15])


class LagrangeInterpolator:
    def __init__(self, x_data, y_data):
        self.x_data = x_data
        self.y_data = y_data
    
    def interpolate(self, x):
        total = 0
        n = len(self.x_data)
        for i in range(n):
            term = self.y_data[i]
            for j in range(n):
                if j != i:
                    term *= (x - self.x_data[j]) / (self.x_data[i] - self.x_data[j])
            total += term
        return total

    def get_polynomial(self):
        x = sp.symbols('x')
        total = 0
        n = len(self.x_data)
        for i in range(n):
            term = self.y_data[i]
            for j in range(n):
                if j != i:
                    term *= (x - self.x_data[j]) / (self.x_data[i] - self.x_data[j])
            total += term
        return sp.simplify(total)
    
    def plot(self, x_test):
        y_test = [self.interpolate(xi) for xi in x_test]
        plt.plot(self.x_data, self.y_data, 'ro', label='Data points')
        plt.plot(x_test, y_test, label='Lagrange Interpolation')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.legend()
        plt.suptitle('Lagrange Interpolation Metode Numerik B')
        plt.title('By Rasya Theresa Jeffrosson Purba')
        plt.show()

# Main data
x = np.array([5, 10, 15, 20, 25, 30, 35, 40])
y = np.array([40, 30, 25, 40, 18, 20, 25, 15])

# Create interpolator
interpolator = LagrangeInterpolator(x, y)

# Get the polynomial expression
polynomial = interpolator.get_polynomial()
print(f"Interpolating Polynomial: {polynomial}")

# Plot the interpolation
x_test_points = np.linspace(5, 40, 100)
interpolator.plot(x_test_points)
