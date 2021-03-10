#!/usr/bin/env python
# malorybergezcasalou
# simple script encryption passwd / txt

typePass = input("type text: ")


def encryption(typePass, decalage=2):
    res = ""

    """
    for lettre in typePass:
        if 65 >= ord(lettre) <= (65 + 26 - decalage):
            res += chr(ord(lettre) + decalage)
        elif ord(lettre) > (65 + 26 - decalage) and ord(lettre) < 97:
            res += chr(65 + ((ord(lettre) + decalage) - (65 + 26)))
        elif 97 >= ord(lettre) <= (97 + 26 - decalage):
            res += chr(ord(lettre) + decalage)
        else:
            res += chr(97 + ((ord(lettre) + decalage) - (97 + 26)))
    """
    for lettre in typePass:
        if ord(lettre) + decalage <= 128:
            res += chr(ord(lettre) + decalage)
        else:
            res += chr((ord(lettre) + decalage) - 128)

    return res


fichier = open("./encryption/encryptedPass.txt", "w")
fichier.write(encryption(typePass, 3))
fichier.close()
