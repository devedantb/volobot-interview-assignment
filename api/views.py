from django.http import JsonResponse
from app_Volobot_assignment.models import Section, Student
from .serializers import SerSection, SerStudent
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(["GET"])
def getRoutes(request):
    routes = [
        "GET /api",
        "GET /getsection",
        "GET /api/getsection/id",
        "GET /getstudent",
        "GET /api/getstudent/id",
    ]
    return Response(routes)


@api_view(["GET", "POST"])
def get_sections(request, format=None):
    if request.method == "GET":
        sections = Section.objects.all()
        serData = SerSection(sections, many=True)
        return JsonResponse(serData.data, safe=False)
    if request.method == "POST":
        serData = SerSection(data=request.data)
        if serData.is_valid():
            serData.save()
            return Response(serData.data, status=status.HTTP_201_CREATED)


@api_view(["GET", "POST"])
def get_students(request, format=None):
    if request.method == "GET":
        students = Student.objects.all()
        serData = SerStudent(students, many=True)
        return JsonResponse(serData.data, safe=False)
    if request.method == "POST":
        serData = SerStudent(data=request.data)
        if serData.is_valid():
            serData.save()
            return Response(serData.data, status=status.HTTP_201_CREATED)


@api_view(["POST", "GET", "PUT", "DELETE"])
def student_api(request, pk, format=None):
    try:
        student = Student.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "POST":
        serData = SerStudent(data=request.data)
        if serData.is_valid():
            serData.save()
            return Response(serData.data, status=status.HTTP_201_CREATED)
    elif request.method == "GET":
        serData = SerStudent(student)
        return Response(serData.data)
    elif request.method == "PUT":
        serData = SerStudent(student, data=request.data)
        if serData.is_valid():
            serData.save()
            return Response(serData.data)
        return Response(serData.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        student.delete()
        return Response(status=status.HTTP_200_OK)


@api_view(["POST", "GET", "PUT", "DELETE"])
def section_api(request, pk, format=None):
    try:
        section = Section.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "POST":
        serData = SerSection(data=request.data)
        if serData.is_valid():
            serData.save()
            return Response(serData.data)
    elif request.method == "GET":
        serData = SerSection(section)
        return Response(serData.data)
    elif request.method == "PUT":
        serData = SerSection(section, data=request.data)
        if serData.is_valid():
            serData.save()
            return Response(serData.data)
        return Response(serData.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        section.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
