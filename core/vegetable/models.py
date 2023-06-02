from django.db import models

# Create your models here.


class Receipe(models.Model):
    receipeName = models.CharField(max_length=100)
    receipeDescription = models.TextField()
    receipeImage = models.ImageField(upload_to="receipe")