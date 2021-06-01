from random import sample, shuffle
import string

class PasswordGenerator:
    def __init__(self):
        self.numbers = string.digits
        self.uppercase_letters = string.ascii_uppercase
        self.lowercase_letters = string.ascii_lowercase
        self.symbols = string.punctuation
        
        
    def randomly_generate(self, howmany_numbers, howmany_symbols, howmany_uppercase, howmany_lowercase) -> str:
        numbers_generated = ''.join(sample(self.numbers, howmany_numbers))
        symbols_generated = ''.join(sample(self.symbols, howmany_symbols))
        uppercase_letters_generated = ''.join(sample(self.uppercase_letters, howmany_uppercase))
        lowercase_letters_generated = ''.join(sample(self.lowercase_letters, howmany_lowercase))
        all_generated_elements = numbers_generated + symbols_generated + uppercase_letters_generated + lowercase_letters_generated
        password = [i for i in all_generated_elements]
        shuffle(password)
        password = ''.join(password)
        return password
    
    
    def generate_by_phrase(self, phrase) -> str:
        import unidecode
        phrase = unidecode.unidecode(phrase)
        password = phrase.lower()
        
        to_replacement = {
            ' ': ['-', '_'],
            'a': ['a', 'A', '@', '4'],
            'b': ['b', 'B'],
            'c': ['c', 'C', '(', '[', '{'],
            'd': ['d', 'D'],
            'e': ['e', 'E', '&', '3'],
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
        
        password = password.replace(' ', ''.join(sample(to_replacement[' '], 1)))
        for i in range(len(password)):
            if password[i].isalpha():
                password = password.replace(password[i], ''.join(sample(to_replacement[password[i].lower()], 1)), 1)
        return password


password_generator = PasswordGenerator()
