CI/CD
=====

Le pipeline GitHub Actions réalise :

* lint ``flake8`` ;
* tests ``pytest`` avec couverture >= 80 % ;
* build de l'image Docker ;
* push Docker Hub si les secrets sont définis ;
* déclenchement du déploiement Render sur ``main``.

Le workflow est défini dans ``.github/workflows/ci.yml``.

Secrets GitHub attendus
-----------------------

* ``DOCKERHUB_USERNAME``
* ``DOCKERHUB_TOKEN``
* ``RENDER_DEPLOY_HOOK_URL``
