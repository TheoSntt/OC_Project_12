
# EPICEVENTS ORM


## Présentation du projet

Le projet ORM EpicEvents est un des derniers projets réalisés dans le cadre de ma formation OpenClassrooms.  
Le but de ce projet était, après 2 projets dédiés à Django, de nous faire réaliser un backend complet d'application sans l'utiliser. Ainsi, j'ai dû développer par moi-même de nombreuses fonctionnalités qui sont gérées de manières très automatiques par Django comme la gestion des tokens JWT, la gestion des champs de mot de passe (hashing, salting), les permissions, etc.  
Cette expérience a été très intéressante pour approfondir ma compréhension de ces mécanismes. Les bonnes pratiques apprises précédemment, comme l'utilisation d'un linter, et la mise en place d'une bonne couverture de tests ont été mises en application dans le cadre de ce projet.  
En termes de technologies, ce projet m'a aussi beaucoup apporté : Il m'a permis d'utiliser pour la première fois MySQL (j'étais plus familier avec SQLite et PostGres), ainsi que SQLAlchemy. C'est également sur ce projet que j'ai configuré l'outil de suivi des erreurs Sentry.  
Ce projet était aussi très intéressant en termes d'architecture et de Design Patterns. Sans l'architecture prédéfinie de Django, j'ai dû trouver des solutions pour rendre l'architecture la plus claire et la plus modulaire possible. J'en ai profité pour mettre en application pour la première fois les Design Patterns DAO et Repository.  

## Mise en place et exécution en local de l'application.

### Configuration de base (environnement virtuel et dépendances)

1. Téléchargez le projet depuis Github. Soit directement (format zip), soit en clonant le projet en utilisant la commande suivante dans Git Bash :  
```
git clone https://github.com/TheoSntt/epicevents-orm 
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
4. La configuration de base (configuration normale d'un projet python) est terminée.  

### Configuration avancée

Ce projet était le premier de ma formation OpenClassrooms pour lequel il était demandé de prêter une attention particulière à des notions de sécurité, notamment dans la manière de gérer les informations confidentielles (clés de sécurité) sur le répo distant. De ce fait, les différents identifiants, mots de passe, clés de sécurité, et autres bases de données ne sont pas présents dans le répo.  
La confifuration nécessaire pour exécuter l'application en local est donc importante. Mais pas impossible. La preuve, étape par étape :  

1. Créer une base de données à l'aide de MySQL nommée epicevents. Si vous gardez la configuration par défaut de MySQL, elle devrait être accessible sur l'hôte
```
localhost
```
et le port
```
3306
```
Si l'un de ces éléments est différent dans votre configuration locale, il faudra répercuter ces changements dans le fichier config.ini qui indique le nom, hôte et port de la base de données.  
Si vous utilisez un autre système de gestion de base de données que MySQL, il faudra effectuer les changements nécessaires dans le fichier database/db_session.py qui définit l'objet session de l'ORM SQLAlchemy.  

2. Il faut maintenant renseigner l'identifiant et le mot de passe d'un utilisateur MySQL ayant les droits sur le BDD nouvellement créée (soit votre utilisateur root, soit un utilisateur créé pour cet effet) au sein de variables d'environnement.
La procédure à suivre dépend selon votre OS. Les variables d'environnement doivent se nommer
```
MYSQL_PROJECT_USERNAME
```
et
```
MYSQL_PROJECT_PW
```
Si vous utilisez d'autres noms, il faudra répercuter ce changement dans le fichier database/db_session.py  

3. Vous pouvez maintenant exécuter le script permettant la création des tables et des données de tests. Pour créer uniquement les tables, lancer la commande
```
python data_setup.py --add_demo_data=False
```
Pour créer également quelques données de test pour peupler les tables :
```
python data_setup.py
```
4. Il ne reste plus qu'à créer 2 variables d'environnement : la clé secrète JWT et le DSN Sentry. La clé secrète JWT peut être une chaîne de caractère de votre choix, le DSN vous est fourni par Sentry lors de la création d'un nouveau projet sur la plateforme. Les noms de ces variables doivent être :
```
MYSQL_PROJECT_JWT_KEY
```
et
```
SENTRY_DSN
```
Si vous utilisez d'autres noms de variable, il faudra répercuter ces changements dans les fichiers auth/jwt/jwt_handler.py et sentry_manager.py, respectivement.

5. Vous pouvez ensuite vous connecter avec le compte admin par défaut (à supprimer une fois un véritable compte admin créé), en utilant les identifiants suivants :
```
id : admin
pw : admin123
```

5. L'application est prête à être utilisée !
 
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
