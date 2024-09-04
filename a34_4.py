# 4. Crie um programa que o usuário informa um número inteiro positivo, e o programa exibe na tela uma contagem regressiva.
import os
import time
num = int(input('Digite un número interito positivo: '))

while num >= 0:
    os.system('cls')
    print('\nContagem regressiva:')
    print(f'{num}...')
    num -= 1
    time.sleep(1)

os.system('cls')
print('KABUMMM')