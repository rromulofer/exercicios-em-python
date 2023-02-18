# Autor: Rômulo Souza Fernandes
# E-mail: 00119110559@pq.uenf.br
# Data de criação: 17/02/23
# Curso em Vídeo

maior = 0
media = 0
menos = 0
soma = 0
nvelho = ''
for x in range(1, 4):
    print('----- {}ª PESSOA -----'.format(x))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: ')).strip()
    soma += idade
    if sexo in 'Ff' and idade < 20:
            menos += 1
    if x==1 and sexo in 'Mm':
            maior = idade
            nvelho = nome
    if sexo in 'Mm' and idade > maior:
        maior = idade
        nvelho = nome

media = soma/4
print('\nMédia de idade: {}'.format(media))
print('\n{} mulheres com menos de 20 anos'.format(menos))
print('\nO homem mais velho tem {} anos e se chama {}'.format(maior, nvelho))



