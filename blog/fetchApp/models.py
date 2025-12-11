from django.db import models

# Create your models here.

class EmployeeDetailModel(models.Model):
    empId = models.IntegerField()
    empName = models.CharField(max_length=200)
    phoneNum = models.IntegerField()
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.empName