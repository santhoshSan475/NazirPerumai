from django.db import models

# Create your models here.

class EmployeeDetails(models.Model):
    empNo = models.IntegerField()
    empName = models.CharField(max_length=200)
    phoneNo = models.IntegerField()
    emailAddress = models.CharField(max_length=100)
    salary = models.IntegerField()

    def __str__(self):
        return self.empName

