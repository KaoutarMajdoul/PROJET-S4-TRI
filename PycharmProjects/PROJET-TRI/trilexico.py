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
import pathlib


def sortLexo(nbElem):
    start_time = time.time() # enregistre le temps de départ
    li = ["".join(random.choice(ascii_letters) # choisi une lettre au hasard (le join va permettre de créer un mot(joindre les lettres))
                         for j in range(random.randint(1000,100000)) ) # nombre de lettres dans le mot (choisi au hasard)
                 for i in range(nbElem) ] # nombre de mots dans la liste à trier

    # tri les mots de la liste dans l'odre lexicographique
    x = len(li)
   
    
    #print("List is : ",li)
    
    
    for i in range(0,x):
        for j in range(0,x):
            if li[i]<li[j]:
                temp = li[i]
                li[i]=li[j]
                li[j]=temp
    
    

    
    #print("After sorting String is : ",li)

    del li
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
    print("r[0] : %s"  % r[0:20])
    print("Somme temps : %s" % somme)
    moyenne = somme / nbLigne
    print("Moyenne : %s" % moyenne)
    print("Nb ligne : %s " % nbLigne)

    # on enregistre la moyenne obtenu dans le fichier moytridenombrement.txt
    savepathMoy = str(Path.home()) + '/PycharmProjects/PROJET-TRI/moyLexico'
    completePathMoy = os.path.join(savepathMoy, 'moytrilexico.txt')
    moy = open(completePathMoy, 'a')
    moy.write(str(moyenne) + ',' + str(nbElem) + '\n')
    moy.close()


import csv
import matplotlib.pyplot
import os



def courbe():

    # on affiche la courbe des moyennes selon le nbElem
    x = []
    y = []

    savepathDenombrement = str(Path.home()) +'/PycharmProjects/PROJET-TRI/moyLexico'
    completePathDenombrement = os.path.join(savepathDenombrement, 'moytrilexico.txt')
    # on ouvre le fichier contenant les moyennes selon le nbElem
    with open(completePathDenombrement, 'r') as csvfileDenombrement:
        # on delimite la separation entre la moyenne et le nbElem par une virgule
        plots = csv.reader(csvfileDenombrement, delimiter=',')
        # on attribut les valeurs du nbElem a x et de la moyenne a y
        for row in plots:
            x.append(float(row[1]))
            y.append(float(row[0]))

    

        # on dessine la courbe
        matplotlib.pyplot.plot(x, y, label='Sort', color="b")
        
        matplotlib.pyplot.xlabel('nbElem')
        matplotlib.pyplot.ylabel('Temps')
        matplotlib.pyplot.title('Courbe tri')
        matplotlib.pyplot.legend()
        matplotlib.pyplot.show()

    # on efface les moyenne afin d'afficher une nouvelle courbe
    # avec les nouvelles valeurs
    open(completePathDenombrement, "w").close()
    
   


def lancement(nbLancement,min,pas,max):

    savepathDenombrement = str(Path.home()) +'/PycharmProjects/PROJET-TRI/moyLexico'
    completePathDenombrement = os.path.join(savepathDenombrement, 'moytrilexico.txt')
    
    nbLance = nbLancement 
    while nbLance > 0 :
        print("--------- %d " % nbLance , "-------------")
        open(completePathDenombrement, "w").close() #on supp les anciennes moyenne afin de garder celle du dernier lancement
        val = min
        while val <= max:
            sortLexo(val);
            val += pas

        nbLance -= 1


    
    courbe();
    
    #pathSaveDirectory =str(Path.home()) +'/PycharmProjects/PROJET-TRI/figures'
    #pathSaveFileInDir = os.path.join(pathSaveDirectory, "%s L %s MIN %s PAS %s MAX.png" % ( nbLancement, min ,pas, max))
    
    
    
   # print("TEST -------- %s " % pathSaveFileInDir)
    #matplotlib.pyplot.savefig(pathSaveFileInDir);

   
  






def main():

    lancement(3,500,5000,50500);



main()
