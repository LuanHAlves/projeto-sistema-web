from django.db import models

class User(models.Model):
   first_name = models.CharField(max_length = 40)
   last_name= models.CharField(max_length = 40)
   email = models.CharField(max_length = 100)
   password = models.CharField(max_length = 10)

   def __str__(self):
      return self.first_name + self.last_name