from django.db import models

# Create your models here.

class Blog(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField(default=0)
    birth = models.DateField()