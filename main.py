"""
Fait par : Jeremy Martin
Groupe : 403
Le code va effectuer une serie d'exercises sur les classes dependament du choix de la personne qui le roule
(les exercises 4 et 5 sont dans le dernier)
"""

from math import pi
from random import randint
import dataclasses

choix_exercise = int(input("Choisissez un exercise (1-4)"))

if choix_exercise == 1:
    class StringFoo:
        def __init__(self):
            self.message = ""

        def set_string(self, string):
            self.message = string

        def print_string(self):
            print(self.message.upper())


    message_du_jeu = StringFoo()
    message_du_jeu.set_string("Salut et bienvenu a mon code")
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


    aire = Rectangle(5, 6)
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


    attributs_cercle = Cercle(5)
    print("Aire", attributs_cercle.calcul_aire())
    print("Circonference", attributs_cercle.calcul_circonference())


else:
    @dataclasses.dataclass
    class StatsCreature:
        force: int = randint(1, 20)
        dexterite: int = randint(1, 20)
        constitution: int = randint(1, 20)
        sagesse: int = randint(1, 20)
        charisme: int = randint(1, 20)
        inteligence: int = randint(1, 20)


    class Hero:
        def __init__(self, nom_hero):
            self.nom_hero = nom_hero
            self.nombre_vies = randint(1, 10) + randint(1, 10)
            self.vies_initial = self.nombre_vies
            self.force_attaque = randint(1, 6)
            self.force_defence = randint(1, 6)
            self.stats = StatsCreature()

        def attaque(self):
            return self.force_attaque + randint(1, 6)

        def dommages(self, dommages):
            if self.stats.constitution >= 15:
                return self.nombre_vies
            else:
                self.nombre_vies -= dommages - self.force_defence
                return self.nombre_vies

        def est_vivant(self):
            return self.nombre_vies > 0


    gennal = Hero("Gennal")
    print(f"Vous faites une attaque de force  {gennal.attaque()}")
    print(
        f"il reste a {gennal.nom_hero} {gennal.dommages(10)} vies apres avoir pris 10 dommage"
        f"\nen vie : {gennal.est_vivant()}\n"
        f"(il y en avait {gennal.vies_initial} vies et {gennal.force_defence} defence au depart)")
