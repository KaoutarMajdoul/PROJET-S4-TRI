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
import re
from pathlib import Path

def comparer( mot1 , mot2 ):
    if ord( mot1[0] ) < ord( mot2[0] ) :
        return mot1
    if ord( mot1[0] ) > ord( mot2[0] ) :
        return mot2
    else :
        if len( mot1 ) == 1 :
            return mot1
        if len( mot2 ) == 1 :
            return mot2
        else :
            tmp1 = mot1[1:]
            tmp2 = mot2[1:]
            if comparer( tmp1 , tmp2 ) == tmp1 :
                return mot1
            else :
                return mot2


def sortLexo(nbElem):
    start_time = time.time() # enregistre le temps de départ
    listwords = ["".join(random.choice(ascii_letters) # choisi une lettre au hasard (le join va permettre de créer un mot(joindre les lettres))
                         for j in range(random.randint(1,3)) ) # nombre de lettres dans le mot (choisi au hasard)
                 for i in range(nbElem) ] # nombre de mots dans la liste à trier
   # print( listwords)
    # tri les mots de la liste dans l'odre lexicographique
  
    x = len(listwords)
   
    
    #on récupère la représentation ascii de la 1ere lettre de chaque mot du tableau
    #ord transforme un caracère en nb ascii
    ascii = [ ord( listwords[i][0] ) for i in range( nbElem ) ]
    
    #on remplit le tableau de 0 
    nbOccurrences = [ 0 for i in range ( max( ascii ) ) ]
    buckets = [ [] for i in range ( max( ascii ) ) ]
    
    
    #On met chaque élément du tableau dans l'indice associé du tableau buckets
    #le tri s'effectue quand on met l'element du tableau dans l'indice associé dans 
    #buckets
    for i in range( nbElem ) : #complexité en O(n) où n = nbElem
        nbOccurrences[ ascii [ i ] - 1 ] += 1
        buckets[ ascii [ i ] - 1 ] . append( listwords[ i ] )
    
    res = []
    
    #on parcourt buckets et on récupére les éléments != 0 
    for i in range( 0 , max( ascii ) ) : #complexité constante car max ascii = 255
        while nbOccurrences[i] != 0 : #Tq on a plusieurs fois la mm première lettre
            res.append(buckets[i].pop())  # on ajoute le prochain elmnt de buckets dans le tab res
            nbOccurrences[i] -= 1 #on décremente nbOccurence de la premiere lettre du mot
            if len( res ) >= 2 : #si la taille du tab res >= 2 
                j = 1 # position du derniere element inséré (dans le sens inverse du tableau)
                
                #Quand on a plusieurs fois la mm lettre on compare le caractére suivant
                #et si encore mm caractere on compare jusqu'à la fin du mot 
                while j <= ( len( res ) - 1 ) and res[ len(res) - j ][0]==res[ len(res) - j - 1 ][0] and comparer( res[ len(res) - j ] , res[ len(res) - j - 1 ] ) == res[ len(res) - j ] :
                    
                     #quand l'ordre alphabétique n'est pas correcte on échange 
                    tmp = res[ len(res) - j ]
                    res[ len(res) - j ] = res[ len(res) - j - 1 ]
                    res[ len(res) - j - 1 ] = tmp
                    j += 1 #on incrémente la position du dernier elemt ajouter chaque fois qu'on ajoute un elemt
    print( res )
    tempsEc = time.time() - start_time;
  
    tempsMaxVal = nbElem / tempsEc



    print("TRI LEXICO")
    print("Nb elem : %d " % nbElem)
    print("Temps d'execution : %s secondes" % (tempsEc))

    # écrit le temps écoulé dans le fichier [nbElem]trilexico.csv
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
        somme += float(r[0:])
        nbLigne += 1
    # print("Somme temps : %s" % somme)
    moyenne = somme / nbLigne
    # print("Moyenne : %s" % moyenne)
    # print("Nb valeur : %s " % nbLigne)

    # on enregistre la moyenne obtenu dans le fichier moytrilexico.txt
    savepathMoy = str(Path.home()) + '/PycharmProjects/PROJET-TRI/moyLexico'
    completePathMoy = os.path.join(savepathMoy, 'moytrilexico.txt')
    moy = open(completePathMoy, 'a')
    moy.write(str(moyenne) + ',' + str(nbElem) + '\n')
    moy.close()




    ####################MEMOIRE#########################

    #calcul moyenne memoire

    savepathMem =  str(Path.home()) + '/PycharmProjects/PROJET-TRI/tempsLexico'
    completePathMem = os.path.join(savepathMem, '%dmemlexico.txt ' % nbElem)
    m = open(completePathMem, 'a')
    m.write(str(tempsMaxVal) + '\n')
    m.close()




import csv
import matplotlib.pyplot
import os



def courbe():

    # on affiche la courbe des moyennes selon le nbElem
    x = []
    y = []

    savepathLexico = str(Path.home()) +'/PycharmProjects/PROJET-TRI/moyLexico'
    completePathLexico = os.path.join(savepathLexico, 'moytrilexico.txt')
    # on ouvre le fichier contenant les moyennes selon le nbElem
    with open(completePathLexico, 'r') as csvfileLexico:
        # on delimite la separation entre la moyenne et le nbElem par une virgule
        plots = csv.reader(csvfileLexico, delimiter=',')
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
    open(completePathLexico, "w").close()
    
   

    ####################MEMOIRE#########################

    #calcul moyenne memoire

    savepathMem =  str(Path.home()) + '/PycharmProjects/PROJET-TRI/tempsLexico'
    completePathMem = os.path.join(savepathMem, '%dmemlexico.txt ' % nbElem)
    m = open(completePathMem, 'a')
    m.write(str(tempsMaxVal) + '\n')
    m.close()


