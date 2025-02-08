#!/usr/bin/env python3

# On demande deux nombres à l'utilisateur
nombre1 = input("Entrez un premier nombre : ")
nombre2 = input("Entrez un second nombre : ")

# On vérifie que ce que l'utilisateur a tapé est bien deux chaînes numériques. Si c'est le cas, on les convertit en "vrais" entiers.
if nombre1.isnumeric() == False or nombre2.isnumeric() == False:
    raise SystemExit("Fin du programme : une des deux valeurs non numérique")

nombre1 = int(nombre1)
nombre2 = int(nombre2)

# On demande à l'utilisateur quelle opération veut-il faire
operateur = input("Quelle opération souhaitez-vous faire (+ - * /) ? ")

if operateur not in ("+", "-", "*", "/"):
    raise SystemExit("Fin du programme : opération inconnue")

# On applique l'opérateur demandé
resultat = None # Pour créer une variable resultat vide
if operateur == "+":
    resultat = nombre1 + nombre2

elif operateur == "-":
    resultat = nombre1 - nombre2

elif operateur == "*":
    resultat = nombre1 * nombre2

elif operateur == "/":

    # On vérifie qu'on ne cherche pas à diviser par zéro
    if nombre2 == 0:
        raise SystemExit("Fin du programme : division par zéro impossible")

    # On voit avec l'utilisateur pour l'arrondi
    arrondi = input("A combien de chiffres après la virgule voulez-vous arrondir ? ")

    # On vérifie que l'utilisateur a bien donné un arrondi numérique
    if arrondi.isnumeric() == False:
        raise SystemError("Fin du programme : arrondi non numérique")
    # On transforme la variable arrondi en int
    arrondi = int(arrondi)

    # On vérifie que l'arrondi est supérieur ou égal à zéro
    if arrondi < 0:
        raise SystemExit("Fin du programme : arrondi invalide")
    
    resultat = nombre1 / nombre2
    resultat = round(resultat, arrondi)

# Enfin, on affiche le résultat final
print(f"Résultat : {resultat}")
