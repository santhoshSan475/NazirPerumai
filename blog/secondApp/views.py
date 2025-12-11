from django.shortcuts import render

# Create your views here.


def studentForm(request):
    return render(request,'secondApp/studentForm.html')


def studentData(request):
    sName = request.GET.get("name")
    admissionNo = request.GET.get("admissionNo")
    gender = request.GET.get("gender")
    bloodGroup = request.GET.get("bloodGroup")
    phoneNumber = request.GET.get("phoneNumber")
    courseName = request.GET.get("courseName")
    return render(request,'secondApp/studentData.html',{"sName":sName,"admissionNo":admissionNo,"gender":gender,"bloodGroup":bloodGroup,"phoneNumber":phoneNumber,"courseName":courseName})



