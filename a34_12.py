# 12. Crie um programa que traduza qualquer texto em qualquer idioma para o português.
from deep_translator import GoogleTranslator

tradutor = GoogleTranslator(source= 'auto', target = 'pt')

while True:
    texto_usuario = input('Digite o que deseja traduzir, idioma sua escolha: ')
    traducao = tradutor.translate(texto_usuario)

    print(traducao)

    repetir = input('Deseja fazer mais uma tradução (s/n)? ').lower()

    if repetir == 's':
        continue
    else:
        break