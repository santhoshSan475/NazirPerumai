from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("employees",views.EmployeeInfoView,basename='emp')



urlpatterns = [
    path("students/",views.studentView,name="student"),
    path("students/<int:pk>/",views.studentMoreInfo,name="moreInfo"),
    path("employee/",views.EmployeeViewData.as_view(),name="employee"),
    path("employee/<int:pk>/",views.EmployeeObjectView.as_view(),name="Object"),
    path("",include(router.urls)),
    path("author/",views.AuthorView.as_view()),
    path("quote/",views.QuoteView.as_view())

]