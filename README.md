Monsieur Chevalier, 


L'équipe TEAM C a le plaisir de vous délivrer les éléments dont nous avons convenu ensemble à la validation du projet technique et nous vous remercions de votre confiance.

**Pour rappel**, vous nous avez consulté, dans un premier temps, pour nous faire part de votre projet de création d'un service de VOD et donc, de vous aider à identifier au travers d'une étude concurrentielle sur quel modèle de contenu vous pourriez vous démarquer ou attirer rapidement des clients.

Afin d'étudier au mieux votre demande, vous nous avez fournis 4 fichiers CSV ainsi qu'un fichier README.txt détaillant l'origine de ces données.

Il en ressortait les éléments suivants :

Cet ensemble de données (Dataset) reprend la notation et l'ajout de tags (texte libre) à une liste de films issu du site MovieLens (http://movielens.org) sur la période du 29/03/1996 au 24/09/2018 par 610 utilisateurs sur 9742 films.

Les données (extraites le 26/09/2018) sont réparties dans 4 fichiers au format CSV :

    - movies.csv : composé de 3 champs (movieId, title, genres);
    - links.csv : composé de 3 champs (movieId, imdbId, tmdbId);
    - tags.csv : composé de 4 champs (userId, movieId, tag, timestamp)
    - ratings.csv : composé de 4 champs (userId, movieId, rating, timestamp);
    
Pour exploiter ce dataset, la meilleure option est d'importer ces 4 fichiers dans une Base de Données de type relationnelle que nous allons nommer Floupics.db.

Voici **le plan** que nous avons établi pour cette réalisation :

L'ensemble des détails technique pour reproduire en autonomie les opérations sont accessibles dans le fichier paramsBDD.ipynb.

Nous vous recommandons d'ouvrir ce fichier sous Jupyterlab, mais vous pouvez également l'ouvrir sous un Editeur de texte tel que Visual Studio Code.

    1) La création d'un dépôt Github movies1 pour retrouver notre étude.
    
    2) Le dépôt est organisé de cette façon :
    
    3) la création de trois fichiers 
         a) "paramsBDD.ipynb":
           - La création d'une base de données sur la base des données fournies uniquement.
           - L'intégration toujours via python des données fournies et la vérification de cette opération
     
         b) "requetesBDD.ipynb" :
           - Une analyse un peu plus poussée (sous SQlite et DB Browser) des données de la base ainsi crée :
       
         c) "synthese.ipynb" :
           - Synthèse finale suggérant des éventuels points à étudier et/ou considérer pour enrichir la base de données crée.
           - Nous avons listé ses contraintes, limitations, manquements
