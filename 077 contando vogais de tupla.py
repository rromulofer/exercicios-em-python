palavras = ('mesa', 'cadeira', 'fogao', 'geladeira')

for palavra in palavras:
    print(f'A palavra {palavra} tem as vogais: ', end = '')
    for letra in palavra:
        if letra in 'aeiou':
            print(f'{letra}', end = ' ')
    print('\n')
