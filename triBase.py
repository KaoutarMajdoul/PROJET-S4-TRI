#!/usr/bin/env python
import random
import time

 
def radixSort(nbElem):        
    start_time = time.time()
    list_vals = random.sample(range(1000),nbElem)    #On créé une liste de nbElem éléments de valeurs aléatoires inférieures ou égale à 1000
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
        print(list_vals)





    tempsEc = time.time() - start_time;
    print("Temps d'execution : %s secondes" % (tempsEc))
    
    
    f = open( '%dtribase.txt' %nbElem, 'a' )
    f.write( str(tempsEc) + '\n' )
    f.close() 
        
    


def main():
    radixSort(25);

if __name__ == "__main__":

    main()
