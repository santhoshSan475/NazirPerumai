from django.urls import path
from . import views

urlpatterns =[
    path("",views.studentForm,name="studentForm"),
    path("student-data/",views.studentData,name="studentData"),
]