from django.db import models

# Create your models here.

class Tweets(models.Model):
    content = models.TextField(max_length= 250, null = True, blank = True)
    image = models.FileField(upload_to= 'templates/', blank= True, null = True)

    def __str__(self):
        return self.id
