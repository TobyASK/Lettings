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

# Lance les migrations, force les credentials admin de démo, puis démarre le serveur.
CMD ["sh", "-c", "python manage.py migrate --noinput && python manage.py shell -c \"from django.contrib.auth import get_user_model; U=get_user_model(); u,_=U.objects.get_or_create(username='admin', defaults={'email':'admin@lettings.com'}); u.email='admin@lettings.com'; u.is_staff=True; u.is_superuser=True; u.is_active=True; u.set_password('admin123'); u.save()\" && gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:8000"]
