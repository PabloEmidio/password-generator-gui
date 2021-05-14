import PySimpleGUI as sg
from password import gerador_de_senhas as gerador
import clipboard

tamBottom = (1, 1)
sg.theme('DarkBrown')
layout = [
    [sg.T('Digita a frase:'), sg.In(
        key='FRASE', text_color='Black', readonly=True)],
    [sg.Checkbox(text='Gerar senha por frase', key='MODE',
                 enable_events=True, pad=(('280', '3'), ('5', '20')))],
    [sg.T('_'*60, text_color='Silver')],
    [sg.T('tamanho da senha:', size=(15, 1)),
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
    [sg.B('GERAR', size=(5, 1)), sg.T('', size=(30, 1), key='OUT')],
    [sg.In(key='RESP', size=(50, 1), default_text='',
           enable_events=True, readonly=True, text_color='Black'), sg.B('Copiar', key='COPIAR', size=(5, 1))],
    [sg.T('Gere senhas seguras', size=(30, 2), key='TEXT')],
    [sg.B(image_filename='GUI-foto/info.png', button_color=(sg.theme_background_color(),
                                                            sg.theme_background_color()), border_width=0, pad=(('380', '3'), ('0', '0')), key='AVISO')]
]
window = sg.Window('Gerador de Senhas', layout)

while True:

    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'EXIT':
        break

    if event == 'MODE':
        if values['MODE'] == True:
            window['FRASE'].update(disabled=False, text_color='White')
            window['TOTAL'].update('0')
            window['NUMERO'].update('0')
            window['SIMBOLO'].update('0')
            window['MAIUSCULO'].update('0')
            window['MINUSCULO'].update('0')
        else:
            window['FRASE'].update(disabled=True, text_color='Black')
            window['TOTAL'].update('12')
            window['NUMERO'].update('3')
            window['SIMBOLO'].update('3')
            window['MAIUSCULO'].update('3')
            window['MINUSCULO'].update('3')

    if values['MODE'] == False:

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
    window['OUT'].update('')
    if event == 'GERAR':
        if values['MODE'] == False:
            if int(values['TOTAL']) - (int(values['NUMERO']) + int(values['SIMBOLO']) + int(values['MAIUSCULO']) + int(values['MINUSCULO'])) > 0:
                sg.Popup(
                    'Valores insuficientes\nAumente as variaveis ou dimunua o total', title='AVISO')
            else:
                
                quantos_numeros, quantos_simbolos, quantos_maiusculos, quantos_minusculos = int(values['NUMERO']), int(values['SIMBOLO']), int(values['MAIUSCULO']), int(values['MINUSCULO'])
                senha = gerador.gerar_senha_aleatoriamente(quantos_numeros, quantos_simbolos, quantos_maiusculos, quantos_minusculos) 
                window['RESP'].update(senha)

                window['OUT'].update('Senha gerada aleatoriamente')

        else:
            if len(values['FRASE']) > 0:
                window['RESP'].update(gerador.gerar_senha_por_frase(values['FRASE']))
                window['OUT'].update('Senha gerada por frase')

    # copiar para a area de transferencia
    window['TEXT'].update('Gere senhas seguras')  # volta para o valor padrão
    if event == 'COPIAR' and values['RESP'] != '':
        clipboard.copy(values['RESP'])
        window['TEXT'].update('Senha copiada para a area de transferencia')

    if event == 'AVISO':
        sg.popup('O gerador de senhas conta com duas opções principais:\n\nGerar senha aleatoriamente: Podendo escolher quantos caracteres gerar essa opção conta tambem com controle de quantos tipos de caracteres a senha irá conter e quanto caractere gerar em cada tipo separadamente, podendo gerar bilhões de combinações diferentes\n\nGerar senha por frase: Se você é daquele tipo de pessoa esquecida e baseia sua senha em palavras e frases que consegue se lembrar, essa opção é feita para você. Selecionando a frase que você digitou e transformando em uma senha forte e dificil de ser descoberta, essa opção pode chegar a fornecer dezenas e até centenas de versões de senha para a frase que você digitou\n\n\nIndependente da função que você escolher, terá maior segurança com suas senhas ao utilizar esse gerador de senhas 100% open-source\n\nCriado por: Pablo Emidio\nGithub:"https://github.com/PabloEmidio/gerador-de-senha-PySimpleGUI"', title='Informações')


window.close()
