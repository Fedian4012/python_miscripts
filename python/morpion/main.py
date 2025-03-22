import os
import re

CELL_REGEX = r"^[ABC][123]$"

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def print_grid(grid):
    clear_screen()
    print("   A   B   C")
    print("  -------------")
    for i in range(1, 4):
        print(f"{i} | {grid[f'A{i}']} | {grid[f'B{i}']} | {grid[f'C{i}']} |")
        print("  -------------")

def verify_cell(cell):
    return re.match(r"^[ABC][123]$", cell) is not None 

grid = {
    "A1": " ",
    "A2": " ",
    "A3": " ",
    "B1": " ",
    "B2": " ",
    "B3": " ",
    "C1": " ",
    "C2": " ",
    "C3": " "
}

print_grid(grid)
player = "X"

while True:
    written_case = input("Dans quelle case voulez-vous jouer ? ")

    # Vérification de la validité de la case
    if not verify_cell(written_case):  
        print("Erreur : nom de case invalide.")
        continue  # Redemander une entrée

    # Vérification si la case est déjà occupée
    if grid[written_case] in ["X", "O"]:  
        print("Erreur : case déjà occupée.")
        continue  # Redemander une entrée

    # Placer le symbole du joueur
    grid[written_case] = player  

    # Afficher la grille mise à jour
    print_grid(grid)  

    # Changer de joueur
    player = "O" if player == "X" else "X"  
