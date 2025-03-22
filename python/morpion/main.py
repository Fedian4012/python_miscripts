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