from random import sample, shuffle
import string

class GeradorDeSenhas:
    def __init__(self):
        self.numeros = string.digits
        self.letras_maiusculas = string.ascii_uppercase
        self.letras_minusculas = string.ascii_lowercase
        self.simbolos = string.punctuation
        
        
    def gerar_senha_aleatoriamente(self, quantos_numeros, quantos_simbolos, quantos_maiusculos, quantos_minusculos) -> str:
        numeros_gerados = ''.join(sample(self.numeros, quantos_numeros))
        simbolos_gerados = ''.join(sample(self.simbolos, quantos_simbolos))
        letras_maiusculas_geradas = ''.join(sample(self.letras_maiusculas, quantos_maiusculos))
        letras_minusculas_geradas = ''.join(sample(self.letras_minusculas, quantos_minusculos))
        soma_dos_elemetentos_gerados = numeros_gerados + simbolos_gerados + letras_maiusculas_geradas + letras_minusculas_geradas
        senha = [i for i in soma_dos_elemetentos_gerados]
        shuffle(senha)
        senha = ''.join(senha)
        return senha
    
    
    def gerar_senha_por_frase(self, frase) -> str:
        import unidecode
        frase = unidecode.unidecode(frase)
        senha = frase.lower()
        
        substitutos = {
            ' ': ['-', '_'],
            'a': ['a', 'A', '@', '4'],
            'b': ['b', 'B'],
            'c': ['c', 'C', '(', '[', '{'],
            'd': ['d', 'D'],
            'e': ['e', 'E', '%', '3'],
            'f': ['f', 'F'],
            'g': ['g', 'G', '6'],
            'h': ['h', 'H', '8'],
            'i': ['i', 'I', '!', '1'],
            'j': ['j', 'J'],
            'k': ['k', 'K'],
            'l': ['l', 'L'],
            'm': ['m', 'M'],
            'n': ['n', 'N'],
            'o': ['o', 'O', '0'],
            'p': ['p', 'P'],
            'q': ['q', 'Q'],
            'r': ['r', 'R'],
            's': ['s', 'S', '$', '5'],
            't': ['t', 'T', '7'],
            'u': ['u', 'U'],
            'v': ['v', 'V'],
            'w': ['w', 'W'],
            'x': ['x', 'X'],
            'y': ['y', 'Y'],
            'z': ['z', 'Z']
            }
        
        senha = senha.replace(' ', ''.join(sample(substitutos[' '], 1)))
        for i in range(len(senha)):
            if senha[i].isalpha():
                senha = senha.replace(senha[i], ''.join(sample(substitutos[senha[i].lower()], 1)), 1)
        return senha


gerador_de_senhas = GeradorDeSenhas()
