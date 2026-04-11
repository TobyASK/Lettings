FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV DEBUG=False
ENV ALLOWED_HOSTS=*

RUN python manage.py collectstatic --noinput

EXPOSE 8000

# Lance les migrations puis démarre le serveur
CMD python manage.py migrate --noinput && gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:8000
