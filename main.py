import maj
#dir(maj)

# Appel de la fonction maj()
print(maj.maj("gamba"))

# Du package minus j'importe le module mesfonctions
from minus import mesfonctions
#dir(mesfonctions)
print(mesfonctions.minuscule("LEOPOLD"))

# Import de la fonction minuscule() directement
from minus.mesfonctions import minuscule
print(minuscule("DUPONT"))
