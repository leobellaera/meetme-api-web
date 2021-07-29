# meetme-api-web

## Run locally

`gunicorn --bind 0.0.0.0:3001 "app:create_app()"`

## DB Local (SQLite)

Para correr las migraciones ejecutar:

- `python manage.py db migrate -m 'comment'>`
- `python manage.py db upgrade`

Para ver las tablas creadas en SQLite:

- `sqlite3`
- `.open meet_me.db`
- `select * from user`

## DB Produccion 

- `python manage.py db upgrade` (previamente habiendo pusheado el archivo con las migraciones a master)
