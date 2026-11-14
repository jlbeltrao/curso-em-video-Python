""" nome = str(input('Qual é o seu nome? '))
if nome == 'Jose':
    print('Que nome lindo você tem!')
else:
    print('Sua nome é tão normal...')
print('Bom dia, {}!'.format(nome)) """

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
""" print('A sua média foi {}.'.format(m))
if m >= 6:
    print('Sua média foi boa.')
else:
    print('Sua média foi ruim! Estude mais!') """
print('Parabéns' if m >= 6 else 'Estude mais!')