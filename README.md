# Work at Olist

This project was created using the Olist backend challenge. Whis is an API to manipulate authors and books data. Python, django and django rest framework was the technologies used in this project.

You can see the API Documentation at ---

## Instaltion and tests instructions

To run this project it is necessary python >= 3.8.


#### Clone this repository: 

```sh
git clone git@github.com:daviromao/work-at-olist.git
cd work-at-olist
```


#### Create the environment:
```sh
python3 -m venv env
```


#### Activate the envirnoment:

on Windows:
```sh
.\env\Scripts\activate               
```

on Ubuntu:
```sh
source env/bin/activate
```


#### Install the reqeuirements:

```
pip install requirements.txt
```


#### Run migrations:

```
python manage.py makemigrations
python manage.py migrate
```


#### Run command to import authors from a csv file:

```
python manage.py import_authors file_path
```
*use --hide to hide the output*


#### Run project:
```sh
python manage.py runserver
```


#### Acces the local API at http://localhost:8000/


#### Run tests:
```sh
python manage.py test
```

