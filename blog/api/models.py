from django.db import models

# Create your models here.

class StudentModels(models.Model):
    name = models.CharField(max_length=200)
    group = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    address = models.TextField()
    def __str__(self):
        return self.name