FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ARG DJANGO_DEBUG=True
ARG DJANGO_ALLOWED_HOSTS=127.0.0.1,localhost
ARG DJANGO_SECRET_KEY=

# Demo-only fallback admin account for environments without shell access.
ENV DJANGO_SUPERUSER_USERNAME=admin
ENV DJANGO_SUPERUSER_EMAIL=admin@lettings.com
ENV DJANGO_SUPERUSER_PASSWORD=admin123

RUN DEBUG=${DJANGO_DEBUG} ALLOWED_HOSTS=${DJANGO_ALLOWED_HOSTS} SECRET_KEY=${DJANGO_SECRET_KEY} python manage.py collectstatic --noinput

EXPOSE 8000

# Lance les migrations, crée un superuser de démo si absent, puis démarre le serveur.
CMD python manage.py migrate --noinput && (python manage.py createsuperuser --noinput || true) && gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:8000
