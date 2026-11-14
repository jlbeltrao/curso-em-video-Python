""" num = input('Informe um número: ')
print('Unidade: {}'.format(list(num)[-1]))
print('Dezena: {}'.format(list(num)[-2]))
print('Centena: {}'.format(list(num)[-3]))
print('Milhar: {}'.format(list(num)[-4])) """

num = int(input('Informe um número: '))
print('Unidade: {}'.format(num // 1) % 10)
print('Dezena: {}'.format((num // 10) % 10))
print('Centena: {}'.format((num // 100) % 10))
print('Milhar: {}'.format((num // 1000) % 10))
