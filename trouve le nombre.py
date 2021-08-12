import random, os, sys
from pyfade import Colors, Fade 
from os import name
from pycenter import center



def clear():
  if name == 'nt':
    os.system('cls')
  else:
    os.system('clear')

    def acueille_mode():
        clear()

def main():
    maxn = 100
    n = random.randint(1, maxn)
    Jeux = """
  ▄▄▄▄███▄▄▄▄    ▄█  ███▄▄▄▄    ▄█          ▄██████▄     ▄████████   ▄▄▄▄███▄▄▄▄      ▄████████    ▄████████ 
 ▄██▀▀▀███▀▀▀██▄ ███  ███▀▀▀██▄ ███         ███    ███   ███    ███ ▄██▀▀▀███▀▀▀██▄   ███    ███   ███    ███ 
 ███   ███   ███ ███▌ ███   ███ ███▌        ███    █▀    ███    ███ ███   ███   ███   ███    █▀    ███    █▀  
 ███   ███   ███ ███▌ ███   ███ ███▌       ▄███          ███    ███ ███   ███   ███  ▄███▄▄▄       ███        
 ███   ███   ███ ███▌ ███   ███ ███▌      ▀▀███ ████▄  ▀███████████ ███   ███   ███ ▀▀███▀▀▀     ▀███████████ 
 ███   ███   ███ ███  ███   ███ ███         ███    ███   ███    ███ ███   ███   ███   ███    █▄           ███ 
 ███   ███   ███ ███  ███   ███ ███         ███    ███   ███    ███ ███   ███   ███   ███    ███    ▄█    ███ 
  ▀█   ███   █▀  █▀    ▀█   █▀  █▀          ████████▀    ███    █▀   ▀█   ███   █▀    ██████████  ▄████████▀  
"""

    print(Fade.Vertical(Colors.red_to_yellow, center(Jeux)))
    print("Bienvenue sur Mini games")
    print('Choisis un chiffre de 1 à %d' % maxn)
    guess = None
    while guess != n:
        guess = int(input('Chiffre: '))
        if guess > n:
            print('Trop haut')
        if guess < n:
            print('Trop bas')

    print('Bravo, tu as gagné !')

main()

liste = ["R","r"]

listes = ["Q","q"]

while True:
    rep = input("Veux tu rejouer ? R[ejouer] ou Q[uitter]: \n").lower()
    if rep == "r":
         clear()
         main()
    if rep == "q":
        sys.exit()