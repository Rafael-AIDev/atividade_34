###1. Crie um programa que peça para que o usuário digite um número, em seguida o converta para float, exibindo em tela tanto o número em si quanto seu tipo de dado.
num = input('Digite um número: ').replace(',', '.')
num = float(num)
mensagem = print(f'O número dgitado é {num} do tipo')
print(type(num))