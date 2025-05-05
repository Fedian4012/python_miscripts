class Echiquier:
    """La classe pour l'échiquier"""

    def __init__(self):
        """Initialise l'échiquier avec les pièces placées à leur position initiale"""
        self.grille = []

        for _ in range(8):
            ligne = []
            for _ in range(8):
                ligne.append(".")
            self.grille.append(ligne)

        ligne_pieces = ["T", "C", "F", "D", "R", "F", "C", "T"]
        for colonne in range(8):
            self.grille[0][colonne] = ligne_pieces[colonne].lower()
            self.grille[1][colonne] = "p"
            self.grille[6][colonne] = "P"
            self.grille[7][colonne] = ligne_pieces[colonne]

        self.afficher()

    def afficher(self):
        """Affiche l'échiquier de manière lisible avec les coordonnées de colonne (a-h) et de ligne (8-1).

        L'affichage utilise des "barres" pour délimiter les cases, avec les numéros de ligne en ordre décroissant
        (8 en haut, 1 en bas) et les colonnes étiquetées de 'a' à 'h'.
        """
        lettres_colonnes = ["a", "b", "c", "d", "e", "f", "g", "h"]

        # En-tête des colonnes
        print("    " + "   ".join(lettres_colonnes))
        print("  +" + "---+" * 8)

        for i in range(8):
            ligne = self.grille[i]
            print(f"{8 - i} | " + " | ".join(ligne) + " |")
            print("  +" + "---+" * 8)

    def coords_echecs_a_coords_python(self, coords):
        """Convertit une coordonnée d'échecs (ex : 'a1') en indices Python (ex : (0,7)).

        L'argument 'coords' est une chaîne de caractères de la forme 'a1', 'd5', etc.
        Cette fonction retourne un tuple avec l'indice de colonne (0 à 7) et l'indice de ligne (0 à 7).
        """
        colonne = coords[0].lower()
        ligne = coords[1]

        index_colonne = "abcdefgh".index(colonne)
        index_ligne = 8 - int(ligne)

        coords_python = (index_colonne, index_ligne)
        return coords_python

    def coords_python_a_coords_echecs(self, coords_python):
        """Convertit des indices Python (ex : (0,7)) en coordonnées d'échecs (ex : 'a1').

        L'argument 'coords_python' est un tuple (colonne, ligne) avec des indices de 0 à 7.
        Cette fonction retourne une chaîne de caractères représentant la coordonnée d'échecs correspondante.
        """
        index_colonne, index_ligne = coords_python

        # Conversion de l'index de colonne en lettre (de 0 à 7 → 'a' à 'h')
        colonne = "abcdefgh"[index_colonne]

        # Conversion de l'index de ligne en numéro (8 - index_ligne)
        ligne = 8 - index_ligne

        # Retourner la coordonnée échiquier
        coords_echecs = f"{colonne}{ligne}"
        return coords_echecs
