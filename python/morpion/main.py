import os
import re

#----------------
# Fonctions
#----------------
def clear_screen():
    '''Efface l'écran'''
    os.system("cls" if os.name == "nt" else "clear")

def print_grid(grid):
    '''Affiche la grille'''
    print("   A   B   C")
    print("  -------------")
    for i in range(1, 4):
        print(f"{i} | {grid[f'A{i}']} | {grid[f'B{i}']} | {grid[f'C{i}']} |")
        print("  -------------")

def verify_cell(cell) -> bool:
    '''Vérifie qu'on veut bien jouer dans une cellule valide'''
    return re.match(r"^[ABC][123]$", cell) is not None

def verify_win(grid):
    '''Regarde si on a une position gagnante'''
    for cell1, cell2, cell3 in winning_combinations:
        if grid[cell1] == grid[cell2] == grid[cell3] and grid[cell1] in ["X", "O"]:
            return grid[cell1]  # Retourne "X" ou "O" s'il y a un gagnant
    return None  # Si aucune combinaison n'a été trouvée

#----------------
# Code
#----------------

winning_combinations = [
    ("A1", "B1", "C1"),  # Ligne 1
    ("A2", "B2", "C2"),  # Ligne 2
    ("A3", "B3", "C3"),  # Ligne 3
    ("A1", "A2", "A3"),  # Colonne A
    ("B1", "B2", "B3"),  # Colonne B
    ("C1", "C2", "C3"),  # Colonne C
    ("A1", "B2", "C3"),  # Diagonale \
    ("A3", "B2", "C1")   # Diagonale /
]


# Initialisation des scores
score_X = 0
score_O = 0

while True:  
    grid = {cell: " " for cell in ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]}
    player = "X"

    while True:
        clear_screen()
        print_grid(grid)
        written_case = input(f"Joueur {player}, dans quelle case voulez-vous jouer ? ").upper()

        if not verify_cell(written_case):
            print("Erreur : case invalide")
            input("Appuyez sur Entrée pour continuer")
            continue
        if grid[written_case] != " ":
            print("Erreur : case déjà occupée.")
            input("Appuyez sur Entrée pour continuer")
            continue  

        grid[written_case] = player

        winner = verify_win(grid)
        if winner is not None:
            print_grid(grid)
            print(f"{winner} a gagné !")
            
            if winner == "X":
                score_X += 1
            else:
                score_O += 1

            break

        if " " not in grid.values():
            print_grid(grid)
            print("Match nul")
            break 

        player = "O" if player == "X" else "X"  # Changer de joueur

    print(f"\nScore : X = {score_X} | O = {score_O}\n")

    replay = input("Voulez-vous rejouer ? (o/n) ").lower()
    if replay != "o":
        print("Merci d'avoir joué !")
        break