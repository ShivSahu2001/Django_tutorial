from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Receipe(models.Model):
    # on_delete= models.CASCADE means If user is deleted then all the corresponding receipe will be deleted of that user

    # on_delete= models.SET_NULL if user is deleted than the user will be set to null and also receipes will be set to null

    # on_delete= models.SET_DEFAULT if user is deleted than we can set default user
    user = models.ForeignKey(User, on_delete= models.SET_NULL, null=True, blank=True)
    receipeName = models.CharField(max_length=100)
    receipeDescription = models.TextField()
    receipeImage = models.ImageField(upload_to="receipe")
    receipeViewCount = models.IntegerField(default=1)