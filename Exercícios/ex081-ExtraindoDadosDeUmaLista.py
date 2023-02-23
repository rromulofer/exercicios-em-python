# Autor: Rômulo Souza Fernandes
# E-mail: 00119110559@pq.uenf.br
# Data de criação: 23/02/23
# Curso em Vídeo

lista = list()
n = 0
cont = 0
verifica = 0

while n != 999:
    n = int(input('Digite um valor[999 para parar]: '))
    
    if n == 5:
        verifica += 1

    if n not in lista and n != 999:
        lista.append(n)
        print('Valor adicionado a lista')
        cont += 1

lista.sort(reverse=True)

print(f'\n\nQuantidade de valores digitados: {cont}')
print(f'\nLista completa de forma decrescente: {lista}\n')

if verifica > 0:
    print('O número 5 foi digitado e está na lista\n')
