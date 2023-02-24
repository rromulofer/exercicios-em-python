# Autor: Rômulo Souza Fernandes
# E-mail: 00119110559@pq.uenf.br
# Data de criação: 24/02/23
# Curso em Vídeo

# Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e 
# cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, 
# mostre os valores pares e ímpares em ordem crescente.

lista = [[], []]
valor = 0

for n in range(0, 7):
    valor = int(input('Digite um valor: '))
    if valor % 2 == 0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)

print(f'Valores pares: {lista[0]}')

print(f'Valores impares: {lista[1]}')

