# class User:
#     pass

class User:

    # Attibut statique : non attaché à self
    surnom = "MOMO"

    # Initialisateur = constructeur par abus de langage
    # Etape 1 : python crée l'objet self, en utilisant la méthode __new__()
    def __init__(self, n, a):
        self.nom = n
        self.__age = a        # L'attribut age est privé = accessible dans la classe

    # Créer un getter (=lire l'âge ds l'objet) et un setter (=modifier l'âge stocké ds objet)
    # Associer une property
    def get_age(self):
        return self.__age
    
    def set_age(self, age):
        self.__age = age

    # Property
    age = property(get_age, set_age)

    # Ajoutons une manière de faire un print de l'objet
    # Cette def doit retourner une chaine
    def __str__(self):
        #chaine = "Je suis " + self.nom + " et j'ai " + str(self.__age) + " ans."
        chaine = "Je suis " + self.nom + " et j'ai " + str(self.age) + " ans."
        return chaine

    def get_identite(self):
        #chaine = "Nom: " + self.nom + " , Age: " + str(self.__age) 
        chaine = "Nom: " + self.nom + " , Age: " + str(self.age)
        return chaine

    # Méthode statique
    @staticmethod     # décorateur = fonction qui modifie le comportement (décore) d'une autre fonction
    def somme(a, b):
        return a + b




# Classe pour héritage
class Salarie(User):
    # Initialisateur
    def __init__(self, n, a, s):
        super().__init__(n, a)
        self.salaire = s



# PROGRAMME PRINCIPAL
# Créer un utilisateur
#u1 = User()          # Si en java : User u1 = new User()
u1 = User("DUPONT", 40)
print(u1)

# Stocker le nom et l'âge
# u1.nom = "TOTO"
# u1.age = 40

# Afficher l'objet
#print("Nom: " , u1.nom)
#print("Age: ", u1.age)
#print(u1.__dict__)

# Afficher l'identité
#print(u1.get_identite())

# Utiliser getter et setter
print("Age: ", u1.get_age())
u1.set_age(100)
print(u1)

# Avec une property age, c'est comme si age était public
print("Age: ", u1.age)

#print(dir(u1))


# Créer un salarié
employe = Salarie("DUPONT", 45, 5600)
print(employe.get_identite(), "et je gagne ", employe.salaire, " Euros.")

# Utiliser l'attribut et la méthode statiques
print("Le surnom est :", User.surnom)
u2 = User("JEAN", 80)
u3 = User("PIERRE", 40)
print(u2.surnom, u3.surnom, User.surnom) # u2 et u3 ont accès

print("Somme de 4 et 9: ", User.somme(4, 9))