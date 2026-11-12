print('Insira as dimensões da parede:')
h = float(input('Altura: '))
l = float(input('Largura: '))
m2 = h*l
rend_tinta_m2 = 2
print('Uma parede de {:.2f}m de largura e {:.2f}m de altura mede {:.2f}m².\nSerão necessários {} litros de tinta para pinta-la.'.format(h, l, m2, m2/rend_tinta_m2))