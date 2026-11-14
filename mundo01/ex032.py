ano = int(input('Digite o ano: '))

if ano % 4 == 0:
    print('O ano {} é bisexto.'.format(ano))
else:
    print('O ano {} não é bisexto'.format(ano))