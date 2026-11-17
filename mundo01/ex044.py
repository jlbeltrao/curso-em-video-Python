preco = float(input('Digite o preço do produto: R$'))

pag_a_vista_dinheiro = 0.9
pag_a_vista_cartao = 0.95
pag_parcelado_3x = 1.2

forma_pag = input('Qual a forma de pagamento? (A vista/Parcelado) ')

if forma_pag.lower() == 'parcelado':
    parcelas = int(input('Em quantas vezes deseja parcelar? '))
    if parcelas < 3:
        print('Condição de pagamento:\n{}x de R${:.2f}\nTotal: R${:.2f}'.format(parcelas, preco / parcelas, preco))
    else:
        print('Condição de pagamento:\n{}x de R${:.2f}\nTotal: R${:.2f}'.format(parcelas, (preco*pag_parcelado_3x) / parcelas, preco*pag_parcelado_3x))
elif forma_pag.lower() == 'a vista':
    print('Condição de pagamento:\nR${} a vista'.format(preco))