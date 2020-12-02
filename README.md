Prestation suite à la validation du projet technique :

Cher Monsieur Chevalier, 


L'équipe TEAM C a le plaisir de vous délivrer les éléments dont nous avons convenu ensemble à la validation du projet technique et nous vous remercions de votre confiance.

Pour rappel, vous nous avez consulté, dans un premier temps, pour nous faire part de votre projet de création d'un service de VOD et donc, de vous aider à identifier au travers d'une étude concurrentielle sur quel modèle de contenu vous pourriez vous démarquer ou attirer rapidement des clients.

Afin d'étudier au mieux votre demande, vous nous avez fournis 4 fichiers CSV ainsi qu'un fichier README détaillant l'origine de ces données.

Il en ressortait les éléments suivants :

Cet ensemble de données (Dataset) reprend la notation et l'ajout de tags (texte libre) à une liste de films issu du site MovieLens (http://movielens.org) sur la période du 29/03/1996 au 24/09/2018 par 610 utilisateurs sur 9742 films.

Les données (extraites le 26/09/2018) sont réparties dans 4 fichiers au format CSV :

    - movies.csv : composé de 3 champs (movieId, title, genres);
    - links.csv : composé de 3 champs (movieId, imdbId, tmdbId);
    - tags.csv : composé de 4 champs (userId, movieId, tag, timestamp)
    - ratings.csv : composé de 4 champs (userId, movieId, rating, timestamp);
    
Pour exploiter ce dataset, la meilleure option est d'importer ces 4 fichiers dans une Base de Données de type relationnelle que nous allons nommer Floupics.db.

Voici le plan que nous avons établi pour cette réalisation :

L'ensemble des détails technique pour reproduire en autonomie les opérations sont accessibles dans le fichier BDD_Floupics.ipynb.

Nous vous recommandons d'ouvrir ce fichier sous Jupyterlab, mais vous pouvez également l'ouvrir sous un Editeur de texte tel que Visual Studio Code.

    1) La création d'un dépôt Github movies1 pour retrouver notre étude.
    
    2) Le dépôt est organisé de cette façon : "à finir dès que l'on sera d'accord sur les dossiers, etc...arborescence"
    
    3) la création d'un fichier BDD_Floupics.ipynb qui hébergera le code python nécessaire à :
    
        a) La création d'une base de données sur la base des données fournies uniquement.
    
        b) l'intégration toujours via python des données fournies et la vérification de cette opération
    
        c) Une analyse un peu plus poussée (sous SQlite et DB Browser) des données de la base ainsi crée :
        
            Q1) Rating moyen par film : à l'aide de cette requête nous sommes capable de classer les films qui ont obtenu les meilleurs notes moyennes.
            
            Q2) Nombre de rating par film : réponse apportée avec la requête précédente, cela complète l'analyse car tous les films listés dans le fichier movies.csv n'ont pas reçu de vote.
            
            Q3) Quels films n’ont reçus aucun vote : nous avons donc voulu connaître le % de films qui ne sont pas pris en compte : résultat seuls 18 films sur 9742 n'ont pas reçu de vote.
        
        d) Nous avons listé ses contraintes, limitations, manquements
        
    4) Vous retrouverez ci-dessous une rapide synthèse finale suggérant des éventuels points à étudier et/ou considérer pour enrichir la base de données crée.

#Synthèse :

