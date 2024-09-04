#5. Crie uma lista de 10 nomes (informados dentro do programa). Em seguida, o usuário informa um número inteiro equivalente a um índice, e o programa retorna o nome equivalente ao índice informado pelo usuário.
nomes = ['Rafael', 'Gabriel', 'Pedro', 'Bruno', 'Gustavo', 'Alison', 'Diego', 'Marcia', 'Augusto', 'Patricia']
entrada = int(input('Informe um número de 0 a 9, será retornado um nome referente a esse índice: '))

try:
    indice = int(entrada)
    if 0<= indice <= len(nomes):
        print(f'O item no índice {indice} é {nomes[indice]}')
    else:
        print('Número fora do intervalo. Por favor, insira um índice válido.')
except:
    print('Entrada inválida')