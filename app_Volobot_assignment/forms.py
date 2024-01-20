from .models import Section, Student
from django.forms import ModelForm


class FormSection(ModelForm):
    class Meta:
        model = Section
        fields = "__all__"


class FormStudent(ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
