from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to= 'images/', default='SOME STRING')


    def __str__(self):
        return self.cover