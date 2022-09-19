from tokenize import Name
from django.db import models


class Products(models.Model):
    Name = models.CharField(max_length=255)
    Title = models.CharField(max_length=255)
    Price = models.FloatField()
    Img = models.CharField(max_length=255)
