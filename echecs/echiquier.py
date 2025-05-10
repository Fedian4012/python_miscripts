from echecs.pieces import *


class Echiquier:
    """La classe pour l'échiquier"""
    def __init__(self):
        """Création de l'objet"""
        self.grille = []

        # Création d'une grille vide
        for _ in range(8):
            ligne = []
            for _ in range(8):
                ligne.append(".")
            self.grille.append(ligne)

        # Placement des pièces
        ligne_pieces = ["T", "C", "F", "D", "R", "F", "C", "T"]
        for colonne in range(8):
            self.grille[0][colonne] = ligne_pieces[colonne].lower()  # noirs
            self.grille[1][colonne] = Pion("noir")  # pions noirs
            self.grille[6][colonne] = Pion("blanc") # pions blancs
            self.grille[7][colonne] = ligne_pieces[colonne]  # blancs

        self.afficher()

    def afficher(self):
        """Affiche la grille proprement"""
        lettres_colonnes = ["a", "b", "c", "d", "e", "f", "g", "h"]

        # En-tête des colonnes
        print("    " + "   ".join(lettres_colonnes))
        print("  +" + "---+" * 8)

        for i in range(8):
            ligne = self.grille[i]
            print(f"{8 - i} | " + " | ".join(str(c) for c in ligne) + " |")
            print("  +" + "---+" * 8)

    def coords_echecs_a_coords_python(self, coords):
        """
        Traduit des coordonnées d'échecs (ex : 'e2') en coordonnées (y, x)
        utilisables directement avec self.grille[y][x]
        """
        colonne = coords[0].lower()
        ligne = coords[1]

        x = "abcdefgh".index(colonne)
        y = 8 - int(ligne)

        return (y, x)

    def coords_python_a_coords_echecs(self, coords_grille):
        """
        Traduit des coordonnées (y, x) de grille en notation échecs (ex : 'e2')
        """
        y, x = coords_grille

        colonne = "abcdefgh"[x]
        ligne = str(8 - y)

        return colonne + ligne

    def deplacer_piece(self, depart, arrivee):
        """Déplace une pièce de la case 'depart' à la case 'arrivee'."""
        y_depart, x_depart = self.coords_echecs_a_coords_python(depart)
        y_arrivee, x_arrivee = self.coords_echecs_a_coords_python(arrivee)

        piece = self.grille[y_depart][x_depart]

        if piece == ".":
            print("Erreur : Aucune pièce à déplacer.")
            return False

        # Vérifier que le mouvement est valide
        if piece.mouvements_valides((y_depart, x_depart), self):
            # Déplacer la pièce
            self.grille[y_arrivee][x_arrivee] = piece
            self.grille[y_depart][x_depart] = "."
            return True
        else:
            print("Mouvement invalide.")
            return False
