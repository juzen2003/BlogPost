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
