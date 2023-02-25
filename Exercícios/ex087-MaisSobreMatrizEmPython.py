# Autor: Rômulo Souza Fernandes
# E-mail: 00119110559@pq.uenf.br
# Data de criação: 25/02/23
# Curso em Vídeo

# Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
#     A) A soma de todos os valores pares digitados.
#         B) A soma dos valores da terceira coluna. 
#             C) O maior valor da segunda linha.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somaP = 0
somaC = 0
maior = 0

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para a posição [{linha}], [{coluna}]: '))
        # Questão A
        if ((matriz[linha][coluna]) % 2) == 0:
            somaP += matriz[linha][coluna]
        # Questão B
        if matriz[linha][2]:
            somaC += matriz[linha][2]
        # Questão C
        if matriz[1][coluna]:
            if coluna == 0:
                maior = matriz[1][coluna]
            elif matriz[1][coluna] > maior:
                maior = matriz[1][coluna]

print('-=' * 30)

for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]}]', end='')
    print()

print(f'Soma dos valores pares: {somaP}')

print(f'Soma dos valores da terceira coluna: {somaC}')


print(f'Maior valor da segunda linha: {maior}')