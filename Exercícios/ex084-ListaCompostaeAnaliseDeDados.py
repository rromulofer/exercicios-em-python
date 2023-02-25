# Autor: Rômulo Souza Fernandes
# E-mail: 00119110559@pq.uenf.br
# Data de criação: 24/02/23
# Curso em Vídeo

# Exercício Python 084: Faça um programa que leia nome e peso de várias
# pessoas, guardando tudo em uma lista. No final, mostre:
#   A) Quantas pessoas foram cadastradas.
#       B) Uma listagem com as pessoas mais pesadas.
#           C) Uma listagem com as pessoas mais leves.

pessoa = list()
lista_pessoas = list()
maior = menor = 0

while True:
    pessoa.append(str(input('Digite o nome: ')))
    pessoa.append(str(input('Digite a o peso: ')))

    if len(lista_pessoas) == 0:
        maior = menor = pessoa[1]
    else:
        if pessoa[1] > maior:
            maior = pessoa[1]
        if pessoa[1] < menor:
            menor = pessoa[1]

    lista_pessoas.append(pessoa[:])
    pessoa.clear()

    resp = str(input('Deseja continuar? [S/N]'))

    if resp in 'Nn':
        break

print(lista_pessoas)

print(f'Foram cadastradas {len(lista_pessoas)} pessoas')

print(f'O maior peso foi de {maior}Kg. Peso de ', end='')

for p in lista_pessoas:
    if p[1] == maior:
        print(f'[{p[0]}]', end='')

print()

print(f'O menor peso foi de {menor}Kg. Peso de ', end='')

for p in lista_pessoas:
    if p[1] == menor:
        print(f'[{p[0]}]', end='')

print()
