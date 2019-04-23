#!/usr/bin/python3.4
# coding: utf-8
import csv
import random
import string
import time
from string import ascii_letters
import os
import getpass
import sys
from pathlib import Path


def sortLexo(nbElem):
    start_time = time.time() # enregistre le temps de départ
    listwords = ["".join(random.choice(ascii_letters) # choisi une lettre au hasard (le join va permettre de créer un mot(joindre les lettres))
                         for j in range(random.randint(100,50000)) ) # nombre de lettres dans le mot (choisi au hasard)
                 for i in range(nbElem) ] # nombre de mots dans la liste à trier

    # tri les mots de la liste dans l'odre lexicographique
    listwords.sort()

    del listwords
    # affiche la liste de mots triés
   # print(listwords)

    tempsEc = time.time() - start_time;
    print("TRI LEXICO")
    print("Nb elem : %d " % nbElem)
    print("Temps d'execution : %s secondes" % (tempsEc))

    # écrit le temps écoulé dans le fichier [nbElem]tridenombrement.csv
    savepathTemps = str(Path.home()) + '/PycharmProjects/PROJET-TRI/tempsLexico'
    completePathTemps = os.path.join(savepathTemps, '%dtrilexico.txt ' % nbElem)
    f = open(completePathTemps, 'a')
    f.write(str(tempsEc) + '\n')
    f.close()

    # calcul de la moyenne à l'aide des variable : somme, moyenne, nbLigne
    somme = 0
    moyenne = 0
    nbLigne = 0

    # on ouvre le fichier contenant les temps en lecture
    cr = (open(completePathTemps, "r"))

    # pour chaque élément de la colonne r, on additionne les valeur et on
    # incrémente le nbLigne afin de calculer la moyenne
    for r in cr:  # r = colone
        somme += float(r[0:20])
        nbLigne += 1
    # print("Somme temps : %s" % somme)
    moyenne = somme / nbLigne
    # print("Moyenne : %s" % moyenne)
    # print("Nb valeur : %s " % nbLigne)

    # on enregistre la moyenne obtenu dans le fichier moytridenombrement.txt
    savepathMoy = str(Path.home()) + '/PycharmProjects/PROJET-TRI/moyLexico'
    completePathMoy = os.path.join(savepathMoy, 'moytrilexico.txt')
    moy = open(completePathMoy, 'a')
    moy.write(str(moyenne) + ',' + str(nbElem) + '\n')
    moy.close()
