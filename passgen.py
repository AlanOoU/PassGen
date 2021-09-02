import string
import random

characters = list(string.ascii_letters + string.digits +",;:!§/.?ù%^¨$£*µ&'(-_)=")

def generate_random_password():
    length = int(input("Entrer le nombre de caractère : "))
    random.shuffle(characters)
    password = []
    for i in range(length):
        password.append(random.choice(characters))

    random.shuffle(password)

    print("".join(password))

generate_random_password()