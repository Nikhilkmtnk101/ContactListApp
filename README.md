# Contact List App

This is the Django Rest Framework Project which will provide various endpoints for easy management of Contacts of Person.

## Local Apps

* authentication
* contacts

### DB Models

Default Django User Model is used for Users and Contact model is defined in contacts/models.py file.

### URLS

URLs corresponding to each app can be found in app_name/views.py

### Views

Views corresponding to each app can be found in app_name/views.py

### Documentation

On home page a Documentation of Apis are created using Swagger UI. It will be easy to understand about each each api.

### How to setup local project
Run these commands in your command line

* python manage.py makemigrations
* python manage.py migrate
* python manage.py runserver