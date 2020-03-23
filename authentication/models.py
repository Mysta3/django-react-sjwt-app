from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

# Customer extends from AbstractUser which gives us access to the standard Django User model attributes and functionalities such as username, password, etc.

#don't need to add the other fields because they already exist in the user model.
class Customer(AbstractUser):
    fav_color = models.CharField(blank=True, max_length=120)