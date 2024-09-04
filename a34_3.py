#3. Crie um programa onde o usuário informa um número inteiro, e o programa informa se o número e par ou ímpar.
num = int(input('Digite um número inteiro'))
#  número dividido por 2 com resto zero é par
#  O operador de módulo(%) é utilizado para obter o resto da divisão.
resto = num % 2

if resto == 0:
    print('O número é par')
else:
    print('O número é ímpar')

