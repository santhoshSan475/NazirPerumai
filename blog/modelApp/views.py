from django.shortcuts import render
from .models import EmployeeDetails
from .forms import RegisterForm,DemoForm
# Create your views here.


def employeedetails(request):
    empdata = EmployeeDetails.objects.all()
    return render(request,"modelApp/employeedetails.html",{"empdata":empdata})


def registerForm(request):
    form = RegisterForm
    return render(request,"modelApp/registerForm.html",{"form":form})



def sampleForm(request):
    form = DemoForm
    return render(request,"modelApp/sampleForm.html",{"form":form})