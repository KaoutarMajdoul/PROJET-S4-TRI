#!/usr/bin/python3.4
# coding: utf-8
import random

import csv
import random
import time

import matplotlib.pyplot as plt
import os
import getpass
import sys
from pathlib import Path

def bucket_sort(nbElem):
    start_time = time.time()
    alist = random.sample(range(100,50000), nbElem)
    largest = max(alist)
    length = len(alist)
    size = largest / length

    buckets = [[0 for i in range(largest + 1)] for _ in range(length + 1)]
    # bucket de  taille largest +1
    # liste de longeur max de liste
    # chaque fois on ajoute un a l'indice de l'elemnt de alist

    for i in range(length):
        j = int(alist[i] / size)
        buckets[j][alist[i]] += 1

    result = []

    for i in range(length):
        # on parcourt bucket et si chaque elemnt != 0 on met indice dans liste resultat
        for j in range(largest):
            # on ajoute l'elem different de 0
            while buckets[i][j] != 0:
                result.append(j)
                buckets[i][j] -= 1

    del  alist


    # calcul temps écoulé
    tempsEc = time.time() - start_time;
    print("TRI PAQUET")
    print("Nb elem : %d " % nbElem)
    print("Temps d'execution : %s secondes" % (tempsEc))

    # écrit le temps écoulé dans le fichier [nbElem]tripaquet.csv
    savepathTemps = str(Path.home()) + '/PycharmProjects/PROJET-TRI/tempsPaquet'
    completePathTemps = os.path.join(savepathTemps, '%dtripaquet.txt ' % nbElem)
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
        somme += float(r[0])
        nbLigne += 1
    # print("Somme temps : %s" % somme)
    moyenne = somme / nbLigne
    # print("Moyenne : %s" % moyenne)
    # print("Nb valeur : %s " % nbLigne)

    # on enregistre la moyenne obtenu dans le fichier moytripaquet.txt
    savepathMoy = str(Path.home()) + '/PycharmProjects/PROJET-TRI/moyPaquet'
    completePathMoy = os.path.join(savepathMoy, 'moytripaquet.txt')
    moy = open(completePathMoy, 'a')
    moy.write(str(moyenne) + ',' + str(nbElem) + '\n')
    moy.close()
