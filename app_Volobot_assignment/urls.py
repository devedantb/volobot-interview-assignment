from django.urls import path
from . import views


urlpatterns = [
    path("", views.School, name="home"),
    path("section", views.CreateSection, name="section"),
    path("student", views.AddStudents, name="student"),
    path("delSection/<int:pk>", views.DeleteSection, name="delSection"),
    path("delStudent/<int:pk>", views.DeleteStudent, name="delStudent"),
]
