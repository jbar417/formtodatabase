# formtodatabase
a web submission form that writes to the database

Recreating a course project into my own modified project, that still works. 
This writes data from a form to a database. 
To run webpage:
open terminal
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

Then fill out the form with data including the date and time of the submission. 

To access the database, 
Open terminal
python manage.py shell
from app1.models import CommentData
CommentData.objects.all()
##and respectively
CommentData.objects.all()[2].comment

See models.py for field info. 
