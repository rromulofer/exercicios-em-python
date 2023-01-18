from random import randint
n = (randint(1, 10), randint(1, 10), randint(1, 10),
     randint(1, 10), randint(1, 10),)
print('Números gerados:', end='')
for cont in n:
    print(f'{cont}', end='')
print(f'\nO maior valor gerado foi {max(n)}')
print(f'O maior valor gerado foi {min(n)}')