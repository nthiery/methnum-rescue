import glob
from jupylates.jupylates import Exerciser  # type: ignore

thèmes = {
    'Fonctions': 'fonctions/*.md',
    'Conditions': 'conditions/*.md',
    'Boucles While': 'boucles-while/*.md',
    'Boucles For': 'boucles-for/*.md',
#    'Fonctions partie 2': 'fonctions2/*.md',
    'Listes': 'listes/*.md'
}

entraîneur = Exerciser({thème: glob.glob(thèmes[thème]) for thème in thèmes},
                       lrs_url="../../../.lrs.json",
                       mode="train")

