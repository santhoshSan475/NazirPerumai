from django.urls import path
from . import views


urlpatterns = [
    path("",views.employeedetails, name="employee"),
    path("register/",views.registerForm,name="register"),
    path("sample/",views.sampleForm,name="sample")
]