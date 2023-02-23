# Autor: Rômulo Souza Fernandes
# E-mail: 00119110559@pq.uenf.br
# Data de criação: 23/02/23
# Curso em Vídeo

lista = list()
listaPar = list()
listaImp = list()


while True:
    lista.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break

for i, v in enumerate(lista):
    if v % 2 == 0:
        listaPar.append(v)
    else:
        listaImp.append(v)

print(f'Lista completa: {lista}')

print(f'Lista de números pares: {listaPar}')

print(f'Lista de números impares: {listaImp}')