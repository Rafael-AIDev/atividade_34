# 11. Crie um programa com funções para calcular a área de 4 figuras geométricas (quadrado, círculo, triângulo e trapézio).
def mostrar_menu():
    print('1 - Calcular quadrilátero.')
    print('2 - Calcular triângulo.')
    print('3 - Calcular círculo.')
    print('4 - Calcular trapézio')
    print('5 - Sair do programa.')

def calcular_quadrilatero(b, h):
    result = b * h
    return result

def calcular_triangulo(b, h):
    result = (b * h)/2
    return result

def calcular_circulo(r):
    result = 3.14*r**2
    return result

def calcular_trapezio(d, b, h):
    result = ((d + b) * h)/2
    return result

# programa principal
while True: 

    mostrar_menu()

    opcao = input('Opção desejada: ')

    match opcao: 
        case '1':
            b = str(input('Informe o valor da base: ')).replace(',', '.')
            h = str(input('Informe o valor da altura: ')).replace(',', '.')
            b = float(b)
            h = float(h)
            print(f'Área do quadrilátero:  {calcular_quadrilatero(b, h)}')
            continue
        case '2':
            b = str(input('Informe o valor da base: ')).replace(',', '.')
            h = str(input('Informe o valor da altura: ')).replace(',', '.')
            b = float(b)
            h = float(h)
            print(f'Área do triângulo:  {calcular_triangulo(b, h)}')
            continue
        case '3':
            r = str(input('Informe o valor do raio: ')).replace(',', '.')
            r = float(r)
            print(f'Área do círculo:  {calcular_circulo(r)}')
            continue
        case '4':
            d = str(input('Informe o valor da base maior: ')).replace(',', '.')
            b = str(input('Informe o valor da base menor: ')).replace(',', '.')
            h = str(input('Informe o valor da altura: ')).replace(',', '.')
            d = float(d)
            b = float(b)
            h = float(h)
            print(f'Área do triângulo:  {calcular_triangulo(d ,b, h)}')
            continue

        case 5:
            print('Programa encerrado')
            break
        case _:
            print('Opção inválida')
            continue