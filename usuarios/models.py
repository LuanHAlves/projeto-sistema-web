from django.db import models
from django.contrib.auth.models import User

class User(models.Model):
   username = models.CharField(max_length = 40)
   first_name = models.CharField(max_length = 40)
   last_name= models.CharField(max_length = 40)
   email = models.CharField(max_length = 100)
   password = models.CharField(max_length = 10)

   def __str__(self):
      return self.username


