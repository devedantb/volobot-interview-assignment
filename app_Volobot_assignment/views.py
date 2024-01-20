from django.shortcuts import render, redirect
from .models import Student, Section
from .forms import FormSection, FormStudent

# Create your views here.


def School(request):
    return render(request, "app_volo/school.html")


def CreateSection(request):
    if request.method == "POST":
        form = FormSection(request.POST)
        if form.is_valid():
            form.save()
            sections = Section.objects.all()
            return render(
                request, "app_volo/section.html", context={"sections": sections}
            )
        else:
            print(form.errors)

    context = {"section": FormSection()}
    return render(request, "app_volo/section.html", context)


def AddStudents(request):
    if request.method == "POST":
        form = FormStudent(request.POST)
        if form.is_valid():
            form.save()
            students = Student.objects.all()
            return render(
                request, "app_volo/students.html", context={"students": students}
            )
        else:
            print(form.errors)
    context = {"student": FormStudent()}
    return render(request, "app_volo/students.html", context)


def DeleteSection(request, pk):
    section = Section.objects.get(pk=pk)
    section.delete()
    sections = Section.objects.all()
    return render(request, "app_volo/section.html", context={"sections": sections})


def DeleteStudent(request, pk):
    student = Student.objects.get(pk=pk)
    student.delete()
    students = Student.objects.all()
    return render(request, "app_volo/students.html", context={"students": students})
