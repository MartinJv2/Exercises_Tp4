from math import pi
from random import randint
import dataclasses

choix_exercise = int(input("Choisissez un exercise (1-6)"))

if choix_exercise == 1:
    class StringFoo:
        def __init__(self):
            self.message = "Salut et bienvenu a mon code"

        def set_string(self, string):
            self.message = string

        def print_string(self):
            print(self.message.upper())


    message_du_jeu = StringFoo()
    message_du_jeu.set_string(input("message : "))
    message_du_jeu.print_string()

elif choix_exercise == 2:
    class Rectangle:
        def __init__(self, longueur, largeur):
            self.longueur = longueur
            self.largeur = largeur
            self.aire = 0

        def calcul_aire(self):
            self.aire = self.longueur * self.largeur

        def afficher_infos(self):
            print(f'Largeur : {self.largeur} Longueur : {self.longueur} Aire = {self.aire}')


    aire = Rectangle(int(input("Longueur")), int(input("Largeur")))
    aire.calcul_aire()
    aire.afficher_infos()

elif choix_exercise == 3:
    class Cercle:
        def __init__(self, rayon):
            self.rayon = rayon

        def calcul_aire(self):
            return pi * self.rayon ** 2

        def calcul_circonference(self):
            return 2 * pi * self.rayon


    attributs_cercle = Cercle(int(input("Rayon")))
    print("Aire", attributs_cercle.calcul_aire())
    attributs_cercle.aire = attributs_cercle.calcul_aire()
    print("Circonference", attributs_cercle.calcul_circonference())

elif choix_exercise == 4:
    class Hero:

        def __init__(self, nom_hero):
            self.nom_hero = nom_hero
            self.nombre_vies = randint(1, 10) + randint(1, 10)
            self.force_attaque = randint(1, 6)
            self.force_defence = randint(1, 6)

        def attaque(self):
            return self.force_attaque + randint(1, 6)

        def dommages(self, dommages):
            self.nombre_vies -= dommages - self.force_defence
            return self.nombre_vies

        def est_vivant(self):
            if self.nombre_vies > 0:
                return True
            else:
                return False


    gennal = Hero("Gennal")
    print(f"Vous faites une attaque de force  {gennal.attaque()}")
    print(f"il reste a {gennal.nom_hero} {gennal.dommages(int(input('Nombre attaque de lennemie')))} vies")

elif choix_exercise == 5:

    @dataclasses.dataclass
    class AttributsDnd:
        force: int = randint(1, 20)
        dexterite: int = randint(1, 20)
        constitution: int = randint(1, 20)
        sagesse: int = randint(1, 20)
        charisme: int = randint(1, 20)

else:
    class Hero:

        def __init__(self, nom_hero, charisme):
            self.nom_hero = nom_hero
            self.nombre_vies = randint(1, 10) + randint(1, 10)
            self.vies_initial = self.nombre_vies
            self.force_attaque = randint(1, 6)
            self.force_defence = randint(1, 6)
            self.charisme = charisme

        def attaque(self):
            return self.force_attaque + randint(1, 6)

        def dommages(self, dommages):
            if self.charisme >= 15:
                return 0
            else:
                self.nombre_vies -= dommages - self.force_defence
                return self.nombre_vies

        def est_vivant(self):
            if self.nombre_vies > 0:
                return True
            else:
                return False


    gennal = Hero("Gennal", randint(1, 20))
    print(f"Vous faites une attaque de force  {gennal.attaque()}")
    print(
        f"il reste a {gennal.nom_hero} {gennal.dommages(int(input('Nombre attaque de lennemie')))} vies "
        f"(il y en avait {gennal.vies_initial} vies et {gennal.force_defence} defence au depart)")