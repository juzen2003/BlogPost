### Install virtual environment on your mac
* first time install virtual env: pip3 install virtualenv

### Steps to create virtual env
* create a virtual env for the project inside the project folder: virtualenv venv_name
* once virtual env is created, we would like to go into virtual env: source venv_name/bin/activate
* deactivate it: deactivate

### Notes
* each virtual env would start clean so we have to install packages needed for the virtual env
* check packages inside virtual env: pip3 freeze

### Steps to create an app in the project
* python3 manage.py startapp app_name
* views for each app should be in views.py in each app folder
* html files are in templates folder under each app and inside templates folder we would create another folder with the same name as app and put html files in there.
* we have to go to settings.py and add our app in INSTALLED_APPS list, we don't need to add templates here because we use app

### Migration
* in order to add the model we created to database, we need to run migration, quit server before running any migration
* to migrate for pre-installed apps at the very beginning: python3 manage.py migrate
* to make migration file whenever we've changed the model: python3 manage.py makemigrations
* you'll see migration file, and then migrate: python3 manage.py migrate

### Admin interface
* django by default uses SQLite
* quit server & create superuser: python3 manage.py createsuperuser
* and register the model
* login admin interface, it allows us to manage the data of registered model inside database

### QuerySet API
* use QuerySet API to query model entries in database in views.py and passed in those info in dictionary to display in html
* for the lookup parameters passed into QuerySet API (kwargs), we can refer to https://docs.djangoproject.com/en/2.1/ref/models/querysets/#id4 for field lookup

### Regex recap
* ^: begin of string
* $: end of string

### views.py, models.py, urls.py
* urls.py: defined the url path to the corresponding view in views.py
* views.py: defined each view to render to the html file in templates, data (or models) are passed into html using dictionary
* models.py: defined the info (or schema) we would like to migrate to database

### Bootstrap 4
* responsive image refer to: https://getbootstrap.com/docs/4.1/content/images/#responsive-images
* use img-fluid and a outer div with text-center instead of a class with img-responsive center-block

### Disqus
* use disqus to build the comment system, refer to: https://disqus.com/
