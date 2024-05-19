# Django REST API

## Setup

1. Clone the repository.
1. Open a terminal
1. Navigate to the Project root folder
1. Run `docker-compose up --build` to build and start the containers.
1. python manage.py makemigrations app
1. python manage.py migrate app
1. python manage.py createsuperuser
1. python manage.py migrate app



## Import Data

To import data from JSONPlaceholder, run the following command inside the web container:
`docker-compose run web python manage.py import_data`

