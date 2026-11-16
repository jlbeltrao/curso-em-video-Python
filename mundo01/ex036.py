preco_casa = float(input('Digite o valor do imóvel: R$'))
salario = float(input('Digite seu salário: R$'))
prazo = int(input('Digite o prazo de pagamento (em anos): '))

prestacao = preco_casa / (prazo*12)

if prestacao >= salario * 0.3:
    print('O valor da prestação excedeu 30% da sua renda. Seu empréstimo foi negado.')
else:
    print('Seu emprestimo foi aprovado!')