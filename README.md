## Idea 360

Service for creating and sharing your own ideas between your colleagues and employees


## Docker

For starting project run `docker-compose run --rm --service-ports idea360`


## Migrations

* `FLASK_APP=manage.py flask db migrate`
* `FLASK_APP=manage.py flask db upgrade`
* `FLASK_APP=manage.py flask db downgrade` - rollback

## Tests
* For setting up need to perform `python manage.py createdb test` in order to
populate test database
* `python manage.py test` - runs unittest tests
* `python manage.py test -t tests.*` - run specific test, where `*` - path
