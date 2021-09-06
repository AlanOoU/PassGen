import string
import random
from pyfade import Colors, Fade
from pycenter import center
from time import sleep
from colorama import Fore , init

characters = list(string.ascii_letters + string.digits +",;:!§/.?ù%^¨$£*µ&'(-_)=")

passgen = """

   ___    ___    ____   ____  _____   ____   _  __
  / _ \  / _ |  / __/  / __/ / ___/  / __/  / |/ /
 / ___/ / __ | _\ \   _\ \  / (_ /  / _/   /    /
/_/    /_/ |_|/___/  /___/  \___/  /___/  /_/|_/

"""

def generate_random_password():
    print(Fade.Vertical(Colors.blue_to_cyan , center(passgen)))
    try:
        length = int(input(Fore.LIGHTGREEN_EX+"Entrer le nombre de caractère : "))
    except ValueError:
        print()
        print(Fore.LIGHTGREEN_EX+"Entrez un Nombre s'il vous plaît")
        (generate_random_password)

    random.shuffle(characters)
    password = []
    for i in range(length):
        password.append(random.choice(characters))

    random.shuffle(password)

    print(Fore.LIGHTRED_EX+"Votre Mot De Passe est : " , password)
    sleep(15)

generate_random_password()
