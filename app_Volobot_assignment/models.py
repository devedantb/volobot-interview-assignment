from django.db import models


# Create your models here.
class Section(models.Model):
    section_name = models.CharField(max_length=1, unique=True)

    def __str__(self):
        return f"{self.section_name}"


class Student(models.Model):
    student_name = models.CharField(max_length=100)
    roll_number = models.IntegerField(unique=True)
    section_name = models.ForeignKey(Section, on_delete=models.CASCADE)

    def __str__(self):
        return f"name:{self.student_name}, section:{self.section_name}, roll number:{self.roll_number}"
