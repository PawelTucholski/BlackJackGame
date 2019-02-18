"""
Black Jack Game
"""
import random
from colorama import init, Fore, Back, Style
init(autoreset=True)

KOLORY = ('Karo', 'Kier', 'Pik', 'Trefl')
FIGURY = ('Dwójka', 'Trójka', 'Czwórka', 'Piątka', 'Szóstka', 'Siódemka', 'Ósemka', 'Dziewiątka', 'Dziesiątka', \
    'Walet', 'Dama', 'Król', 'As')
PUNKTY = {'Dwójka':2, 'Trójka':3, 'Czwórka':4, 'Piątka':5, 'Szóstka':6, 'Siódemka':7, 'Ósemka':8,\
     'Dziewiątka':9, 'Dziesiątka':10, 'Walet':10, 'Dama':10, 'Król':10, 'As':11}

class Karta:
    """Klasa tworząca kartę danej figury i danego koloru"""
    def __init__(self, figura, kolor):
        self.kolor = kolor
        self.figura = figura
    def __str__(self):
        """ Wyswietlanie karty """
        return self.figura + " " + self.kolor
class Talia:
    """
    Klasa tworząca talię kart
    """
    def __init__(self):
        self.talia = []
        for kolor in KOLORY:
            for figura in FIGURY:
                self.talia.append(Karta(figura, kolor))
    def __str__(self):
        """ Wyswietlanie talii """
        moja_talia = ''
        for karta in self.talia:
            moja_talia += '\n'+ karta.__str__()
        return "Talia zawiera "+ moja_talia
    def tasuj(self):
        """ Tasowanie kart """
        random.shuffle(self.talia)
    def wez_karte(self):
        """ Dobieranie karty """
        karta = self.talia.pop()
        return karta

talia_testowa = Talia()
#print(talia_testowa)
talia_testowa.tasuj()
print(talia_testowa)
print(Fore.RED + Back.BLUE + "Test")
print(Style.BRIGHT + "Test1")