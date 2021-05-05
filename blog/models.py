from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.TextField()
    sort_desciption = models.TextField()
    desciption = models.TextField()
    photo = models.ImageField(upload_to='photo/')
    creation = models.DateTimeField(auto_now=True)
