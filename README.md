# OC Lettings (architecture modulaire)

## Objectif

Application Django découpée en 3 apps :

- `oc_lettings_site` : cœur applicatif (home, config, erreurs) ;
- `lettings` : gestion des locations ;
- `profiles` : gestion des profils.

Le projet inclut :

- refonte modulaire ;
- réduction de dette technique ;
- tests + couverture > 80 % ;
- intégration Sentry + logging ;
- pipeline CI (GitHub Actions) ;
- conteneurisation Docker ;
- documentation Sphinx + Read The Docs.

## Installation locale

### Prérequis

- Python 3.12
- Git
- Docker (optionnel pour run conteneur)

### Démarrage

1. Cloner le repo.
2. Installer les dépendances :

  - `pip install -r requirements.txt`

3. Lancer le serveur :

  - `python manage.py runserver`

4. Ouvrir `http://127.0.0.1:8000`.

### Linting

- `flake8`

### Tests + couverture

- `pytest`

Le seuil de couverture minimal est fixé à 80 % (`setup.cfg`).

## Administration

- URL : `/admin`
- identifiants de démonstration (image Docker) : `admin` / `admin123`

## Variables d'environnement

Copier `.env.example` et adapter les valeurs :

- `DEBUG`
- `SECRET_KEY`
- `ALLOWED_HOSTS`
- `LOG_LEVEL`
- `SENTRY_DSN`
- `SENTRY_TRACES_SAMPLE_RATE`
- `SENTRY_ENVIRONMENT`

En local, le fichier `.env` est chargé automatiquement au démarrage.

Dans GitHub Actions, toutes les variables sont lues depuis les
`Repository variables` (`vars.*`) et `Repository secrets` (`secrets.*`),
sans valeur codée en dur dans le workflow.

## Sentry

L'initialisation est automatique si `SENTRY_DSN` est défini.

Pour tester : provoquer une erreur (URL invalide, exception volontaire) et vérifier la remontée sur le projet Sentry.

Route de test dédiée : `/sentry-debug/`.

## Docker

### Build local

- `docker build -t <dockerhub_user>/oc-lettings:latest .`

### Run local

- `docker run --rm -p 8000:8000 --env-file .env <dockerhub_user>/oc-lettings:latest`

### Push Docker Hub

- `docker login`
- `docker push <dockerhub_user>/oc-lettings:latest`

### Extraire l'image Docker Hub

- `docker pull <dockerhub_user>/oc-lettings:latest`

## CI/CD

Workflow : `.github/workflows/ci.yml`

Déclenchement automatique sur `push` et `pull_request`.

Étapes :

1. Installation dépendances ;
2. `flake8` ;
3. `pytest` + couverture ;
4. build image Docker ;
5. push Docker Hub (si secrets configurés) ;
6. déclenchement Render Deploy Hook (sur `main`).

Secrets GitHub à définir :

- `DJANGO_SECRET_KEY`
- `SENTRY_DSN`
- `DOCKERHUB_TOKEN`
- `RENDER_DEPLOY_HOOK_URL`

Variables GitHub à définir :

- `DOCKERHUB_USERNAME`
- `DJANGO_DEBUG`
- `DJANGO_ALLOWED_HOSTS`
- `DJANGO_LOG_LEVEL`
- `SENTRY_TRACES_SAMPLE_RATE`
- `SENTRY_ENVIRONMENT`

## Déploiement (exemple Render)

1. Créer un service Web Docker.
2. Pointer sur le repository GitHub.
3. Ajouter les variables d'environnement (notamment `SECRET_KEY`, `DEBUG=False`, `ALLOWED_HOSTS`, `SENTRY_DSN`).
4. Déployer et récupérer l'URL publique.

Le fichier `render.yaml` est fourni pour rendre le déploiement répétable.

## Démonstration demandée

1. Modifier le titre de la page home dans `templates/index.html`.
2. Commit / push.
3. Redéployer.
4. Vérifier le nouveau titre sur l'URL publique.
5. Montrer l'extraction Docker Hub :

  - `docker pull <dockerhub_user>/oc-lettings:latest`

## Documentation technique

Sources Sphinx dans `docs/`.

Build local documentation :

- `sphinx-build -b html docs docs/_build/html`

Configuration Read the Docs : `.readthedocs.yaml`.
