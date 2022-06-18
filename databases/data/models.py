import email
from django.db import models
from django.forms import CharField, EmailField


# Create your models here.
class Na(models.Model):

    name = models.CharField(max_length=20)
    email =models.EmailField(max_length=50)
    age = models.IntegerField(max_length=5)
def __str__(self):
    return self.name()
