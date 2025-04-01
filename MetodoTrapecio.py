"""
           Autor:
   Juan Pablo Buitrago Rios
   juanybrisagames@gmail.com
   Version 2.0 : 26/03/2025 11:50pm

"""

import numpy as np
import matplotlib.pyplot as plt

# Definimos la función a integrar
def f(x):
    return np.sin(x) #Ejercicio 3
    #return np.exp(-x**2) #Ejercicio 2
    #return x**2+3*x+1 #Ejercicio 1
    #return x**2+1 #ejercicio de ejemplo

# Implementación de la regla del trapecio
def trapezoidal_rule(a, b, n):
    x = np.linspace(a, b, n+1)  # Puntos equidistantes
    y = f(x)
    h = (b - a) / n
    integral = (h / 2) * (y[0] + 2 * sum(y[1:n]) + y[n])  # Regla del trapecio compuesta
    return integral, x, y
#Parametros de ejercicio 1
#a,b = 0, 2
#n = 50 # 10 20 50
#Parametros de ejercicio 2
#a,b = 1, 4
#n = 15 # 5 10 15
#Parametros de ejercicio 3
a,b = 0, np.pi
n = 100# 20 40 60
# Parámetros de integración ejercicio de ejemplo
#a, b = 0, 2  # Intervalo de integración
#n = 4  # Número de subdivisiones

# Cálculo de la integral
integral_approx, x_vals, y_vals = trapezoidal_rule(a, b, n)

# Imprimir el resultado de la integral aproximada
print(f"Integral aproximada con la regla del trapecio: {integral_approx:.6f}")

# Gráfica de la función y la aproximación por trapecios
x_fine = np.linspace(a, b, 100)
y_fine = f(x_fine)

plt.figure(figsize=(8, 5))
plt.plot(x_fine, y_fine, 'r-', label=r'$f(x) = sin(x)', linewidth=2) #Ejercicios de ejemplo: r'$f(x) = x^2+1$'  Ejercicio 1: r'$f(x) = x^2 + 3x + 1$'  Ejercicio 2: r'$f(x) = e^-x^2$' '
plt.fill_between(x_vals, y_vals, alpha=0.3, color='blue', label="Aproximación Trapecios")
plt.plot(x_vals, y_vals, 'bo-', label="Puntos de integración")

# Etiquetas y leyenda
plt.xlabel("$x$")
plt.ylabel("$f(x)$")
plt.title("Aproximación de la integral con la regla del trapecio")
plt.legend()
plt.grid()

# Guardar la figura
plt.savefig("trapecio.png")
plt.show()