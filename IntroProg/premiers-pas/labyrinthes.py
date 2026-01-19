from laby.global_fr import Laby


def une_porte(x: int, y: int, largeur=10, hauteur=10) -> Laby:
    carte = "o " * (largeur + 2) + "\n"
    for i in range(hauteur):
        carte += "o "
        for j in range(largeur):
            if j == x and i == hauteur - 1 - y:
                carte += "x "
            elif j == 0 and i == hauteur - 1:
                carte += "→ "
            else:
                carte += ". "
        carte += "o\n"
    carte += "o " * (largeur + 2) + "\n"
    return Laby(carte=carte)

