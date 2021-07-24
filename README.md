# meetme-api-web

# Ejecución
- chmod +x services/web/entrypoint.sh
- docker-compose build
- docker-compose up
- docker-compose exec web python manage.py seed_db (en otra terminal)

# Acceso a DB
- docker-compose exec db psql --username=meet_me --dbname=meet_me_dev