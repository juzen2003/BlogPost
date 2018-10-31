from django.db import models

# Create your models here.
# model is singular
class Post(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateField()
    image = models.ImageField(upload_to='media/')
    body = models.TextField()
