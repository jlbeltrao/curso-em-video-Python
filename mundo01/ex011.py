print('Insira as dimensões da parede:')
h = float(input('Altura: '))
l = float(input('Largura: '))
m2 = h*l
rendtintam2 = 2
print('Uma parede de largura {:.2f} e altura {:.2f}, mede {:.2f}m². Serão necessários {} litros de tinta para pinta-la.'.format(h, l, m2, m2/rendtintam2))