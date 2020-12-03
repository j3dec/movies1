import sqlite3

"""Pour exécuter ce script, il faut avoir la base de donnée(remplie au préalable) et ce fichier dans un même dossier
ouvrir un terminal, se placer dans sur le dossier et taper la commande > python splitData.py"""

db = sqlite3.connect("Floupics.db")
cur = db.cursor()

# SPLIT DES TITRES ET ANNEES
cur.execute('select title from movies')
listTitle = []
listYear = []
for row in cur:
    a_split = row[0].split("(")
    title = (a_split[0:-1])
    year = (a_split[-1]).replace(")", "")
    listTitle.append(title)
    listYear.append(year)
"""
SPLIT DES GENRES
On crée deux listes, contenant les id (listId) et les genres (listGenre)
"""
cur.execute('select movieId from movies')
listId = [i[0] for i in cur]

cur.execute('select genres from movies')
listGenres = []
for row in cur:
    a_split = row[0].split("|")
    listGenres.append(a_split)

""" 
A partir des deux listes on crée un dictionnaire contenant le movieId en clé et les genres en valeurs
Exemple pour Toy Story: {1: ['Adventure', 'Animation', 'Children', 'Comedy', 'Fantasy']}
"""
dictTitle = dict(zip(listId, listTitle))
dictYear = dict(zip(listId, listYear))
dictGenre = dict(zip(listId, listGenres))


# Afficher le titre, année et genres d'un film en fonction de l'idMovie
movieInput = int(input("Entrer l'id du film: "))

try:
    print(f'{dictTitle.get(movieInput)} est sorti en {dictYear[movieInput]}')
    print(f'Il es classé en tant que : {dictGenre[movieInput]}')
except NameError:
    print("L'id n'est pas correct")
