frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for cont in range(len(junto) -1, -1, -1):
    inverso += junto[cont]
print(inverso, junto)
if inverso == junto:
    print('A frase é um palindromo')
else:
    print('A frase não é um palindromo')
