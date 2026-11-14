import random

num_aleatorio = random.randint(1, 5)
num = int(input('Digite um número: '))

""" if num == num_aleatorio:
    print('Você venceu!')
else:
    print('Você perdeu!') """

print('Você venceu!' if num == num_aleatorio else 'Você perdeu!')