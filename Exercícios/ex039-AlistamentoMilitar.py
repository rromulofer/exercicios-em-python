ano = int(input('Digite o ano em que você nasceu: '))
idade = 2020-ano


if ano>1920 and ano<2021:
    if idade<18 and idade>0:
        falta = 18 - idade
        anoali = 2020+falta
        print('Você tem {}, faltam {} anos para o seu alistamento, será no ano {} '.format(idade, falta, anoali))
    elif idade==18:
        print('Você tem {} anos e precisa se alistar esse ano!'.format(idade))
    elif idade>18:
        print('Você tem {} anos e já passou da hora de se alistar!'.format(idade))
else:
    print('---Ano incompatível---')
