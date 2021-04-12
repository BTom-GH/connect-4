from turtle import*
speed("fastest") #Règle la vitesse du tracé au maximum
ht() #cache la flèche
title("Puissance 4") #Titre de la fenêtre turtle
j=0 #Variable joueur pour définir quel joueur joue
numéro_j=0 #variable qui stocke le numéro du joueur grâce a la variable joueur
   
def carre(x,y,n):
    #dessine un carré, dont la position
    #et la dimension sont données en paramètres
    up()
    goto(x,y)
    down()
    for i in range (4):
        left(90)
        forward(n)
    up()
    return True

def Grille_vide():
    #Crée la liste représentant la grille vide du puissance 4
    global g
    g=[]
    for loop in range (6):
        g.append([0]*7)
    return g

def Coup_possible(g,c):
    #retourne vrai si le coup est possible et faux s'il ne l'est pas
    global l
    if g[l][c-1]==0:
        return True
    else:
        return False

def Jouer(g,j,c):
    #Prend en compte le choix de colonne du joueur et place son pion sur la liste représentant la grille,
    #puis sur la grille dessinée
    global x
    global y
    global l
    x=-300
    y=-250
    l=0
    n=False
    while n!=True:
        if Coup_possible(g,c)==True:
            if (j%2)==0:
                g[l][c-1]=1
                n=True
            else:
                g[l][c-1]=2
                n=True
        else:
            l=l+1
            y=y+100
            n=False
    for loop in range(c-1):
        x=x+100
    goto(x,y)
    pion(j)
    return x and c and y and l
    

def pion(j):
    #dessine un pion dont la couleur change en fonction du joueur
    down()
    if (j%2)==0:
        color("Deep Sky Blue")
    else:
        color("red")
    dot(90)
    up()
    return True


def Horiz(g, j, l, c):
    #Vérifie si dans la ligne "l" 4 pions sont alignés autour de celui de la colonne "c"
    #et renvoie la variable "gagner"
    global gagner
    gagner=0
    i=g[l][c-1]
    if i!=0:
        if (j%2)==0:
            pion=1
        else:
            pion=2
            
        listetest=[]
        listetest=(g[l][c-1:c+3])
        if listetest==[pion,pion,pion,pion]:
            gagner=pion
            return gagner
        else:
            listetest=[]
            listetest=(g[l][c-4:c])
        if listetest==[pion,pion,pion,pion]:
            gagner=pion
            return gagner
        else:
            listetest=[]
            listetest=(g[l][c-3:c+1])
        if listetest==[pion,pion,pion,pion]:
            gagner=pion
            return gagner
        else:
            listetest=[]
            listetest=(g[l][c-2:c+2])
        if listetest==[pion,pion,pion,pion]:
            gagner=pion
            return gagner
        else:
            return gagner

def Verti(g, j, l, c):
    #Verifie si 4 pions sont alignés verticalement dans la colonne "c"
    global gagner
    gagner=0
    i=g[l][c-1]
    if i!=0:
        if (j%2)==0:
            pion=1
        else:
            pion=2
            
        listetest=[]
        for loop in range(4):
            listetest.append(g[l-loop][c-1])
        if listetest==[pion,pion,pion,pion]:
            gagner=pion
            return gagner
    else:
        return gagner
                        
def Diago(g,j,l,c):
    #vérifie si 4 pions sont alignés en diagonale
    global gagner
    gagner=0
    i=0
    j=0
    for l in range (3):
        for c in range (4):
            liste_test=[]
            i=g[l][c]
            if i!=0:
                if (j%2)==0:
                    pion=1
                else:
                    pion=2
                for loop in range (4):
                    j=g[l+loop][c+loop]
                    if i==j:
                        liste_test.append(j)
                if liste_test==[pion,pion,pion,pion]:
                        gagner=pion
                        return gagner
                    
    for l in range (3):
        for c in range (3,6):
            liste_test=[]
            i=g[l][c]
            if i!=0:
                for loop in range (4):
                    j=g[l+loop][c-loop]
                    if i==j:
                        liste_test.append(j)
                if liste_test==[1,1,1,1] or liste_test==[2,2,2,2]:
                        gagner=1
                        return gagner
                    
    return gagner
    
                
            
    
    
def Partie_nulle(g):
    #Vérifie si la grille est pleine, si c'est le cas et affiche "égalité" et renvoie vrai
    global test
    global test2
    compte=0
    for o in g[5]:
            if o==0:
                compte=compte+1
            else:
                compte=compte
    if compte==0:
        test==False
        test2==False
        goto(0,-400)
        color("black")
        write("Egalité !", align="center", font=("arial", 30,"underline"))
        return True
    else:
        return False
                

def Gagner(g,j):
        #prend en compte la variable gagner sortie des fonctions de vérifications
        #et arrête le programme si un gagnant est détecté en affichant son nom
        global test
        global test2
        global l
        global c
        global gagner
        test3=False
        gagner=0
        
        for loop in range(1):
            Horiz(g,j,l,c)
            if gagner!=0:
                break
            Verti(g,j,l,c)
            if gagner!=0:
                break
            Diago(g,j,l,c)
            if gagner!=0:
                break
        
            
            
        if gagner==1:
            gagnant="Joueur 1 a gagné !"
            test==False
            test2==False
            goto(0,-400)
            color("black")
            write(gagnant, align="center", font=("arial", 30,"underline"))
            return True
            
        elif gagner==2:
            gagnant="Joueur 2 a gagné !"
            test==False
            test2==False
            goto(0,-400)
            color("black")
            write(gagnant, align="center", font=("arial", 30,"underline"))
            return True
        else:
            return False

def Affiche_Grille() :
    #crée la grille sur turtle
    global x
    global y
    tracer(0,0)
    setup(1720, 1080)
    bgpic("grille_pss4.png")
    y=-400
    for loop in range(6):
        x=350
        y=y+100
        carre(x,y,100)
        for loop in range(6):
            x=x-100
            carre(x,y,100)
    update()
    return x and y

#appelle la fonction qui crée la liste représentant la grille
Grille_vide()
#appelle la fonction qui crée la grille sur turtle
Affiche_Grille()




#Boucle qui tourne tant que la grille n'est pas pleine ou que la boucle soit break
while Partie_nulle(g)!=True:
    test=True
    test2=True
    while test==True:
        while test2==True:
            if j%2==0:
                numéro_j=1
            else:
                numéro_j=2
            #Demande la colonne dans laquelle le joueur veut jouer
            c=numinput(("Coup du joueur",numéro_j),"Entrez le numéro de colonne compris entre 1 et 7,\n 1 étant le plus a gauche et 7 le plus a droite.")
           #vérifie la colonne
            if c==None:
                print("Veuillez entrer un nombre valable")
            else:
                test2=False
                
        c=int(c)
        if c<1 or c>7:
            print("Veuillez entrer un nombre valable")
            test2=True
        
        if test2==False:        
            try:
                Jouer(g,j,c)
                test=False
            except IndexError:
                print("Veuillez choisir une autre colonne")
                test2=True
    #Appelle la fonction gagner et break si elle renvoie vrai         
    if Gagner(g,j)==True:
        break

    #ajoute +1 à la variable joueur et donc passe au joueur suivant
    else:
        j=j+1
       


        
