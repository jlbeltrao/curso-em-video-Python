d = float(input('Quantos reais você tem? R$'))
USD = 3.27
print('Com R${:.2f} você pode comprar ${:.2f}.'.format(d, d/USD))