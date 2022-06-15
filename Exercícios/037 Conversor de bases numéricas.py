n = int(input('Digite um número: '))
print('''Opções: 
1-Binário
2-Octal
3-Hexadecimal''')
opcao = int(input('Digite uma opção: '))
if opcao == 1:
    print('Conversão para binário: {}'.format(bin(n)[2:]))
elif opcao == 2:
    print('Conversão para octal: {}'.format(oct(n)[2:]))
elif opcao == 3:
    print('Conversão para hexadecimal: {}'.format(hex(n)[2:]))
else:
    print('---Opção inválida---')