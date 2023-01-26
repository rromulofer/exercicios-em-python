# Autor: Rômulo Souza Fernandes
# E-mail: 00119110559@pq.uenf.br
# Data de criação: 26/01/23
# Curso em Vídeo

lista = list()
n = 0

while n != 999:
    n = int(input('Digite um valor[999 para parar]: '))
    
    if n not in lista and n != 999:
        lista.append(n)
        print('Valor adicionado a lista')

lista.sort()

print(f'Lista completa digitada: {lista}')