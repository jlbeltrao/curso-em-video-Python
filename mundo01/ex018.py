import math

angulo = float(input('DIgite o angulo que você deseja: '))

print('Para o angulo de {:.3f}º temos:\nSeno: {:.3f}\nCosseno: {:.3f}\nTangente: {:.3f}'.format(angulo, math.sin(math.radians(angulo)), math.cos(math.radians(angulo)), math.tan(math.radians(angulo))))