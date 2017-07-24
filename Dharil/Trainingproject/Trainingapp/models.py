
from __future__ import  unicode_literals
from django.db import models

# Create your models here.

class signup(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
