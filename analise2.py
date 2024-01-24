import numpy as np


idades =  np.array([10,15,20,18])
notas = np.array([9,8,5,7])


print(notas[idades == 20])
#saida = 5 

print(np.mean(idades)) #media
#saida = 15.75

salario= np.array([[1000,1200,1300],[800,900,950],[2000,2100,2110]])
print(salario[1,2])
#saida = 950

  