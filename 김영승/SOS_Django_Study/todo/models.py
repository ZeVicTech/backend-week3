from django.db import models


# Create your models here.
class ToDo(models.Model):
    """Model definition for ToDo"""
    title = models.CharField(max_length=100)
    description = models.TextField()
    is_starred = models.BooleanField()
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
