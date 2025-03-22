import os
import re

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

def verify_win(grid):
    for cell1, cell2, cell3 in winning_combinations:
        if grid[cell1] == grid[cell2] == grid[cell3] and grid[cell1] != "":
            return grid[cell1]
        return None

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


print_grid(grid)
player = "X"

while True:
    written_case = input("Dans quelle case voulez-vous jouer ? ")
    if not verify_cell(written_case):  
        print("Erreur : nom de case invalide.")
        continue  # Redemander une entrée

    if grid[written_case] in ["X", "O"]:  
        print("Erreur : case déjà occupée.")
        continue  # Redemander une entrée

    grid[written_case] = player  
    
    
    winner = verify_win(grid)
    if winner is not None:
        print_grid(grid)
        print(f"{winner} a gagné !")
        break
    player = "O" if player == "X" else "X"  