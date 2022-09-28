#Contrução da Matriz 1 e Matriz 2 - Programa Principal
import random

def somaMatrizes(matriz1, matriz2):
    if(len(matriz1) != len(matriz2) or len(matriz1[0]) != len(matriz2[0])):
        return None
    result = []
    for i in range(len(matriz1)):
        result.append([])
        for j in range(len(matriz1[0])):
            result[i].append(matriz1[i][j] + matriz2[i][j])
    return result

def produtoMatrizes(matriz1, matriz2):
    if(len(matriz1) != len(matriz2) or len(matriz1[0]) != len(matriz2[0])):
        return None
    result = []
    for i in range(len(matriz1)):
        result.append([])
        for j in range(len(matriz1[0])):
            result[i].append(matriz1[i][j] * matriz2[i][j])
    return result

matriz1 = []

n = int(input("Informe a quantidade de linhas\n da matriz 1:" ))
m = int(input("Informe a quantidade de colunas\n da matriz 1:" ))
for i in range(n):
     matriz1.append([])
     for j in range(m):
        matriz1[i].append(random.randint(0,100))

for i in range(len(matriz1)):
    for j in range(len(matriz1[i])):
        print(matriz1[i][j], end=" ")
    print ("\n")


matriz2 = []
n = int(input("Informe a quantidade de linhas\n da matriz 2:" ))
m = int(input("Informe a quantidade de colunas\n da matriz 2:" ))

for i in range(n):
     matriz2.append([])
     for j in range(m):
        matriz2[i].append(random.randint(0,100))

for i in range(len(matriz2)):
    for j in range(len(matriz2[i])):
        print(matriz2[i][j], end=" ")
    print ("\n")

soma = somaMatrizes(matriz1, matriz2)
produto = produtoMatrizes(matriz1, matriz2)

if soma is not None:
    for i in soma:
        print(i)
else:
    print('Matrizes devem conter o mesmo numero de linhas e colunas')

print('\n\n')

if produto is not None:
    for i in produto:
        print(i)
else:
    print('Matrizes devem conter o mesmo numero de linhas e colunas')