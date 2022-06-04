import random
from math import *

Predefinie = input("Voulez vous utilisez la liste d'élèves prédéfinies ? Y or N ")
while Predefinie not in ['Y','N']:
    Predefinie = input("Voulez vous utilisez la liste d'élèves prédéfinies ? Y or N ")

if Predefinie == "Y":
    Effectif_filles = 5
    Liste_Filles = ['Maelle','Berangere','Linda','Pascale','Justine']
    Effectif_garcons = 8
    Liste_Garcons = ['Caesar','Eric','Rudy','Randolf','Mohammed','Allan','Rayan','Yvan']
    Effectif_total = Effectif_filles+Effectif_garcons
elif Predefinie == "N":
    Effectif_filles = int(input("Entrez le nombre de filles "))
    Effectif_garcons = int(input("Entrez le nombre de garcons "))
    Effectif_total = Effectif_filles+Effectif_garcons
    Liste_Filles=[]
    Liste_Garcons=[]
    for i in range(0,Effectif_filles):
        Nom = input("Entrer le nom d'UNE eleve ")
        Liste_Filles.append(Nom)
        
    for i in range(0,Effectif_garcons):
        Nom = input("Entrer le nom d'UN eleve ")
        Liste_Garcons.append(Nom)

Absent = input("Est ce qu'il y a des absents ? Y or N ")
while Absent not in ['Y','N']:
    Absent = input("Est ce qu'il y a des absents ? Entrer Y ou N ")

if Absent == 'Y':
    Nombre_absent = int(input("Il y a combien d'absents ? "))
    while Nombre_absent not in range(1,(Effectif_total+1)):
        Nombre_absent = int(input(f"Entrer un nombre correct d'absents ( compris entre 1 et {(Effectif_total+1)}) "))
    Effectif_total = Effectif_total - Nombre_absent
    if Effectif_total == 0:
        print("La CLASSE ENTIERE est ASBENTE")

    Nombre_fille_absent = int(input("Il y a combien de filles absentes ? "))
    while Nombre_fille_absent not in range(1,(Effectif_filles+1)):
        Nombre_fille_absent = int(input(f"Entrer un nombre correct d'absents ( compris entre 1 et {(Effectif_filles+1)}) "))
    Effectif_filles = Effectif_filles - Nombre_fille_absent

    if Nombre_fille_absent == Nombre_absent:
        print("TOUT les absents sont des filles, TOUT les GARCONS sont PRESENTS")
        Nombre_garcon_absent = 0

    else :
        Nombre_garcon_absent = int(input("Il y a combien de garcons absents ? "))
        while Nombre_garcon_absent not in range(1,(Effectif_garcons+1)):
            Nombre_garcon_absent = int(input(f"Entrer un nombre correct d'absents ( compris entre 1 et {(Effectif_garcons+1)}) "))
        Effectif_garcons = Effectif_garcons - Nombre_garcon_absent
    
        if Nombre_garcon_absent == Nombre_absent:
            print("TOUT les absents sont des garcons, TOUTES les FILLES sont PRESENTES")
            Nombre_fille_absent = 0

    print(f"Il y a {Nombre_absent} absents. ")
    print(f"Il y a {Nombre_fille_absent} filles absentes. ")
    print(f"Il y a {Nombre_garcon_absent} garcons absents. ")

    Liste_filles_absentes = []
    for i in range(1,(Nombre_fille_absent+1)):     
        Fille_absente= input("Entrer correctement le nom d'une des filles absente ")
        while Fille_absente not in Liste_Filles :
            Fille_absente = input("Le nom entré est incorrect, faites attention et recommencer")
        Liste_filles_absentes.append(Fille_absente)
        Liste_Filles.remove(Fille_absente)
    print(f"La liste de filles absentes est la suivante : {Liste_filles_absentes} ")

    if Nombre_garcon_absent > 0 :
        Liste_garcons_absents = []  
        for i in range in range(1,(Nombre_garcon_absent+1)):        
            Garcon_absent= input("Entrer correctement le nom d'un des garcons absent. ")
            while Garcon_absent not in Liste_Filles :
                Garcon_absent = input("Le nom entré est incorrect, faites attention et recommencer")
            Liste_garcons_absents.append(Garcon_absent)
            Liste_Garcons.remove(Garcon_absent)
        print(f"La liste de garcons absents est la suivante : {Liste_garcons_absents} ")
        
print(f"La liste de filles presents est la suivante : {Liste_Filles} ")
print(f"La liste de garcons presents est la suivante : {Liste_Garcons} ")
print(f"Il y a un effectif total de {Effectif_total} personnes , {Effectif_garcons} garcons et {Effectif_filles} filles")

Nombres_groupe = int(input("Nombre de groupe "))

while Nombres_groupe>max(len(Liste_Garcons),len(Liste_Filles)):
    Nombres_groupe = int(input(f"Changer le nombre de groupe, sa valeur maximale doit etre {max(len(Liste_Garcons),len(Liste_Filles))} "))
 
Nombre_eleve_groupe= Effectif_total // Nombres_groupe

if Nombres_groupe <= Effectif_filles: 
    Nombre_fille_groupe= Effectif_filles // Nombres_groupe
    print(f"Il y aura au moins {Nombre_fille_groupe} filles par groupe ")

if Nombres_groupe <= Effectif_garcons:
    Nombre_garcon_groupe= Effectif_garcons // Nombres_groupe
    print(f"Il y aura au moins {Nombre_garcon_groupe} garcons par groupe ")


Liste = [ [] for i in range(0,Nombres_groupe)    ]

print(f"La liste de départ est la suivante : {Liste}")


while Liste_Garcons != [] :

    for j in range(0,Nombres_groupe):
        if len(Liste_Garcons) > 0 : 
            garcon_random = random.choice(Liste_Garcons)
            Liste[j].append(garcon_random)
            Liste_Garcons.remove(garcon_random)

while Liste_Filles != []:

    for j in range(0,Nombres_groupe):
        if len(Liste_Filles) > 0 : 
            fille_random = random.choice(Liste_Filles)
            Liste[j].append(fille_random)
            Liste_Filles.remove(fille_random)

print(Liste)
print(f"  La liste de Garcons restants est : {Liste_Garcons}  ") 
print(f"  La liste de Filles restantes est : {Liste_Filles} ")