
# EPICEVENTS ORM


## Avertissements

Ce repo contient l'application ORM d'Epicevents.
Du fait de la structure du projet, exécuter localement le code contenu dans ce repository demanderait beaucoup de configuration.
Ce travail devra néanmoins être fait pour le déploiement de l'application.

## Mise en place et exécution en local de l'application.

1. Téléchargez le projet depuis Github. Soit directement (format zip), soit en clonant le projet en utilisant la commande suivante dans Git Bash :  
```
git clone https://github.com/TheoSntt/OC_Project_12
```
2. Créez un environnement virtuel Python en exécutant la commande suivantes dans le Terminal de votre choix :
```
python -m venv env (env étant le nom de l'environnement, vous pouvez le changer)
```
Puis, toujours dans le terminal, activez votre environnement avec la commande suivante si vous êtes sous Linux :
```
source env/bin/activate
```
Ou bien celle-ci si vous êtes sous Windows
```
env/Scripts/activate.bat
```
3. Dans vorte environnement virtuel, téléchargez les packages Python nécessaires à la bonne exécution de l'application à l'aide de la commande suivante :
```
pip install -r requirements.txt
```
4. La configuration de base est terminée. Les étapes de configuration suivantes sont nécessaires pour le bon fonctionnement de l'application dans un nouvel environnement :

- Changer les informations de connexions à la base de données pour renseigner les nouvelles informations (informations de connexion à la BDD de l'entreprise) dans les fichiers config.ini et database/db_session.py
- Changer les informations de clés secrètes JWT (pour l'instant récupérées depuis une variable d'environnement) pour les remplacer par une manière d'accéder à la nouvelle clé secret dans le fichier auth/jwt/jwt_handler.py
- Changer les informations de connexion à Sentry.io contenues dans le fichier sentry_manager.py pour les remplacer par les informations au compte d'entreprise.
- Lancer le script data_setup à l'aide de la commande suivante :
```
python data_setup.py
```
- Cela créera les tables dans la base de données ainsi que des données de test. Pensez bien à utiliser un utilisateur en Base de données ayant les droits nécessaires. (NB: Il faudra ensuite changer les droits de cet utilisateur -ou changer d'utilisateur dans les informations de connexion- pour appliquer le principe du moindre privilège).
- Vous pouvez ensuite vous connecter avec le compte admin par défaut (à supprimer une fois un véritable compte admin créé), en utilant les identifiants suivants :
```
id : admin
pw : admin123
```

5. L'application est prête à être utilisée. Son fonctionnement correspond aux documents de conception fournis.
 
## Schéma de la base de données

![UML(1)](https://github.com/TheoSntt/OC_Project_12/assets/118457519/33772aad-6c4e-4b31-b4eb-65bc8bdd7050)
 
## BONUS :
Si vous souhaitez tester vous même la conformité à la PEP8, vous pouvez exécuter flake8, à l'aide de la commande suivante :

```		
flake8 --format=html --htmldir=rapport
```
## BONUS 2 :
Si vous souhaitez tester vous même la couverture de test, vous pouvez exécuter pytest-cov, à l'aide de la commande suivante :

```		
pytest --cov=. --cov-report html
```
