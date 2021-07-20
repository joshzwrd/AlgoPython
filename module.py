# 1- MODULE builtins 
# Chargé dès le chargement de Python
# Il contient beaucoup de fonctions qu'on utilise directement sans les importer
nom = "TOTO"
taille = len(nom)
print(taille)

nb = [4, 1, 2, 8, 11, 0]
print(max(nb))

#import builtins
#print(dir(builtins))


# 2- MODULES installés avec Python, mais qu'il faut importer
import math
#print(dir(math))
print("racine de 16 : ", math.sqrt(16))

from math import sqrt
print("racine de 24 : ", sqrt(24))

# 3- MODULES non présents dans Python = à installer et importer
# pip install easygui
from easygui import integerbox
age = integerbox(msg="Donner age", title="fenetre COOL")
print("Age :", age)

# 4- MODULE Crée par vous (voir le fichier main.py)