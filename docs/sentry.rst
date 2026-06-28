Sentry et logs
==============

Variables d'environnement supportées :

* ``SENTRY_DSN``
* ``SENTRY_TRACES_SAMPLE_RATE``
* ``SENTRY_ENVIRONMENT``
* ``LOG_LEVEL``

Lorsque ``SENTRY_DSN`` est configuré, l'application initialise Sentry au démarrage.
Les logs applicatifs passent par la configuration ``LOGGING`` dans les settings.

Validation rapide
-----------------

Provoquer une erreur applicative (ou une URL invalide) et verifier sa remontee dans Sentry.
