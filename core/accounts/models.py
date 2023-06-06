from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager
# Create your models here.

class CustomUser(AbstractUser):

    username = models.CharField(max_length=10, unique=True)
    # phoneNumber = 
    userEmail = models.EmailField(unique=True)
    userBio = models.CharField(max_length=50)
    userProfileImage = models.ImageField(upload_to="profile")

    # By this USERNAME_FIELD property --> you can login from Phone Number
    USERNAME_FIELD = 'username'
    # REQUIRED_FIELDS property means all fields are required or not
    REQUIRED_FIELDS = []

