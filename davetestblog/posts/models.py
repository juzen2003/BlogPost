from django.db import models

# Create your models here.
# model is singular
class Post(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateField()
    # blank=True makes image optional, not required
    image = models.ImageField(upload_to='media/', blank=True)
    body = models.TextField()

    # display title in the admin gui
    def __str__(self):
        return self.title
