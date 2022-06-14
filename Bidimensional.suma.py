import random as rng
import numpy as np

arreglo_a = np.array([[1,2,3],[4,5,6],[7,8,9]])
arreglo_b = np.array([[9,8,7],[6,5,4],[3,2,1]])
arreglo_suma = np.array([[],[],[]])

for i in range(3):
    for j in range(3):
        arreglo_suma = np.matmul(arreglo_a, arreglo_b)

# print(arreglo_a)
# print(arreglo_b)
print(arreglo_suma)