from django.urls import path
from . import views
urlpatterns =[
    path("",views.voterTable,name="data"),
    path("registerForm/",views.registerVoterInfo,name="createForm"),
    path("update/<int:id>/",views.updateVoterInfo,name="update"),
    path("delete/<int:id>/",views.deleteVoterInfo,name="delete")
]