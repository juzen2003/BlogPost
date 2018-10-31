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
* we have to go to settings.py and add our app in INSTALLED_APPS list
