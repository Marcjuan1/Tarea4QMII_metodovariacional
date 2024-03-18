import numpy as np
import matplotlib.pyplot as plt

# Definición del potencial
def potential(x, V0, beta):
    return V0 * (beta**2 / x**2 - beta / (2 * x))

# Definición de la función de onda
def wave_function(x, alpha):
    return (2 * alpha**(5/4)) / (np.sqrt(3) * np.sqrt(np.pi / 2)) * x**2 * np.exp(-alpha * x**2)

# Parámetros del potencial
V0 = 1.0  # Constante V0
beta = 1.0  # Constante beta

# Rango de valores de x para graficar
x_values = np.linspace(-5, 5, 400)  # Evita dividir por cero en x = 0

# Calcular el potencial para cada valor de x
V_values = potential(x_values, V0, beta)

# Calcular la función de onda para cada valor de x
alpha = 1  # Valor de alpha para la función de onda
psi_values = wave_function(x_values, alpha)

# Graficar el potencial y la función de onda
plt.figure(figsize=(8, 6))
plt.plot(x_values, V_values, label=r'$V(x) = V_0 \left( \frac{\beta^2}{x^2} - \frac{\beta}{2x} \right)$', color='b')
plt.plot(x_values, psi_values, label=r'$\psi(x)$', color='r', linestyle='--')
plt.title('Potencial $V(x)$ y función de onda $\psi(x)$')
plt.xlabel('$x$')
plt.ylabel('Magnitud')
plt.grid(True)
plt.legend()
plt.show()
