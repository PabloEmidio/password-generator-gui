from random import choice, shuffle, randint


def GerarSenhaRandom(quantoNumero=0, quantoSimbolo=0, quantoMaiusculo=0, quantoMinusculo=0):

    quantoNum = quantoSimb = quantoMaius = quantoMinus = 0
    senha = []
    while True:

        op = choice([1, 2, 3, 4])
        gera = ''
        if op == 1 and quantoNumero > quantoNum:
            gera = gerarNumeros()
            quantoNum += 1
        elif op == 2 and quantoSimbolo > quantoSimb:
            gera = gerarSimbolo()
            quantoSimb += 1
        elif op == 3 and quantoMaiusculo > quantoMaius:
            gera = gerarMaiusculo()
            quantoMaius += 1
        elif op == 4 and quantoMinusculo > quantoMinus:
            gera = gerarMinusculo()
            quantoMinus += 1
        senha.append(gera)

        if quantoNum == quantoNumero and quantoSimb == quantoSimbolo and quantoMinus == quantoMinusculo and quantoMaius == quantoMaiusculo:
            break
    shuffle(senha)
    senha = ''.join(senha)
    return senha


def gerarNumeros():

    opcoes = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    return choice(opcoes)


def gerarSimbolo():

    opcoes = ['!', '@', '#', '$', '%', '¬', '&',
              '*', '(', ')', '-', '_', '=', '+', '§']
    return choice(opcoes)


def gerarMaiusculo():

    opcoes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
              'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    return choice(opcoes)


def gerarMinusculo():

    opcoes = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
              'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    return choice(opcoes)


# gerar senha para frase

def GerarSenhaByFrase(text):

    text = text.lower()

    sorte = Sortear()
    if sorte % 2 == 0:
        text = text.replace(' ', '_')
    else:
        text = text.replace(' ', '-')

    sorte = Sortear()
    if sorte % 2 == 0:
        text = text.replace('a', '@')
    else:
        text = text.replace('a', '4')

    sorte = Sortear()
    if sorte % 2 == 0:
        text = text.replace('g', '6')

    sorte = Sortear()
    if sorte % 2 == 0:
        text = text.replace('o', '0')

    sorte = Sortear()
    if sorte % 2 == 0:
        text = text.replace('t', '7')

    sorte = Sortear()
    if sorte % 2 == 0:
        text = text.replace('s', '5')
    else:
        text = text.replace('s', '$')

    sorte = Sortear()
    if sorte % 2 == 0:
        text = text.replace('i', '!')
    else:
        text.replace('i', '1')

    sorte = Sortear()
    if sorte % 2 == 0:
        text = text.replace('e', '&')
    else:
        text.replace('e', '3')

    cont = 0
    while True:
        op = randint(0, len(text)-1)
        cont += 1
        if text[op].isalpha():
            tochange = text[op]
            tochange = tochange.upper()
            text = text.replace(text[op], tochange)
        if cont == len(text):
            break
    return text


def Sortear():
    return randint(0, 10000)
