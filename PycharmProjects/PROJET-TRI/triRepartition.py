import random

def bucket_sort(nbElem):

    alist = random.sample(range(1000), nbElem)
    largest = max(alist)
    length = len(alist)
    size = largest/length

    buckets = [[0 for i in range(largest+1)] for _ in range(length+1)]
    # bucket de  taille largest +1 
    # liste de longeur max de liste
    # chaque fois on ajoute un a l'indice de l'elemnt de alist  
	
    for i in range(length):
        j = int(alist[i]/size)
        buckets[j][alist[i]] += 1

    result = []

    for i in range(length):
    # on parcourt bucket et si chaque elemnt != 0 on met indice dans liste resultat
        for j in range(largest):
        # on ajoute l'elem different de 0 
            while buckets[i][j] != 0 :
                result.append(j)
                buckets[i][j] -= 1

    return result

    #calcul de la moyenne du temps d'exécution de l'algo
    somme = 0
    moyenne = 0
    nbLigne = 0
    cr = csv.reader(open("%dmoyRepartition.csv" %nbElem, "r"))
    for r in cr: #r = colonne
        somme  += float(r[0:20])
        nbLigne += 1
    print("Somme temps : %s" % somme)
    moyenne = somme / nbLigne
    print("Moyenne : %s" % moyenne)
    print("Nb valeur : %s " % nbLigne)
    
    #stockage du temps moyen dans un fichier
    moy = open('%dmoyRepartition.csv' % nbElem, 'w')
    moy.write(str(moyenne) + '\n')
    moy.close()


### EXPLICATION ###
	# 1/ On va faire le quotient pour chaque nombre, entre le nombre et la taille du tableau
	# 2/ Ca va créer un tableau avec les quotients, et pour chaque quotient le tableau va être trié dans l'ordre
	# 3/ On concatène

def main():

    sorted_list = bucket_sort(10)
    print('Sorted list: ', end='')
    print(sorted_list)

if __name__ == "__main__":
    # execute only if run as a script
    main()
	
