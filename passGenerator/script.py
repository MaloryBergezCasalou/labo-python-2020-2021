#!/usr/bin/env python
# malorybergezcasalou
# script password generator


import random
import string

letters = string.ascii_letters
numbers = string.digits  
punctuation = string.punctuation    

def passwdGenerator(length=12):
    printable = f'{letters}{numbers}{punctuation}'
    liste = []
    for _ in range(length):
        liste.append(random.choice(printable))
    
    randomPass = ''.join(liste)
    return randomPass

password = passwdGenerator()

fichier = open("./passGenerator/pass.txt", "w")
fichier.write(password)
fichier.close()
