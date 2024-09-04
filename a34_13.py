# importa bibliotecas
import pyautogui
import time

# tempo que cada comando demora para executar
pyautogui.PAUSE = 1

# instruções
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')

# espera 10 segundos para abrir o vscode e continuar com os comandos
time.sleep(10)

# continua as instruções
pyautogui.hotkey('ctrl', 'shift', "'")
pyautogui.write('youtube')
pyautogui.press('enter')

for i in range(4):
