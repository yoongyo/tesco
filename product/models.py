from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField(blank=True, null=True)
    image = models.ImageField()
