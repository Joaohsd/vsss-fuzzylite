import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Cria grades de valores para d e Δd
d = np.linspace(1, 2000, 100)
delta_d = np.linspace(-100, 100, 100)

# Cria uma matriz de valores da função usando d e Δd
D, Delta_D = np.meshgrid(d, delta_d)

# Ajusta a influência da distância (d) com uma sigmoid
k_d = 0.005  # Ajuste o coeficiente para controlar a inclinação da sigmoid
f_d = 1 / (1 + np.exp(-k_d * (D - 400)))  # A sigmoid é centrada em d = 500

# Ajuste a influência da variação da distância (Δd) com outra sigmoid
k_delta_d = 0.02  # Ajuste o coeficiente para controlar a inclinação da sigmoid
f_delta_d = 1 / (1 + np.exp(-k_delta_d * Delta_D**2))

# Combina as influências de d e Δd
f = f_d * f_delta_d

# Reajusta o conjunto imagem para [0, 1]
f_min = f.min()
f_max = f.max()
f_scaled = (f - f_min) / (f_max - f_min)

# Plota a influência de ambas as variáveis em um gráfico 3D
print(D.shape)

print(Delta_D.shape)

print(f_scaled.shape)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(D, Delta_D, f_scaled, cmap='viridis')
ax.set_xlabel('Distância (d)')
ax.set_ylabel('Variação da Distância (Δd)')
ax.set_zlabel('Função (f)')
plt.title('Influência de d e Δd na Função')
plt.show()
