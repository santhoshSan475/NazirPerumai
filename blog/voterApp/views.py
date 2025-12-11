from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import VoterDetails
from .forms import VoterForm

# Create your views here.


def voterTable(request):
    data = VoterDetails.objects.all()
    return render(request,"voterApp/voterData.html",{"data":data})


def registerVoterInfo(request):
    if request.method == "POST":
        form = VoterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/voterApp/")
        else:
            return HttpResponse("<h1>Something went wrong</h1>")
    form = VoterForm
    return render(request,"voterApp/createVoter.html",{"form":form})



def updateVoterInfo(request,id):
    voterData = VoterDetails.objects.get(id=id)
    if request.method == "POST":
        form = VoterForm(request.POST,instance=voterData)
        if form.is_valid():
            form.save()
            return redirect("/voterApp/")
        else:
            return HttpResponse("<h1>Something went wrong</h1>")
    form = VoterForm
    return render(request,"voterApp/createVoter.html",{"form":form})



def deleteVoterInfo(request,id):
    voterData = VoterDetails.objects.get(id=id)
    voterData.delete()
    return redirect("/voterApp/")









