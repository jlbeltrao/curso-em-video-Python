salario = float(input('Digite seu salário: R$'))
aumento = 15
novosalario = (salario*(100+aumento))/100
print('Parabéns, você foi promovido e recebeu {}% de aumento. Seu novo salário é R${:.2f}.'.format(aumento, novosalario))