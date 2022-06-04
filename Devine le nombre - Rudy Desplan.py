#Devine le nombre
import random
Nombre_ordi = random.randint(1,100)
Nombre_utilisateur = int(input("Entrer un nombre ENTIER compris entre 1 et 100 "))

while Nombre_utilisateur <1 or Nombre_utilisateur>100:
    print("Le numéro entré n'est pas valide, entrer un nouveau numéro")
    Nombre_utilisateur=int(input("Entrer un nombre ENTIER compris entre 1 et 100 "))

while Nombre_utilisateur != Nombre_ordi:
    if Nombre_utilisateur < Nombre_ordi:
        print("Le numéro choisi est inférieur à celui de l'ordinateur")
        Nombre_utilisateur = int(input("Entrer un autre numérooo "))
    elif Nombre_utilisateur > Nombre_ordi :
        print("Le numéro choisi est supérieur à celui de l'ordinateur")
        Nombre_utilisateur = int(input("Entrer un autre numérooo "))
print("BINGOO vous avez trouvez le bon numéro")