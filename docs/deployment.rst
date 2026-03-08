Déploiement Docker
==================

Build local
-----------

.. code-block:: bash

   docker build -t <dockerhub_user>/oc-lettings:latest .

Run local
---------

.. code-block:: bash

   docker run --rm -p 8000:8000 --env-file .env <dockerhub_user>/oc-lettings:latest

Push Docker Hub
---------------

.. code-block:: bash

   docker login
   docker push <dockerhub_user>/oc-lettings:latest

Extraction de l'image depuis Docker Hub
---------------------------------------

.. code-block:: bash

   docker pull <dockerhub_user>/oc-lettings:latest

Déploiement Render (recommandé)
-------------------------------

Le blueprint ``render.yaml`` est inclus pour un déploiement répétable.
Le déploiement automatique peut être déclenché par hook via la CI.
