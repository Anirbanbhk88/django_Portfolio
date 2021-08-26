from django.db import models

# Create your models here.
'''
--------------
Model
--------------
'''

'''
Class: Category
specifies the category of the blogs
'''
class Category(models.Model):
    name = models.CharField(max_length=20)

'''
Class: Post
specifies the class for posts
'''
class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('Category', related_name='posts')

'''
Class: Comment
specifies the class for Comment
'''
class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)