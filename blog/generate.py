import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog.settings')
django.setup()

from fetchApp.models import EmployeeDetailModel
from faker import Faker
from random import randint
f=Faker()

def fakeEmployeeData():
    f_empid=randint(a=200, b=999)
    f_name=f.name()
    f_ph=randint(a=6000000000, b=9000000000)
    f_email=f.email()
    emp=EmployeeDetailModel.objects.get_or_create(
        empId=f_empid,
        empName=f_name,
        phoneNum=f_ph,
        email=f_email,
    )

for i in range(1,20):
    fakeEmployeeData()

