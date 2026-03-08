# Livrables du projet OC Lettings (P13)

## Statut global

- ✅ Refonte architecture modulaire terminée.
- ✅ Réduction de dette technique terminée.
- ✅ Intégration Sentry + logs terminée.
- ✅ Pipeline CI/CD + Docker mis en place.
- ✅ Documentation Sphinx + Read the Docs mise en place.
- ✅ Validation locale lint/tests/couverture effectuée.

---

## 1) Architecture modulaire Django

### Objectif atteint

- Découpage de l’application en 3 apps :
  - `oc_lettings_site` (cœur projet)
  - `lettings` (locations)
  - `profiles` (profils)

### Réalisations

- Création des apps `lettings` et `profiles` avec fichiers dédiés :
  - `apps.py`, `models.py`, `views.py`, `urls.py`, `admin.py`, `tests.py`, `migrations/`.
- Déplacement de la logique depuis le module central vers les apps dédiées.
- Mise à jour du routage racine pour inclure les routes des apps.
- Conservation de la compatibilité base existante via `db_table`.

### Migrations (sans SQL brut)

- Ajout de migrations d’état avec `SeparateDatabaseAndState` :
  - `lettings/migrations/0001_initial.py`
  - `profiles/migrations/0001_initial.py`
- Respect de la contrainte : **pas de `RunSQL()`**.

---

## 2) Réduction de la dette technique

### Lint / qualité

- Configuration pytest et couverture dans `setup.cfg`.
- Ajout de `.coveragerc` pour exclure tests/migrations/manage.py du calcul.
- Correction des longueurs de lignes et style pour passer flake8.

### Docstrings

- Ajout de docstrings module/classe/fonction sur les nouveaux modules et les modules modifiés.

### Admin Django

- Séparation de l’admin par app (`lettings/admin.py`, `profiles/admin.py`).
- Pluralisation correcte via `Meta.verbose_name_plural`.

### Pages d’erreur

- Ajout des pages personnalisées :
  - `templates/404.html`
  - `templates/500.html`
- Handlers configurés dans `oc_lettings_site/urls.py`.

### Tests

- Remplacement du test dummy par des tests utiles.
- Regroupement des tests par app :
  - `oc_lettings_site/tests.py`
  - `lettings/tests.py`
  - `profiles/tests.py`

### Résultats mesurés

- `flake8` : ✅ sans erreur
- `pytest` : ✅ 9 tests passés
- Couverture : ✅ **89.80%** (seuil demandé > 80%)

---

## 3) Sentry + logging

### Intégration

- Ajout dépendance `sentry-sdk`.
- Initialisation conditionnelle Sentry dans `oc_lettings_site/settings.py` si `SENTRY_DSN` est défini.
- Variables d’environnement supportées :
  - `SENTRY_DSN`
  - `SENTRY_TRACES_SAMPLE_RATE`
  - `SENTRY_ENVIRONMENT`
  - `LOG_LEVEL`

### Logging

- Configuration Django `LOGGING` ajoutée avec handler console et loggers applicatifs.

### Validation erreur

- Ajout route de test Sentry : `/sentry-debug/`.

---

## 4) CI/CD + Docker + déploiement

### CI/CD (GitHub Actions)

- Création du workflow : `.github/workflows/ci.yml`.
- Étapes automatisées :
  - Installation dépendances
  - Lint (`flake8`)
  - Tests + couverture (`pytest`)
  - Build image Docker
  - Push Docker Hub (optionnel, si secrets présents)
  - Trigger deploy Render (optionnel, si secret présent)

### Secrets attendus (GitHub)

- `DOCKERHUB_USERNAME`
- `DOCKERHUB_TOKEN`
- `RENDER_DEPLOY_HOOK_URL`

### Docker

- Ajout :
  - `Dockerfile`
  - `docker-compose.yml`
  - `.dockerignore`
- Config de production Django améliorée pour staticfiles/WhiteNoise.

### Déploiement

- Ajout blueprint Render : `render.yaml`.
- `autoDeploy: false` conforme au point de vigilance demandé.

### Limite constatée localement

- Docker daemon non démarré au moment du test (CLI installée mais moteur indisponible), donc build/pull réels non exécutés sur cette session.

---

## 5) Documentation technique (Sphinx + RTD)

### Fichiers ajoutés

- `.readthedocs.yaml`
- `docs/conf.py`
- `docs/index.rst`
- `docs/modules.rst`
- `docs/deployment.rst`
- `docs/cicd.rst`
- `docs/sentry.rst`
- `docs/_static/`

### Validation

- Génération locale HTML effectuée avec succès : `docs/_build/html`.

---

## 6) Exigence de démonstration (modif home)

### Réalisé

- Titre homepage modifié dans `templates/index.html` :
  - `Holiday Homes` → `OC Lettings Home`
- Titre principal mis à jour :
  - `Welcome to Holiday Homes` → `Welcome to OC Lettings`

---

## 7) Mise à jour documentation projet

- Réécriture complète de `README.md` avec :
  - setup local
  - tests/lint/couverture
  - Sentry
  - Docker
  - CI/CD
  - déploiement Render
  - procédure de démonstration finale

---

## 8) Fichiers clés modifiés/ajoutés (résumé)

- `README.md`
- `requirements.txt`
- `setup.cfg`
- `.coveragerc`
- `.env.example`
- `.dockerignore`
- `Dockerfile`
- `docker-compose.yml`
- `.github/workflows/ci.yml`
- `render.yaml`
- `.readthedocs.yaml`
- `oc_lettings_site/settings.py`
- `oc_lettings_site/urls.py`
- `oc_lettings_site/views.py`
- `oc_lettings_site/tests.py`
- `templates/404.html`
- `templates/500.html`
- `templates/index.html`
- `lettings/*`
- `profiles/*`
- `docs/*`

---

## 9) Ce qu’il reste à faire côté compte utilisateur (hors code)

- Renseigner les secrets GitHub (Docker Hub + Render).
- Démarrer Docker Desktop (daemon) localement.
- Pousser l’image sur Docker Hub avec tes credentials.
- Déployer sur Render (ou autre hébergeur) avec variables de prod.
- Configurer le projet Read the Docs pointant sur ce repo.
