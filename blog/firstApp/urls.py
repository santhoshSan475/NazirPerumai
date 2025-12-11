from django.urls import path
from . import views

urlpatterns = [
    path("",views.welcomeScript, name="welcome"),
    path("aboutPage/",views.about,name="about1"),
    path("students/<int:count>/",views.studentsCount,name="student"),
    path("home/<int:num>",views.homePage,name="home"),
    path("contactPage/<int:num>",views.contactPage,name="contact"),
    path("incoming/",views.incoming,name="in"),
    path("out-going/",views.outgoing,name="out"),
    path("index-page/",views.indexPage,name="index"),
    path("about-page/",views.aboutPage,name="about")
]


