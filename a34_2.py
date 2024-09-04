# 2. Crie um programa que receba o peso (em gramas) de um bebê recém-nascido, e indique se o bebê está normal ou se precisa ficar internado, caso o bebê tenha menos que 2500g.
bebe = input('Digite o peso do bebê em gramas: ').replace(',', '.')
bebe = float(bebe)
if bebe < 2500:
    print('O peso do bebê está abaixo do ideal, precisará de internação')
else:
    print('O peso do bebê está normal')