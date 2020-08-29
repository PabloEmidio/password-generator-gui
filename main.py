import PySimpleGUI as sg
from password import GerarSenha
import clipboard
from time import sleep

tamBottom = (1, 1)

sg.theme('DarkBrown')
layout = [[sg.T('tamanho da senha:', size=(15, 1)),
           sg.In(key='TOTAL', size=(3, 2), default_text='12',
                 enable_events=True, readonly=True, text_color='Black', ),
           sg.B('+', size=tamBottom, key='tot+'),
           sg.B('-', size=tamBottom, key='tot-')],

          [sg.T('Quantos numeros: ', size=(15, 1)),
           sg.In(key='NUMERO', size=(3, 2), default_text='3',
                 enable_events=True, readonly=True, text_color='Black', ),
           sg.B('+', size=tamBottom, key='NUM+'),
           sg.B('-', size=tamBottom, key='NUM-')],

          [sg.T('Quantos simbolos: ', size=(15, 1)),
           sg.In(key='SIMBOLO', size=(3, 2), default_text='3',
                 enable_events=True, readonly=True, text_color='Black'),
           sg.B('+', size=tamBottom, key='SIMB+'),
           sg.B('-', size=tamBottom, key='SIMB-')],

          [sg.T('Letras Maiusculas: ', size=(15, 1)),
           sg.In(key='MAIUSCULO', size=(3, 2), default_text='3',
                 enable_events=True, readonly=True, text_color='Black'),
           sg.B('+', size=tamBottom, key='MAIUS+'),
           sg.B('-', size=tamBottom, key='MAIUS-')],

          [sg.T('Letras Minusculas: ', size=(15, 1)),
           sg.In(key='MINUSCULO', size=(3, 2), default_text='3',
                 enable_events=True, readonly=True, text_color='Black'),
           sg.B('+', size=tamBottom, key='MINUS+'),
           sg.B('-', size=tamBottom, key='MINUS-')],

          [sg.Text()],
          [sg.B('GERAR', size=(5, 1))],
          [sg.In(key='RESP', size=(30, 2), default_text='',
                 enable_events=True, readonly=True, text_color='Black'), sg.B('Copiar Senha', key='COPIAR')],
          [sg.T('Gere senhas seguras', size=(30, 2), key='TEXT')]]

window = sg.Window('Gerador de Senhas', layout)

while True:

    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'EXIT':
        break

    # evento total
    if event == 'tot+':
        window['TOTAL'].update(int(values['TOTAL']) + 1)

    if event == 'tot-':
        if int(values['TOTAL']) - (int(values['NUMERO']) + int(values['SIMBOLO']) + int(values['MAIUSCULO']) + int(values['MINUSCULO'])) > 0:
            window['TOTAL'].update(int(values['TOTAL']) - 1)

    # evento numero
    if event == 'NUM+':
        if int(values['TOTAL']) - (int(values['NUMERO']) + int(values['SIMBOLO']) + int(values['MAIUSCULO']) + int(values['MINUSCULO'])) > 0:
            window['NUMERO'].update(int(values['NUMERO']) + 1)

    if event == 'NUM-':
        if int(values['NUMERO']) > 0:
            window['NUMERO'].update(int(values['NUMERO']) - 1)

    # evento simbolo
    if event == 'SIMB+':
        if int(values['TOTAL']) - (int(values['NUMERO']) + int(values['SIMBOLO']) + int(values['MAIUSCULO']) + int(values['MINUSCULO'])) > 0:
            window['SIMBOLO'].update(int(values['SIMBOLO']) + 1)

    if event == 'SIMB-':
        if int(values['SIMBOLO']) > 0:
            window['SIMBOLO'].update(int(values['SIMBOLO']) - 1)

    # evento letra maiuscula
    if event == 'MAIUS+':
        if int(values['TOTAL']) - (int(values['NUMERO']) + int(values['SIMBOLO']) + int(values['MAIUSCULO']) + int(values['MINUSCULO'])) > 0:
            window['MAIUSCULO'].update(int(values['MAIUSCULO']) + 1)

    if event == 'MAIUS-':
        if int(values['MAIUSCULO']) > 0:
            window['MAIUSCULO'].update(int(values['MAIUSCULO']) - 1)

    # evento letra maiuscula
    if event == 'MINUS+':
        if int(values['TOTAL']) - (int(values['NUMERO']) + int(values['SIMBOLO']) + int(values['MAIUSCULO']) + int(values['MINUSCULO'])) > 0:
            window['MINUSCULO'].update(int(values['MINUSCULO']) + 1)

    if event == 'MINUS-':
        if int(values['MINUSCULO']) > 0:
            window['MINUSCULO'].update(int(values['MINUSCULO']) - 1)

    # evento gerar a senha
    if event == 'GERAR':
        if int(values['TOTAL']) - (int(values['NUMERO']) + int(values['SIMBOLO']) + int(values['MAIUSCULO']) + int(values['MINUSCULO'])) > 0:
            sg.Popup(
                'Valores insuficientes\nAumente as variaveis ou dimunua o total')
        else:
            senha = GerarSenha(quantoNumero=int(values['NUMERO']), quantoSimbolo=int(
                values['SIMBOLO']), quantoMaiusculo=int(values['MAIUSCULO']), quantoMinusculo=int(values['MINUSCULO']))
            window['RESP'].update(senha)
        
        
    #copiar para a area de transferencia
    window['TEXT'].update('Gere senhas seguras') #volta para o valor padrão
    if event == 'COPIAR' and values['RESP']!= '':
        clipboard.copy(values['RESP'])
        window['TEXT'].update('Senha copiada para a area de transferencia')
    
        
window.close()
