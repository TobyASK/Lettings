Architecture modulaire
======================

Le projet est découpé en trois applications Django :

* ``oc_lettings_site`` : application cœur (page d'accueil, configuration globale).
* ``lettings`` : gestion des locations et adresses.
* ``profiles`` : gestion des profils utilisateur.

Les modèles ont été déplacés de façon compatible avec les données existantes.
Les tables SQL historiques sont conservées via ``db_table``.

API des modules
---------------

.. automodule:: oc_lettings_site.views
   :members:

.. automodule:: lettings.views
   :members:

.. automodule:: profiles.views
   :members:
