from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("routes", views.getRoutes, name="routes"),
    path("getsection", views.get_sections, name="getsections"),
    path("getstudent", views.get_students, name="getstudents"),
    path("getsection/<int:pk>", views.section_api, name="getsection"),
    path("getstudent/<int:pk>", views.student_api, name="getstudent"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
