try:
    salario = float(input('Digite salário do funcionário: R$'))
    if salario <= 1250:
        print('O salário de R${:.2f} será aplicado um aumento de 15%. O novo salário é de R${:.2f}.'.format(salario, salario*1.15))
    elif salario > 1250:
        print('O salário de R${:.2f} será aplicado um aumento de 10%. O novo salário é de R${:.2f}.'.format(salario, salario*1.1))

except ValueError:
    print('Digite um valor válido.')