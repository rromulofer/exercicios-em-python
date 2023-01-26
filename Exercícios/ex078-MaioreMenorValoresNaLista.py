# Autor: Rômulo Souza Fernandes
# E-mail: 00119110559@pq.uenf.br
# Data de criação: 25/01/23
# Curso em Vídeo

valores  = []
maior = 0
menor = 0

for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
    if (cont == 0):
        maior = menor = valores[cont]

for cont in range(0, 5):
    if valores[cont] > maior:
        maior = valores[cont]
    elif valores[cont] < menor:
        menor = valores[menor]

print('Maior: {}, menor: {}'.format(maior, menor))
print('Valores digitados: {}'.format(valores))