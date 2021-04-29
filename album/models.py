from django.db import models

# Create your models here.
# album model
class Album(models.Model):
    description = models.TextField()
    photo = models.ImageField(upload_to='photo/')
    creation = models.DateTimeField(auto_now=True)
