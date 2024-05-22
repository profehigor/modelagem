import numpy as np
import matplotlib.pyplot as plt

# Parâmetros da circunferência
R = 5  # Raio da circunferência
a = -1  # Limite esquerdo da tira
b = 2   # Limite direito da tira

# Valores de x e y para a circunferência
theta = np.linspace(0, 2 * np.pi, 1000)
x = R * np.cos(theta)
y = R * np.sin(theta)

# Funções para os limites superior e inferior da tira
def y_upper(x):
    return np.sqrt(R**2 - x**2)

def y_lower(x):
    return -np.sqrt(R**2 - x**2)

# Valores de x para a tira
x_tira = np.linspace(a, b, 1000)
y_tira_upper = y_upper(x_tira)
y_tira_lower = y_lower(x_tira)

# Plotar a circunferência
plt.figure(figsize=(8, 8))
plt.plot(x, y, label='Circunferência')

# Preencher a tira
plt.fill_between(x_tira, y_tira_lower, y_tira_upper, color='lightblue', alpha=0.5, label='Tira vertical')

# Configurações do gráfico
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.gca().set_aspect('equal', adjustable='box')
plt.xlim(-R-1, R+1)
plt.ylim(-R-1, R+1)
plt.title('Tira Vertical da Circunferência')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
