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

class Reka:
    """ Klasa definiiująca ile i jakie karty mamy w ręce """
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def dodaj_karte(self,karta):
        """ Dodanie karty do ręki """
        self.cards.append(karta)
        self.value += PUNKTY[karta.figura]
        if karta.figura == 'As':
            self.aces += 1
    
    def dopasuj_as(self):
        while self.value > 21 and self.aces :
            self.value -= 10
            self.aces -= 1

class Zetony:
    """ Klasa żetony """
    def __init__(self,total=100):
        self.total = total
        self.zaklad = 0

    def wygrana(self):
        """ Wygrany zaklad """
        self.total += self.postaw

    def przegrana(self):
        """ Przegrany zaklad """
        self.total -= self.postaw

def przyjmij_zaklad(zetony):
    while True:
        try:
            zetony.zaklad = int(input("Ile zetonow chcesz postawic?: "))
        except:
            print("Wprowadz prawidlowa wartosc")
        else:
            if zetony.zaklad > zetony.total :
                print("Nie masz tyle zetonow")
            else:
                break

def dobierz(talia,reka):
    reka.dodaj_karte(talia.wez_karte())
    reka.dopasuj_as()

def dobierz_albo_stoj(talia,reka):
    global playing
    while True:
        x = input("Dobierasz czy stoisz? h/s")
        if x[0].lower() == 'h':
            dobierz(talia,reka)
        elif x[0].lower() == 's':
            print("Koniec tury, kolej Dilera")
            playing = False
        else:
            print("Wpisz h or s")
            continue
        break

def gracz_wygral(player,dealer,zetony):
    print("Gracz wygral!")
    player.wygrana()
    
def gracz_przegral(player,dealer,zetony):
    print("Gracz przegral!")
    player.przegrana()
    
def dealer_wygral(player,dealer,zetony):
    print("Dealer wygral!")
    player.przegrana()
    
def dealer_przegral(player,dealer,zetony):
    print("Dealer przegral!")
    player.wygrana()
    
def remis():
    print("Remis!")
    

while True:
    print("Witamy w grze")
    talia = Talia()
    talia.tasuj()

    gracz_reka = Reka()
    gracz_reka.dodaj_karte(talia.wez_karte())
    gracz_reka.dodaj_karte(talia.wez_karte())

    dealer_reka = Reka()
    dealer_reka.dodaj_karte(talia.wez_karte())
    dealer_reka.dodaj_karte(talia.wez_karte())

    gracz_zetony = Zetony()

    przyjmij_zaklad(gracz_zetony)

    