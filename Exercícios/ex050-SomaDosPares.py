# Autor: Rômulo Souza Fernandes
# E-mail: 00119110559@pq.uenf.br
# Data de criação: 24/01/23
# Curso em Vídeo

# O programa soma apenas os números pares digitados

soma = 0
cont = 0

for x in range(1, 7):
    n = int(input('Digite um valor: '))
    
    if n % 2 == 0:
        soma += n
        cont += 1

print('Você digitou {} números pares! '.format(cont))
print('Soma dos números pares: {}'.format(soma))