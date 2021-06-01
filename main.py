from password import password_generator as generator

import PySimpleGUI as sg
import clipboard

bottom_size = (1, 1)
sg.theme('DarkBrown')

layout = [
    [
        sg.T('Type a phrase:'),
        sg.In(key='PHRASE', text_color='Black', readonly=True)], 
    [
        sg.Checkbox(text='Generate password by phrase', key='MODE', enable_events=True, pad=(('280', '3'), ('5', '20')))],
    [
        sg.HorizontalSeparator(color='Black')],
    [
        sg.T('Password Lenght:', size=(15, 1)),
        sg.In(key='TOTAL', size=(3, 2), default_text='12',enable_events=True, readonly=True, text_color='Black'),
        sg.B('+', size=bottom_size, key='TOT+'),
        sg.B('-', size=bottom_size, key='TOT-')],
    [
        sg.T('Numbers: ', size=(15, 1)),
        sg.In(key='NUMBERS', size=(3, 2), default_text='3', enable_events=True, readonly=True, text_color='Black', ), 
        sg.B('+', size=bottom_size, key='NUM+'), sg.B('-', size=bottom_size, key='NUM-')],
    [
        sg.T('Symbols: ', size=(15, 1)),
        sg.In(key='SYMBOLS', size=(3, 2), default_text='3', enable_events=True, readonly=True, text_color='Black'),
        sg.B('+', size=bottom_size, key='SYMB+'),
        sg.B('-', size=bottom_size, key='SYMB-')],
    [
        sg.T('Uppercase letters: ', size=(15, 1)),
        sg.In(key='UPPERCASE', size=(3, 2), default_text='3', enable_events=True, readonly=True, text_color='Black'),
        sg.B('+', size=bottom_size, key='UPPER+'),
        sg.B('-', size=bottom_size, key='UPPER-')],
    [
        sg.T('Lowercase letters: ', size=(15, 1)),
        sg.In(key='LOWERCASE', size=(3, 2), default_text='3', enable_events=True, readonly=True, text_color='Black'),
        sg.B('+', size=bottom_size, key='LOWER+'),
        sg.B('-', size=bottom_size, key='LOWER-')],
    [
        sg.B('Generate', size=(7, 1)),
        sg.T('', size=(30, 1), key='OUT')],
    [
        sg.In(key='ANSWER', size=(50, 1), default_text='', enable_events=True, readonly=True, text_color='Black'),
        sg.B('Copy', key='COPY', size=(5, 1))],
    [
        sg.T('Generate security passwords', size=(30, 2), key='TEXT')],
    [
        sg.B(image_filename='.images/info.png', button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0, pad=(('450', '0'), ('0', '5')), key='INFORMATION')]]


window = sg.Window('Password generator', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == 'MODE':
        if values['MODE'] == True:
            window['PHRASE'].update(disabled=False, text_color='White')
            window['TOTAL'].update('0')
            window['NUMBERS'].update('0')
            window['SYMBOLS'].update('0')
            window['UPPERCASE'].update('0')
            window['LOWERCASE'].update('0')
        else:
            window['PHRASE'].update(disabled=True, text_color='Black')
            window['TOTAL'].update('12')
            window['NUMBERS'].update('3')
            window['SYMBOLS'].update('3')
            window['UPPERCASE'].update('3')
            window['LOWERCASE'].update('3')

    if values['MODE'] == False:

        # modify total value event
        if event == 'TOT+':
            window['TOTAL'].update(int(values['TOTAL']) + 1)

        if event == 'TOT-':
            if int(values['TOTAL']) - (int(values['NUMBERS']) + int(values['SYMBOLS']) + int(values['UPPERCASE']) + int(values['LOWERCASE'])) > 0:
                window['TOTAL'].update(int(values['TOTAL']) - 1)

        # modify number value event
        if event == 'NUM+':
            if int(values['TOTAL']) - (int(values['NUMBERS']) + int(values['SYMBOLS']) + int(values['UPPERCASE']) + int(values['LOWERCASE'])) > 0:
                window['NUMBERS'].update(int(values['NUMBERS']) + 1)

        if event == 'NUM-':
            if int(values['NUMBERS']) > 0:
                window['NUMBERS'].update(int(values['NUMBERS']) - 1)

        # modify symbol value event
        if event == 'SYMB+':
            if int(values['TOTAL']) - (int(values['NUMBERS']) + int(values['SYMBOLS']) + int(values['UPPERCASE']) + int(values['LOWERCASE'])) > 0:
                window['SYMBOLS'].update(int(values['SYMBOLS']) + 1)

        if event == 'SYMB-':
            if int(values['SYMBOLS']) > 0:
                window['SYMBOLS'].update(int(values['SYMBOLS']) - 1)

        # modify uppercase value event
        if event == 'UPPER+':
            if int(values['TOTAL']) - (int(values['NUMBERS']) + int(values['SYMBOLS']) + int(values['UPPERCASE']) + int(values['LOWERCASE'])) > 0:
                window['UPPERCASE'].update(int(values['UPPERCASE']) + 1)

        if event == 'UPPER-':
            if int(values['UPPERCASE']) > 0:
                window['UPPERCASE'].update(int(values['UPPERCASE']) - 1)

        # modify lowercase value event
        if event == 'LOWER+':
            if int(values['TOTAL']) - (int(values['NUMBERS']) + int(values['SYMBOLS']) + int(values['UPPERCASE']) + int(values['LOWERCASE'])) > 0:
                window['LOWERCASE'].update(int(values['LOWERCASE']) + 1)

        if event == 'LOWER-':
            if int(values['LOWERCASE']) > 0:
                window['LOWERCASE'].update(int(values['LOWERCASE']) - 1)

    # password generator event
    window['OUT'].update('')
    if event == 'Generate':
        if values['MODE'] == False:
            if int(values['TOTAL']) - (int(values['NUMBERS']) + int(values['SYMBOLS']) + int(values['UPPERCASE']) + int(values['LOWERCASE'])) > 0:
                sg.Popup(
                    'insufficient values\nIncrease the variables or decrease the total', title='INFORMATION')
            else:
                
                howmany_numbers, howmany_symbols, howmany_lowercase, howmany_uppercase = int(values['NUMBERS']), int(values['SYMBOLS']), int(values['UPPERCASE']), int(values['LOWERCASE'])
                password = generator.randomly_generate(howmany_numbers, howmany_symbols, howmany_lowercase, howmany_uppercase) 
                window['ANSWER'].update(password)

                window['OUT'].update('password generated randomly')

        else:
            if len(values['PHRASE']) > 0:
                window['ANSWER'].update(generator.generate_by_phrase(values['PHRASE']))
                window['OUT'].update('password generated by phrase')

    # copy to clipboard
    window['TEXT'].update('Generate security passwords')  # return default value
    if event == 'COPY' and values['ANSWER'] != '':
        clipboard.copy(values['ANSWER'])
        window['TEXT'].update('password copied to clipboard')

    if event == 'INFORMATION':
        sg.popup('The password generator has two main alternative:\n\nGenerate randomly password: With full controle of how many and what characters to use for generating, this alternative can generate billions of random combinations\n\nGenerate password by phrase: If you are kind of person who forgets every single security password, This alternative generates several password by a word or phrase from you choose\n\n\n\nCreated by: Pablo Emidio\nGithub: "https://github.com/PabloEmidio/password-generator-PySimpleGUI"', title='Information')


window.close()
