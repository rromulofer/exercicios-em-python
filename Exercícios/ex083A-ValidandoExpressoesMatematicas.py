# Autor: Rômulo Souza Fernandes
# E-mail: 00119110559@pq.uenf.br
# Data de criação: 23/02/23
# Curso em Vídeo

pilha = list()

expr = str(input('Digite a expressão: '))

for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('A expressão é válida')
else:
    print('A expressão NÃO é válida')