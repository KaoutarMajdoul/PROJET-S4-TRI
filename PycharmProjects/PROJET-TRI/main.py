

mport csv
import matplotlib.pyplot
import os
import pathlib
from pathlib import Path
import tridenombrement
import tripaquet
import tribase
import trilexico

def courbe():

    # on affiche la courbe des moyennes selon le nbElem
    x = []
    y = []

    savepathDenombrement = str(Path.home()) +'/PycharmProjects/PROJET-TRI/moyDenombrement'
    completePathDenombrement = os.path.join(savepathDenombrement, 'moytridenombrement.txt')
    # on ouvre le fichier contenant les moyennes selon le nbElem
    with open(completePathDenombrement, 'r') as csvfileDenombrement:
        # on delimite la separation entre la moyenne et le nbElem par une virgule
        plots = csv.reader(csvfileDenombrement, delimiter=',')
        # on attribut les valeurs du nbElem a x et de la moyenne a y
        for row in plots:
            x.append(float(row[1]))
            y.append(float(row[0]))

    c = []
    d = []

    savepathPaquet = str(Path.home()) + '/PycharmProjects/PROJET-TRI/moyPaquet'
    completePathPaquet = os.path.join(savepathPaquet, 'moytripaquet.txt')
    # on ouvre le fichier contenant les moyennes selon le nbElem
    with open(completePathPaquet, 'r') as csvfilePaquet:
        # on delimite la separation entre la moyenne et le nbElem par une virgule
        plots = csv.reader(csvfilePaquet, delimiter=',')
        # on attribut les valeurs du nbElem a x et de la moyenne a y
        for row in plots:
            c.append(float(row[1]))
            d.append(float(row[0]))

    a=[]
    b=[]

    savepathLexico = str(Path.home()) + '/PycharmProjects/PROJET-TRI/moyLexico'
    completePathLexico = os.path.join(savepathLexico, 'moytrilexico.txt')
    # on ouvre le fichier contenant les moyennes selon le nbElem
    with open(completePathLexico, 'r') as csvfileLexico:
        # on delimite la separation entre la moyenne et le nbElem par une virgule
        plots = csv.reader(csvfileLexico, delimiter=',')
        # on attribut les valeurs du nbElem a x et de la moyenne a y
        for row in plots:
            a.append(float(row[1]))
            b.append(float(row[0]))

        # on dessine la courbe
        matplotlib.pyplot.plot(x, y, label='Denombrement', color="b")
        matplotlib.pyplot.plot(a, b, label="Lexico", color="r")
        matplotlib.pyplot.plot(c, d, label="Paquet", color="g")
        matplotlib.pyplot.xlabel('nbElem')
        matplotlib.pyplot.ylabel('Temps')
        matplotlib.pyplot.title('Courbe tri')
        matplotlib.pyplot.legend()
        matplotlib.pyplot.show()

    # on efface les moyenne afin d'afficher une nouvelle courbe
    # avec les nouvelles valeurs
    open(completePathDenombrement, "w").close()
    open(completePathLexico, "w").close()
    open(completePathPaquet, "w").close()
    
   


def lancement(nbLancement,min,pas,max):

    savepathDenombrement = str(Path.home()) +'/PycharmProjects/PROJET-TRI/moyDenombrement'
    completePathDenombrement = os.path.join(savepathDenombrement, 'moytridenombrement.txt')

    savepathLexico = str(Path.home()) + '/PycharmProjects/PROJET-TRI/moyLexico'
    completePathLexico = os.path.join(savepathLexico, 'moytrilexico.txt')

    savepathPaquet = str(Path.home()) + '/PycharmProjects/PROJET-TRI/moyPaquet'
    completePathPaquet = os.path.join(savepathPaquet, 'moytripaquet.txt')
    
    nbLance = nbLancement 
    while nbLance > 0 :
        print("--------- %d " % nbLance , "-------------")
        open(completePathDenombrement, "w").close() #on supp les anciennes moyenne afin de garder celle du dernier lancement
        open(completePathLexico, "w").close()
        open(completePathPaquet, "w").close()
        val = min
        while val <= max:
            tridenombrement.counting_sort(val);
            trilexico.sortLexo(val);
            tripaquet.bucket_sort(val);
            val += pas

        nbLance -= 1


    
    courbe();
    
    pathSaveDirectory =str(Path.home()) +'/PycharmProjects/PROJET-TRI/figures'
    pathSaveFileInDir = os.path.join(pathSaveDirectory, "%s L %s MIN %s PAS %s MAX.png" % ( nbLancement, min ,pas, max))
    
    
    
    print("TEST -------- %s " % pathSaveFileInDir)
    matplotlib.pyplot.savefig(pathSaveFileInDir);
    
    
    
    
    
    
    
