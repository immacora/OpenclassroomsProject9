# OpenclassroomsProject9
Développez une application Web MVP en utilisant Django

Application web MVP conforme aux directives PEP 8, développée pour une exécution locale à l'aide du framework Django selon un cahier des charges, des wireframes et une structure de base de données définis.
L'application LITReview permet à ses utilisateurs authentifiés de consulter les critiques de livres ou d’articles rédigés par les utilisateurs qu'ils suivent, d'en publier, ou d'en solliciter via la création de ticket.

![LITReview](https://user-images.githubusercontent.com/76613773/228791438-6f013a2f-8970-4510-b9ea-e2fe91983d4f.jpg)

## Prérequis :
  - python 3.11.2
  - pip
  - django-4.1.7

## Installation (Windows 11)

  - Dans le répertoire souhaité, clonez le projet : git clone https://github.com/immacora/OpenclassroomsProject9.git
  - Dirigez-vous dans le répertoire créé : cd OpenclassroomsProject9
  - Créez l’environnement virtuel du projet : py -m venv env
  - Activez l’environnement virtuel : env\Scripts\activate
  - Dirigez-vous dans le répertoire LITReview : cd LITReview
  - Installez les modules requis : pip install -r requirements.txt

## Contenu

  - Le répertoire documentation contenant le cahier des charges, les wireframes, et la structure de base de données à respecter
  - Le répertoire flake-report contenant le fichier HTML généré par flake8
  - Le répertoire LITReview contenant l'application
  - Le fichier de configuration .flake8
  - Le fichier README.md
  - Le fichier requirements

## Utilisation
### Remarques générales

L'application LITReview contient :
  - 2 sous applications :
    - users : gestion des utilisateurs : authentification et abonnement des utilisateurs à d'autres comptes utilisateurs
    - reviews : demandes et rédaction de critiques de livres ou d'articles
  - Le fichier db.sqlite3
  - Le fichier manage.py permettant d'exécuter l'application

Pour générer rapport flake8 (vérification de la conformité PEP8), saisir : flake8 --format=html --htmldir=flake-report

### Lancement du serveur Django
    - Dirigez-vous dans le répertoire de l'application : cd LITReview
    - Lancez le serveur : py manage.py runserver
    - Faites un CTRL clic sur l'adresse HTTP ou saisissez l'adresse dans votre navigateur pour ouvrir la page d'accès au site (page de connexion)

### Connexion
    Remarque : Ces comptes, créés à visée de test, utilisent des mots de passe identiques.

    1- Administrateur :
        Identifiant et Mot de passe : 
            - Nom d'utilisateur: administrateur
            - Mot de passe: 123456789!

    2- Utilisateur :
        Identifiant et Mot de passe : 
            - Noms d’utilisateurs: utilisateur1, utilisateur2, utilisateur3, utilisateur4
            - Mot de passe (identiques): 123456789!

### Manuel
    1. Création de comptes :

        1.1 : Via l'interface d'administration :
            - Se connecter avec les identifiants de l'administrateur existant (ci-dessus)
            - Se rendre sur l'interface d'administration via le menu de navigation
            - Cliquer sur le bouton + Ajouter de l'onglet Utilisateurs
                * Compte administrateur : 
                    - Saisir le nom d'utilisateur et le mot de passe souhaités
                    - Enregistrer et continuer les modifications
                    - Cocher la case "Statut équipe" de l'onglet permission
                    - Ajouter le groupe administrateurs puis enregistrer
                * Compte utilisateur : 
                    - Saisir le nom d'utilisateur et le mot de passe souhaités puis enregistrer

        1.2 : Via l'interface utilisateurs :
            - Cliquer sur le bouton s'inscrire de la page d'accueil de l'application
            - Saisir le nom d'utilisateur et le mot de passe puis cliquer sur le bouton s'inscrire

    2. Interface utilisateurs :

        2.1 : Authentification (page d'accès à l'application)
            - Créer son compte
            - Se connecter

        2.2 Page d'accueil
            - Menu :
                * Onglet Flux
                * Onglet Posts
                * Onglet Abonnements
                * Bouton "Se déconnecter"
            - Bouton "Demander une critique":
                Créer un ticket pour demander une critique sur un livre ou un article
            - Bouton "Créer une critique"
                Créer un ticket de demande de critique et la critique correspondante
            - Affichage du flux personnalisé de l'utilisateur connecté :
                * Consulter la liste de ses dernières publications (tickets et critiques, réponses comprises) ainsi que celles des utilisateurs qu'il suit
                * Créer une critique en réponse à un ticket qui n'a pas encore reçu de réponse via le bouton du ticket "Créer une critique"

        2.3 : Page de Posts
            - Consulter ses critiques et tickets (affichage séparé)
            - Modifier ses critiques/ tickets
            - Supprimer ses critiques/ tickets

        2.4 : Page Abonnements :
            - S'abonner à un utilisateur : Saisir un nom d'utilisateur dans la zone de texte et cliquer sur "Envoyer"
            - Se désabonner d'un utilisateur : Dans la liste "Abonnements", cliquer sur le bouton "Désabonner" correspondant à l'utilisateur
            - Consulter ses abonnés affichés dans la liste "Abonnés"
