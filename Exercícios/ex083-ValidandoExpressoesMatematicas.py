# Autor: Rômulo Souza Fernandes
# E-mail: 00119110559@pq.uenf.br
# Data de criação: 23/02/23
# Curso em Vídeo

pilha = list()
abre = 0
fecha = 0 

expr = str(input('Digite a expressão: '))

for simb in expr:
    if simb == '(':
        abre += 1
    elif simb == ')':
        fecha += 1

if abre == fecha:
    print('A expressão é válida')
else:
    print('A expressão NÃO é válida')