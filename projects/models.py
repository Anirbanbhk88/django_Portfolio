from django.db import models

'''
--------------
Model
--------------
Model class is described here. It creates the Project Model class with the following
Attributes:
    title: title of project
    description: detailed description of project
    technology: tech stack used
    image: the image path for thumbnails of each project
'''
# Create your models here.
class Project(models.Model):
    title= models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.FilePathField(path='/img')
     