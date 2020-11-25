#!/usr/bin/env python
# malorybergezcasalou
# script password generator

"""
SCRIPT EN COURS
"""

import random
import string

letters = string.ascii_letters
numbers = string.digits  
punctuation = string.punctuation    

def passwdGenerator(length=12):
    printable = f'{letters}{numbers}{punctuation}'
    printable = list(printable)
    random.shuffle(printable)

    randomPass = random.choices(printable)
    randomPass = ''.join(randomPass)
    return randomPass

password = passwdGenerator()

fichier = open("./passGenerator/pass.txt", "w")
fichier.write(password)
fichier.close()
