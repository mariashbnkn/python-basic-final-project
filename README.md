### ### ###
    Project for creating urban planning regulations, linking to territorial zone and mapping (GIS)
### ### ###

# install GDAL
    sudo apt-get install gdal-bin

# docker build
    docker compose up -d --build

# docker up
    docker compose up -d

# create admin (needs)
    python manage.py createsuperuser

# make migration and migrate
    python manage.py makemigrations --name
    python manage.py migrate

# add data in terzone
    python manage.py loaddata kindterzone-fixture.json
    python manage.py loaddata terzone-fixture.json

# create workspace and add stores in geoserver (password and login in "docker-compose.yaml")
# and publish terzone_terzoneexist
    http://localhost:8080/geoserver/web/

# celery
    python manage.py migrate django_celery_results
    celery -A gis worker -l INFO

# run app 
    python manage.py runserver
