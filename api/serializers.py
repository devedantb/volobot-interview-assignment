from rest_framework import serializers
from app_Volobot_assignment.models import Section, Student


class SerSection(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = "__all__"


class SerStudent(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"