def courbeBase():

    # on affiche la courbe des moyennes selon le nbElem
    x = []
    y = []

    savepathBase = str(Path.home()) +'/PycharmProjects/PROJET-TRI/moyBase'
    completePathBase = os.path.join(savepathBase, 'moytribase.txt')
    # on ouvre le fichier contenant les moyennes selon le nbElem
    with open(completePathBase, 'r') as csvfileBase:
        # on delimite la separation entre la moyenne et le nbElem par une virgule
        plots = csv.reader(csvfileBase, delimiter=',')
        # on attribut les valeurs du nbElem a x et de la moyenne a y
        for row in plots:
            x.append(float(row[1]))
            y.append(float(row[0]))

    

        # on dessine la courbe
        matplotlib.pyplot.plot(x, y, label='tri base', color="b")
        
        matplotlib.pyplot.xlabel('nbElem')
        matplotlib.pyplot.ylabel('Temps')
        matplotlib.pyplot.title('Courbe tri')
        matplotlib.pyplot.legend()
        matplotlib.pyplot.show()

         # on efface les moyenne afin d'afficher une nouvelle courbemport csv
import matplotlib.pyplot
import os
import pathlib
from pathlib import Path
import tridenombrement
import tripaquet
import tribase
import trilexico

def courbe():

    # on affiche la courbe des moyennes selon le nbElem
    x = []
    y = []

    savepathDenombrement = str(Path.home()) +'/PycharmProjects/PROJET-TRI/moyDenombrement'
    completePathDenombrement = os.path.join(savepathDenombrement, 'moytridenombrement.txt')
    # on ouvre le fichier contenant les moyennes selon le nbElem
    with open(completePathDenombrement, 'r') as csvfileDenombrement:
        # on delimite la separation entre la moyenne et le nbElem par une virgule
        plots = csv.reader(csvfileDenombrement, delimiter=',')
        # on attribut les valeurs du nbElem a x et de la moyenne a y
        for row in plots:
            x.append(float(row[1]))
            y.append(float(row[0]))

    c = []
    d = []

    savepathPaquet = str(Path.home()) + '/PycharmProjects/PROJET-TRI/moyPaquet'
    completePathPaquet = os.path.join(savepathPaquet, 'moytripaquet.txt')
    # on ouvre le fichier contenant les moyennes selon le nbElem
    with open(completePathPaquet, 'r') as csvfilePaquet:
        # on delimite la separation entre la moyenne et le nbElem par une virgule
        plots = csv.reader(csvfilePaquet, delimiter=',')
        # on attribut les valeurs du nbElem a x et de la moyenne a y
        for row in plots:
            c.append(float(row[1]))
            d.append(float(row[0]))

    a=[]
    b=[]

    savepathLexico = str(Path.home()) + '/PycharmProjects/PROJET-TRI/moyLexico'
    completePathLexico = os.path.join(savepathLexico, 'moytrilexico.txt')
    # on ouvre le fichier contenant les moyennes selon le nbElem
    with open(completePathLexico, 'r') as csvfileLexico:
        # on delimite la separation entre la moyenne et le nbElem par une virgule
        plots = csv.reader(csvfileLexico, delimiter=',')
        # on attribut les valeurs du nbElem a x et de la moyenne a y
        for row in plots:
            a.append(float(row[1]))
            b.append(float(row[0]))

        # on dessine la courbe
        matplotlib.pyplot.plot(x, y, label='Denombrement', color="b")
        matplotlib.pyplot.plot(a, b, label="Lexico", color="r")
        matplotlib.pyplot.plot(c, d, label="Paquet", color="g")
        matplotlib.pyplot.xlabel('nbElem')
        matplotlib.pyplot.ylabel('Temps')
        matplotlib.pyplot.title('Courbe tri')
        matplotlib.pyplot.legend()
        matplotlib.pyplot.show()

    # on efface les moyenne afin d'afficher une nouvelle courbe
    # avec les nouvelles valeurs
    open(completePathDenombrement, "w").close()
    open(completePathLexico, "w").close()
    open(completePathPaquet, "w").close()
    
   


