#!/usr/bin/env python
import random
import time

 
def radixSort(nbElem): #on définit une fonction qui prend en paramètre nbElem
    start_time = time.time()
    list_vals = random.sample(range(1000),nbElem) #on créé une liste de nbElem éléments de valeurs aléatoires inférieures ou égale à 1000
    maxLength = False  #On initialise maxLenght à False qui est vrai si on est sur le dernier placement 
    tmp = -1            #On initialise tmp à -1 
    placement = 1      #On initialise placement à 1 qui indique le placement dans notre chiffre

    
    while not maxLength: 
        maxLength = True
        buckets = [list() for _ in range( 10 )] # On créé un tableau de 10 tableaux
        # Parcours list_val et saisie les valeurs dans les buckets
        for i in list_vals:                     
            tmp = int(i / placement)
            buckets[tmp % 10].append(i) 
            if maxLength and tmp > 0:  
                maxLength = False            

        a = 0
        #Parcours buckets et saisie les valeurs dans list_val
        for b in range( 10 ):
            buck = buckets[b]

            for i in buck:
                list_vals[a] = i
                a += 1
    
        placement *= 10
    print(list_vals);
tempsEc = time.time() - start_time;
    print("Temps d'execution : %s secondes" % (tempsEc))
    
    
    f = open( '%dtribase.txt' %nbElem, 'a' )
    f.write( str(tempsEc) + '\n' )
    f.close() 
        
    


def main():
    radixSort(25);

if __name__ == "__main__":

    main()