#

def courbeLexico():
   # on affiche la courbe des moyennes selon le nbElem
    x = []
    y = []

    savepathLexico = str(Path.home()) +'/PycharmProjects/PROJET-TRI/moyLexico/'
    completePathLexico = os.path.join(savepathLexico, 'moytrilexico.txt')
    #on ouvre le fichier contenant les moyennes selon le nbElem
    with open(completePathLexico, 'r') as csvfileLexico:
       # on delimite la separation entre la moyenne et le nbElem par une virgule
        plots = csv.reader(csvfileLexico, delimiter=',')
        #on attribut les valeurs du nbElem a x et de la moyenne a y
        for row in plots:
            x.append(float(row[1]))
            y.append(float(row[0]))



      #  on dessine la courbe
        matplotlib.pyplot.plot(x, y, label='tri lexico', color="b")

        matplotlib.pyplot.xlabel('nbElem')
        matplotlib.pyplot.ylabel('Temps (s)')
        matplotlib.pyplot.title('Courbe tri')
        matplotlib.pyplot.legend()
        matplotlib.pyplot.show()

        # on efface les moyenne afin d'afficher une nouvelle courbe
         #avec les nouvelles valeurs
    open(completePathLexico, "w").close()






def courbeLexicoMemoire():

    #on affiche la courbe des moyennes selon le nbElem
    x = []
    y = []

    savepathLexicomem = str(Path.home()) +'/PycharmProjects/PROJET-TRI/moyLexico/'
    completePathLexicomem = os.path.join(savepathLexicomem, 'memtrilexico.txt')
    #on ouvre le fichier contenant les moyennes selon le nbElem
    with open(completePathLexicomem, 'r') as csvfileLexicomem:
       # on delimite la separation entre la moyenne et le nbElem par une virgule
        plots = csv.reader(csvfileLexicomem, delimiter=',')
       # on attribut les valeurs du nbElem a x et de la moyenne a y
        for row in plots:
            x.append(float(row[1]))
            y.append(float(row[0]))



      #  on dessine la courbe
        matplotlib.pyplot.plot(x, y, label='tri lexico mem', color="r")

        matplotlib.pyplot.xlabel('nbElem')
        matplotlib.pyplot.ylabel('temps / maxVal')
        matplotlib.pyplot.title('Courbe tri')
        matplotlib.pyplot.legend()
        matplotlib.pyplot.show()

        # on efface les moyenne afin d'afficher une nouvelle courbe
        # avec les nouvelles valeurs
    open(completePathLexicomem, "w").close()




def lancementLexico(nbLancement,min,pas,max):
    savepathLexico = str(Path.home()) +'/PycharmProjects/PROJET-TRI/moyLexico/'
    completePathLexico = os.path.join(savepathLexico, 'moytrilexico.txt')

    nbLance = nbLancement

    while nbLance > 0 :
        print("--------- %d " % nbLance , "-------------")
        open(completePathLexico, "w").close() #on supp les anciennes moyenne afin de garder celle du dernier lancement
        val = min
        while val <= max:
            sortLexo(val);
            
            
            

            val += pas

        nbLance -= 1


    ##################MEMOIRE#########################
    savepathMem =  str(Path.home()) + '/PycharmProjects/PROJET-TRI/tempsLexico'
    minD= min
    maxD = max
    pasD = pas

    while minD < maxD :
        minD += pasD

        completePathMem = os.path.join(savepathMem, '%dmemlexico.txt ' % minD)



        sommeMem = 0
        moyenneMem = 0
        nbLigneMem = 0

       # on ouvre le fichier contenant les temps en lecture
        cr = (open(completePathMem, "r"))

       # pour chaque élément de la colonne r, on additionne les valeur et on
        #incrémente le nbLigne afin de calculer la moyenne
        for r in cr:  # r = colone
            sommeMem += float(r[0:])
            nbLigneMem += 1
        print("Somme temps : %s" % sommeMem)
        moyenneMem = sommeMem / nbLigneMem
        print("Moyenne : %s" % moyenneMem)
        print("Nb valeur : %s " % nbLigneMem)

        #on enregistre la moyenne obtenu dans le fichier moytrilexico.txt
        savepathMoymem = str(Path.home()) + '/PycharmProjects/PROJET-TRI/moyLexico'
        completePathMoymem = os.path.join(savepathMoymem, 'memtrilexico.txt')
        moymem = open(completePathMoymem, 'a')
        moymem.write(str(moyenneMem) + ',' + str(minD) + '\n')
        moymem.close()

    #####################################



    courbeLexico();
    #courbeLexicoMemoire();
    pathSaveDirectory =str(Path.home()) +'/PycharmProjects/PROJET-TRI/figures'
    pathSaveFileInDir = os.path.join(pathSaveDirectory, "TRILEXICO%s L %s MIN %s PAS %s MAX.png" % ( nbLancement, min ,pas, max))


    pathSaveDirectory =str(Path.home()) +'/PycharmProjects/PROJET-TRI/figures'
    pathSaveFileInDir = os.path.join(pathSaveDirectory, "MEMOIRETRILEXICO%s L %s MIN %s PAS %s MAX.png" % ( nbLancement, min ,pas, max))



    print("TEST -------- %s " % pathSaveFileInDir)
    matplotlib.pyplot.savefig(pathSaveFileInDir);






def main():
    #lancement(5,500,5000,50500);

    #lancementLexico(1,50,100,1050);
    
    sortLexo(60);
    
    #print ( comparer( "j" , "jn" ) );
    
    


main()
