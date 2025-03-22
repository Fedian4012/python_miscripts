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
    written_case = input("Dans quelle case voulez-vous jouer ?")
    if verify_cell(written_case) == False:
        print("Erreur : nom de case invalide.")
    if grid["case"] == "X" or grid["case"] == "O":
        print("Erreur : case déjà occupée.")
    else:
        grid["case"] = "X" if player == "X" else grid["case"] = "O"
    player = "O" if player == "X" else "X" # changement de joueur
    print_grid(grid)