## Idea 360

Service for creating and sharing your own ideas between your colleagues and employees

## Docker

For starting project run `docker-compose run --rm --service-ports idea360`


## Migrations

* `FLASK_APP=manage.py flask db migrate`
* `FLASK_APP=manage.py flask db upgrade`

## Tests

* `python manage.py test` - runs unittest tests
