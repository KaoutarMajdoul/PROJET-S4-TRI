#!/usr/bin/python3.4
# coding: utf-8
import csv
import random
import time

import matplotlib.pyplot as plt
import os
import getpass
import sys
from pathlib import Path

def counting_sort(nbElem):
    #debut timer
    start_time = time.time()
    # mise en place d'une liste de nbElem de 0 à 1000
    list_vals = random.sample(range(1000,50000), nbElem)

    liste = []
    moyenne = 0

    #  récup valeur max de la liste aléatoire
    max_val = max(list_vals);

    list_counts = [];
    list_sorted = [];
    # initialise chaque élément à 0
    list_counts = [0 for i in range(0, max_val + 1)];

    # fréquence de chaque elemt du tableau
    for i in range(0, len(list_vals)):
        list_counts[list_vals[i]] += 1;

        # ajoute les elements triés selon la fréquence
    for i in range(0, max_val + 1):
        while (list_counts[i] > 0):
            list_sorted.append(i);
            list_counts[i] -= 1;

    del list_vals
    # affichage avant après tri
    #print(list_vals);
    #print(list_sorted);

    # calcul temps écoulé
    tempsEc = time.time() - start_time;
    print("TRI DENOMBREMENT")
    print("Nb elem : %d " % nbElem)
    print("Temps d'execution : %s secondes" % (tempsEc))

    # écrit le temps écoulé dans le fichier [nbElem]tridenombrement.csv
    savepathTemps =  str(Path.home()) + '/PycharmProjects/PROJET-TRI/tempsDenombrement'
    completePathTemps = os.path.join(savepathTemps, '%dtridenombrement.txt ' % nbElem)
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
    #print("Moyenne : %s" % moyenne)
    #print("Nb valeur : %s " % nbLigne)

    # on enregistre la moyenne obtenu dans le fichier moytridenombrement.txt
    savepathMoy = str(Path.home()) + '/PycharmProjects/PROJET-TRI/moyDenombrement'
    completePathMoy = os.path.join(savepathMoy, 'moytridenombrement.txt')
    moy = open(completePathMoy, 'a')
    moy.write(str(moyenne) + ',' + str(nbElem) + '\n')
    moy.close()
