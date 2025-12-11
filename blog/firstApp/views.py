from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse

# Create your views here.


def welcomeScript(request):
    return HttpResponse("welcome to Django community")

def about(request):
    return HttpResponse("welcome to about page")


def studentsCount(request,count):
    return HttpResponse(f"Today's student count in alphabet {count}")


def homePage(request,num):
    return redirect(f"/myApp/contactPage/{num}")

def contactPage(request,num):
    return HttpResponse(f"You're in contact page,And number of contact stored in this page is :{num}")


def incoming(request):
    return redirect(reverse("out"))

def outgoing(request):
    return HttpResponse("You're in outgoing page")


def indexPage(request):
    composer = {
        "title":"index Page",
        "name":"harris jayaraj",
        "value":"music composer",
        "description":"J. Harris Jayaraj is an Indian composer from Tamil Nadu. He composes soundtracks predominantly for Tamil films, while also having composed for a few films in Telugu. He has also worked on a few Hindi films that were remakes of his Tamil films."
    }
    return render(request,"firstApp/index.html",composer)


def aboutPage(request):
    return render(request,"firstApp/about.html")


