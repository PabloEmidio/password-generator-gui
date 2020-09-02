# def frase_gerador():

import PySimpleGUI as sg
from password import GerarSenhaRandom, GerarSenhaByFrase
import clipboard

tamBottom = (1, 1)

sg.theme('DarkBrown')

layout = [[sg.T('Digita a frase:'), sg.In(key='FRASE')],

[sg.T('Caracteres extras', pad=('15', ('50', '5')))],

[sg.T('↑', background_color='DarkBlue', enable_events=True, key='NUM+'), sg.In(default_text='0', size=(3, 6), enable_events=True, key='NUMERO'), sg.T('↓', background_color='DarkBlue', enable_events=True, key='NUM-'), sg.T('Numeros')],

[sg.T('↑', background_color='DarkBlue', size=(1,1), enable_events=True, key='SIMB+'), sg.In(default_text='0', size=(3, 2), enable_events=True, key='SIMBOLO'), sg.T('↓', background_color='DarkBlue', enable_events=True, key='SIMB-'), sg.T('Simbolos')],

[sg.T('↑', background_color='DarkBlue', enable_events=True, key='MAIUS+'), sg.In(default_text='0', size=(3, 6), enable_events=True, key='MAIUSCULA'), sg.T('↓', background_color='DarkBlue', enable_events=True, key='MAIUS-'), sg.T('Letras Maiusculas')],

[sg.T('↑', background_color='DarkBlue', enable_events=True, key='MINUS+'), sg.In(default_text='0', size=(3, 6), enable_events=True, key='MINUSCULA'), sg.T('↓', background_color='DarkBlue', enable_events=True, key='MINUS-'), sg.T('Letras Minusculas')],

[sg.B('GERAR')],

[sg.In(default_text='', enable_events=True, readonly=True, key='SENHA', text_color='Black'), sg.B('Copiar', key='COPY')]]

window = sg.Window('Gerador de Senha', layout, size=(500, 500))
sg.Text()
while True:

    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == 'NUM+':
        window['NUMERO'].update(int(values['NUMERO']) + 1)
    
    if event == 'NUM-':
        window['NUMERO'].update(int(values['NUMERO']) - 1)

    
    if event == 'SIMB+':
        window['SIMBOLO'].update(int(values['SIMBOLO']) +1)
    
    if event == 'SIMB-':
        window['SIMBOLO'].update()


    if event == 'GERAR':
        if len(values['FRASE']) > 0:
           window['SENHA'].update(GerarSenhaByFrase(values['FRASE']))

    if event == 'COPY':
        clipboard.copy(values['SENHA'])
    


window.close()
