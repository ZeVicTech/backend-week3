from django.db import models


# Create your models here.
class House(models.Model):
    """Model definition for Houses"""
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    description = models.TextField()
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name