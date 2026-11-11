preco = float(input('Insira o preço do produto: R$'))
desconto = 5
print('Aplicando {}% de desconto, o valor do produto cai para R${:.2f}.'.format(desconto, preco*(1-(desconto/100))))