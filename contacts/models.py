from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Contacts(models.Model):
    owner=models.ForeignKey(to=User,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    country_code=models.CharField(max_length=30)
    phone_number=models.CharField(max_length=50)
    email=models.EmailField(max_length=255)
    contact_picture=models.URLField(null=True)
    is_favourite=models.BooleanField(default=True)

