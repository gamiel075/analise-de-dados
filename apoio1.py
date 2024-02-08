

#estudo gráfico de dispensão

import matplotlib.pyplot as plt

# Dados de exemplo
horas_estudo = [2, 3, 5, 1, 4, 6, 7, 8, 9, 10]
notas_prova = [60, 65, 75, 50, 70, 80, 85, 90, 92, 95]

# Criar o gráfico de dispersão
plt.scatter(horas_estudo, notas_prova)

# Adicionar rótulos aos eixos e título
plt.xlabel('Horas de Estudo')
plt.ylabel('Notas na Prova')
plt.title('Relação entre Horas de Estudo e Notas na Prova')

# Exibir o gráfico
plt.show()

#Aqui podemos estabelecer uma relalção quanto mais o estudante estuda mais boas notas ele tira

import matplotlib.pyplot as plt
import numpy as np

# Dados fictícios
horas_atividade_fisica = [2, 3, 4, 2.5, 3.5, 5, 1.5, 4, 6, 7]
consumo_calorias = [200, 250, 300, 220, 320, 400, 180, 350, 500, 600]
peso_perdido = [1, 1.5, 2, 1.2, 2.5, 3, 0.8, 2.8, 3.5, 4]

# Criar o gráfico de dispersão
plt.figure(figsize=(10, 6))
plt.scatter(horas_atividade_fisica, consumo_calorias, c=peso_perdido, cmap='viridis', s=100, alpha=0.8)

# Adicionar barra de cores e legendas
barra_cores = plt.colorbar()
barra_cores.set_label('Peso Perdido (kg)')

# Adicionar rótulos aos eixos e título
plt.xlabel('Horas de Atividade Física')
plt.ylabel('Consumo de Calorias (kcal)')
plt.title('Relação entre Atividade Física, Consumo de Calorias e Peso Perdido')

# Exibir o gráfico
plt.show()

#Aqui temos a relação entre horas de exercicio e quantidade de calorias perdidas(usando cores)
