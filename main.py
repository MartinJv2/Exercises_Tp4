from math import pi
from random import randint

choix_exercise = int(input("Choisissez un exercise (1-4)"))

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

if choix_exercise == 2:
    class Rectangle:
        def __init__(self, longueur, largeur):
            self.longueur = longueur
            self.largeur = largeur
            self.aire = 0

        def calcul_aire(self):
            self.aire = self.longueur * self.largeur
            return aire

        def afficher_infos(self):
            print(f'Largeur : {self.largeur} Longueur : {self.longueur} Aire = {self.largeur*self.longueur}')


    aire = Rectangle(int(input("Longueur")), int(input("Largeur")))
    aire.afficher_infos()

if choix_exercise == 3:
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

if choix_exercise == 4:
    class Hero:

        def __init__(self, nom_hero):
            self.nom_hero = nom_hero
            self.nombre_vies = randint(1, 10) + randint(1, 10)
            self.force_attaque = randint(1, 6)
            self.force_defence = randint(1, 6)

        def attaque(self):
            return self.force_attaque + randint(1, 6)

        def dommages(self, dommages):
            return dommages - self.force_defence

        def est_vivant(self):
            return bool()


    gennal = Hero
    print("Une attaque de force ",gennal.attaque)
    print(f"il vous reste {gennal.nombre_vies - gennal.dommages} vies")
