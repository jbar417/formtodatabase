from django.db import models
##started a new project to start with clean database and migrations. 
## it did not fix the bug. 
## the form does not write to the database. 

# Create your models here.
class CommentData(models.Model):
  name = models.CharField(max_length=30)
  email = models.CharField(max_length=50)
  comment = models.TextField()