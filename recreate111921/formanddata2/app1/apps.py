from django.apps import AppConfig

## commented out this line to be in coordination with settings.py
## this did not solve the problem
class App1Config(AppConfig):
##    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app1'
