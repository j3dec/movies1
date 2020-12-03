import sqlite3

db = sqlite3.connect("Floupics.db")
cur = db.cursor()

# SPLIT DES TITRES ET ANNEES
cur.execute('select title from movies')
for row in cur:
    a_split = row[0].split("(")
    title = (a_split[0:-1])
    year = (a_split[-1]).replace(")", "")

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
res = dict(zip(listId, listGenres))
print(res)
