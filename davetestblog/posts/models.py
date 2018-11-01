from django.db import models

# Create your models here.
# model is singular
class Post(models.Model):
    title = models.CharField(max_length=255)
    # if we use DateField here then it would only have date but no time for data input
    pub_date = models.DateTimeField()
    # blank=True makes image optional, not required
    image = models.ImageField(upload_to='media/', blank=True)
    body = models.TextField()

    # display title in the admin gui
    def __str__(self):
        return self.title

    # strftime is a python function to better display time
    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')

    # display only first 100 character in summary, not all posts body
    def summary(self):
        return self.body[:100]
