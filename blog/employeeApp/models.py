from django.db import models

# Create your models here.

class EmployeeModel(models.Model):
    empName = models.CharField(max_length=200)
    empNo = models.IntegerField()
    designation = models.CharField()

    def __str__(self):
        return self.empName