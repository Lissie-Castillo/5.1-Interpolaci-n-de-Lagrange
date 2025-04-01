import numpy as np
import matplotlib.pyplot as plt

# Definición de los puntos de interpolación
x_points = np.array([2.0,4.0,6.0,8.0])
y_points = np.array([2500,2300,2150,2050])  
# Función de interpolación de Lagrange
def lagrange_interpolation(x, x_points, y_points):
    n = len(x_points)
    result = 0
    for i in range(n):
        term = y_points[i]
        for j in range(n):
            if i != j:                term *= (x - x_points[j]) / (x_points[i] - x_points[j])
        result += term
    return result

# Puntos para graficar la interpolación
x_values = np.linspace(min(x_points), max(x_points), 100)
y_values = [lagrange_interpolation(x, x_points, y_points) for x in x_values]


print(lagrange_interpolation(5, x_points, y_points))
# Graficar los puntos y la interpolación
plt.figure(figsize=(6,4))
plt.plot(x_values, y_values, label="Interpolación de Lagrange", color="blue")
plt.scatter(x_points, y_points, color="red", label="Puntos dados")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Interpolación de Lagrange")
plt.legend()
plt.grid(True)
plt.savefig("lagrange_interpolacion.png")
plt.show()