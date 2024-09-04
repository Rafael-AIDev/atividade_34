#7. Crie um programa onde o usuário possa digitar uma lista de nomes (quantos ele quiser) e no final exiba a lista de nomes em ordem alfabética na tela, mostrando também o número de nomes digitado pelo usuário.
import os
nomes = ['Fulano']
nomes.sort()

while True:
    print('1 - Listar nomes cadastrados')
    print('2 - Cadastrar novo nome')
    print('3 - Sair do programa ')

    opcao = input('Opção do usuário: ')

    match opcao:
        case '1':
            nomes.sort()
            for i in range(len(nomes)):
                print(f'Nome de índice {i}: {nomes[i]}')
            continue
        case '2':
            novo_nome = input('Informe novo nome: ')
            nomes.append(novo_nome)
            print(f'Nome {novo_nome} cadastrado com sucesso')
            continue
        case '3':
            print('Programa encerrado ')
            break
        case _:
            print('Opção inválida')
            continue
        


    

    
    