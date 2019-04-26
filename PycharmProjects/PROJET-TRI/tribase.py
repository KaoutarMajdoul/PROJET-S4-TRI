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
 
def radixSort(nbElem):        
    start_time = time.time()
    list_vals = random.sample(range(1000),nbElem)    #On créé une liste de nbElem éléments de valeurs aléatoires inférieures ou égale à 1000
    print("Le tableau non trié :")
    print(list_vals)
    maxLength = False     #On initialise maxLenght à False qui est vrai si on est sur le dernier placement 
    placement = 1         #On initialise placement à 1 qui indique le placement dans notre chiffre
    nbOccurence = [0 for i in range(0, max(list_vals)+1)]; #On créé un tableau de taille max(list_vals)+1  dans lequel on placera le nombre d'occurence à un indice donnée
    occurences = [[] for y in range(0,max(list_vals)+1)]   #On creéé un tableau ayant pour indice les valeurs du tableau nbOccurence
    listTmp = [0 for i in range(0, len(list_vals))]        
    while not maxLength:                                                                            
        list_chiffres = [int(((list_vals[i]%(placement*10))/placement)) for i in range(0,nbElem)]     #On complète le tableau list_count en commençant par le chiffre des unités des valeurs de list_vals
        # Dans cette boucle on parcours list_counts et on complète le tableau nbOccurence par le nombre d'occurences de chaque valeurs et on complète buckets2 par les indices d'occurences de chaque élément
        for i in range(0,nbElem):
            nbOccurence[list_chiffres[i]]+=1
            occurences[list_chiffres[i]].append(i)
        j=0
        # Dans cette boucle on parcours buckets2 et nboccurrence et en fonction du nombre d'occurence enregistrés dans nboccurence, les indices des éléments qui sont enregistrées dans le tableau buckets2 on complète le tableau listTmp qui a la meme taille que listVals  
        for i in range(0, max(list_vals)+1):
            k=0
            while nbOccurence[i] > 0  :
                listTmp[j]=list_vals[occurences[i][k]]
                j = j+1
                k = k+1
                nbOccurence[i] = nbOccurence[i] - 1
        
        #On vide les deux tableaux
        nbOccurence = [0 for i in range(0, max(list_vals)+1)]
        occurences = [[] for i in range(0,max(list_vals)+1)] 
        
        #On copie em profondeur le listTmp dans listVal
        list_vals = [listTmp[i]for i in range(0,nbElem)]
        
        #On passe des unités aux dizaines et ainsi de suite 
        placement *= 10
        
        #Si on est au niveau des centaines on arrete la boucle 
        if placement == 1000:
            maxLength = True
            
        





    #On affiche la liste triée
    print("Le tableau trié :")
    print(list_vals)
    tempsEc = time.time() - start_time;
    print("Temps d'execution : %s secondes" % (tempsEc))
    
    
 
    print("TRI PAR BASE")
    print("Nb elem : %d " % nbElem)
    print("Temps d'execution : %s secondes" % (tempsEc))

    # écrit le temps écoulé dans le fichier [nbElem]tridenombrement.csv
    savepathTemps = str(Path.home()) + '/PycharmProjects/PROJET-TRI/tempsBase'
    completePathTemps = os.path.join(savepathTemps, '%dtribase.txt ' % nbElem)
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
        for r in cr:  # r = colone
            r = str(r)
            r = r[2:-2]
            somme += float(r[0:20])
            nbLigne += 1
    print("Somme temps : %s" % somme)
    moyenne = somme / nbLigne
    print("Moyenne : %s" % moyenne)
    print("Nb ligne : %s " % nbLigne)

    # on enregistre la moyenne obtenu dans le fichier moytridenombrement.txt
    savepathMoy = str(Path.home()) + '/PycharmProjects/PROJET-TRI/moyBase'
    completePathMoy = os.path.join(savepathMoy, 'moytribase.txt')
    moy = open(completePathMoy, 'a')
    moy.write(str(moyenne) + ',' + str(nbElem) + '\n')
    moy.close()
        
        
def main (): 
    radixSort(12)
main() 
    