def lancement(nbLancement,min,pas,max):

    savepathDenombrement = str(Path.home()) +'/PycharmProjects/PROJET-TRI/moyDenombrement'
    completePathDenombrement = os.path.join(savepathDenombrement, 'moytridenombrement.txt')

    savepathLexico = str(Path.home()) + '/PycharmProjects/PROJET-TRI/moyLexico'
    completePathLexico = os.path.join(savepathLexico, 'moytrilexico.txt')

    savepathPaquet = str(Path.home()) + '/PycharmProjects/PROJET-TRI/moyPaquet'
    completePathPaquet = os.path.join(savepathPaquet, 'moytripaquet.txt')
    
    nbLance = nbLancement 
    while nbLance > 0 :
        print("--------- %d " % nbLance , "-------------")
        open(completePathDenombrement, "w").close() #on supp les anciennes moyenne afin de garder celle du dernier lancement
        open(completePathLexico, "w").close()
        open(completePathPaquet, "w").close()
        val = min
        while val <= max:
            tridenombrement.counting_sort(val);
            trilexico.sortLexo(val);
            tripaquet.bucket_sort(val);
            val += pas

        nbLance -= 1


    
    courbe();
    
    pathSaveDirectory =str(Path.home()) +'/PycharmProjects/PROJET-TRI/figures'
    pathSaveFileInDir = os.path.join(pathSaveDirectory, "%s L %s MIN %s PAS %s MAX.png" % ( nbLancement, min ,pas, max))
    
    
    
    print("TEST -------- %s " % pathSaveFileInDir)
    matplotlib.pyplot.savefig(pathSaveFileInDir);
    
    
    
    
    
    
    
def courbeBase():

    # on affiche la courbe des moyennes selon le nbElem
    x = []
    y = []

    savepathBase = str(Path.home()) +'/PycharmProjects/PROJET-TRI/moyBase'
    completePathBase = os.path.join(savepathBase, 'moytribase.txt')
    # on ouvre le fichier contenant les moyennes selon le nbElem
    with open(completePathBase, 'r') as csvfileBase:
        # on delimite la separation entre la moyenne et le nbElem par une virgule
        plots = csv.reader(csvfileBase, delimiter=',')
        # on attribut les valeurs du nbElem a x et de la moyenne a y
        for row in plots:
            x.append(float(row[1]))
            y.append(float(row[0]))

    

        # on dessine la courbe
        matplotlib.pyplot.plot(x, y, label='tri base', color="b")
        
        matplotlib.pyplot.xlabel('nbElem')
        matplotlib.pyplot.ylabel('Temps')
        matplotlib.pyplot.title('Courbe tri')
        matplotlib.pyplot.legend()
        matplotlib.pyplot.show()

         # on efface les moyenne afin d'afficher une nouvelle courbe
         # avec les nouvelles valeurs
    open(completePathBase, "w").close()
        
        
        
        
def lancementBase(nbLancement,min,pas,max):
    savepathBase = str(Path.home()) +'/PycharmProjects/PROJET-TRI/moyBase'
    completePathBase = os.path.join(savepathBase, 'moytribase.txt')
    
    nbLance = nbLancement 
    while nbLance > 0 :
        print("--------- %d " % nbLance , "-------------")
        open(completePathBase, "w").close() #on supp les anciennes moyenne afin de garder celle du dernier lancement
        val = min
        while val <= max:
            tribase.radixSort(val);
            val += pas

        nbLance -= 1


    
    courbeBase();
   
  






def main():
    
   # lancement(5,50,10,70);

    lancementBase(1,1000,10000,100000);

main()

         # avec les nouvelles valeurs
    open(completePathBase, "w").close()
        
        
        
        
def lancementBase(nbLancement,min,pas,max):
    savepathBase = str(Path.home()) +'/PycharmProjects/PROJET-TRI/moyBase'
    completePathBase = os.path.join(savepathBase, 'moytribase.txt')
    
    nbLance = nbLancement 
    while nbLance > 0 :
        print("--------- %d " % nbLance , "-------------")
        open(completePathBase, "w").close() #on supp les anciennes moyenne afin de garder celle du dernier lancement
        val = min
        while val <= max:
            tribase.radixSort(val);
            val += pas

        nbLance -= 1


    
    courbeBase();
   
  






def main():
    
   # lancement(5,50,10,70);

    lancementBase(1,1000,10000,100000);

main()

