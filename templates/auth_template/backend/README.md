# Authentication Template (Django Backend)

### Instructions for setup
1. Initialise a new python environment
2. Run `pip3 install -r requirements.txt`
3. Rename the root project folder (authtemplate) to your project name
4. Edit the .env file and change the `PROJECT_NAME` environment variable to your project name
5. Edit .gitignore to include the .env file
6. Create a new django project using django-admin startproject
7. Go into the settings.py file of that project, look for the SECRET KEY variable and set it to the `DJANGO_SECRET_KEY` environemnt variable in the .env file.
8. Modify the User models, serializers, views and permission classes as required
