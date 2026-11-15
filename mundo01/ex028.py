import random
import time
num_aleatorio = random.randint(0, 5)
print('-='*30)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-='*30)
num = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
time.sleep(2)
print('Você venceu!' if num == num_aleatorio else 'Você perdeu! Eu pensei no número {}'.format(num_aleatorio))