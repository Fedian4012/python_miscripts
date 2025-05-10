from echecs.echiquier import Echiquier


class Piece:
    """Classe de base pour les pièces d'échecs"""
    def __init__(self, couleur):
        if couleur not in ("blanc", "noir"):
            raise ValueError(f"Couleur invalide : {couleur}. Utilisez 'blanc' ou 'noir'.")
        self.couleur = couleur
        self.symbole = "Pièce"

    def __str__(self):
        return self.symbole

    def mouvements_valides(self, position, echiquier):
        """Méthode à redéfinir pour chaque pièce"""
        raise NotImplementedError("Cette pièce n’a pas encore de logique de déplacement.")

class Pion(Piece):
    """Classe pour le pion"""
    def __init__(self, couleur):
        super().__init__(couleur)
        self.symbole = "♙" if self.couleur == "blanc" else "♟"

    def mouvements_valides(self, position, echiquier):
        """
        Retourne une liste des positions jouables à partir de la position actuelle.

        position : tuple (y, x) de la position actuelle du pion
        echiquier : objet Echiquier (utilisé pour consulter les cases autour)
        """
        y, x = position
        coups = []

        direction = -1 if self.couleur == "blanc" else 1  # blanc monte, noir descend

        # 1 case en avant
        if 0 <= y + direction < 8 and echiquier.grille[y + direction][x] == ".":
            coups.append((y + direction, x))

            # 2 cases en avant si en position initiale
            ligne_depart = 6 if self.couleur == "blanc" else 1
            if y == ligne_depart and echiquier.grille[y + 2 * direction][x] == ".":
                coups.append((y + 2 * direction, x))

        # Captures diagonales
        for dx in [-1, 1]:
            nx = x + dx
            ny = y + direction
            if 0 <= nx < 8 and 0 <= ny < 8:
                case = echiquier.grille[ny][nx]
                if case != "." and isinstance(case, Piece):
                    # Vérification que la case contient une pièce de l'adversaire
                    if (self.couleur == "blanc" and case.couleur == "noir") or \
                       (self.couleur == "noir" and case.couleur == "blanc"):
                        coups.append((ny, nx))

        return coups

class Tour(Piece):
    def __init__(self, couleur):
        super().__init__(couleur)
        self.symbole = "♖" if self.couleur == "blanc" else "♜"

    def mouvements_valides(self, position, echiquier):
        pass