# from students import models
from django.http import HttpResponse
from .models import Student
import random
from faker import Faker
from django import forms

class CountForm(forms.Form):
    count = forms.IntegerField(min_value=1, max_value=100)


fake = Faker()

def hello(request):
    return HttpResponse("Here's the text of th web page")

def secondpage(request):
    return HttpResponse("<h1>TEXT OF tHE SECONDPAGE<h1/>")

def thirdpage(request):
    return HttpResponse("<h1>TEXT OF tHE THIRDPAGE<h1/>")

def fourthpage(request):
    return HttpResponse("<h1>ТЕКСТ ЧЕТВЕРТОЙ СТРАНИЦЫ<h1/>")

def list_students(request):
    student_list = Student.objects.all()
    output = [f"  {student.first_name} {student.last_name}, {student.age};" for student in student_list]
      
    return HttpResponse(output)

def generate_student(request):
    studentadd = Student.objects.create(first_name = fake.first_name(), last_name = fake.last_name(), age =random.randint(18,100))
    output = f"{studentadd.id} {studentadd.first_name} {studentadd.last_name}, {studentadd.age};"
    return HttpResponse(output)

def generate_students(request):
    form = CountForm(request.GET)
    if form.is_valid():
        count = form.cleaned_data['count']
        studentslist = [
            Student.objects.create(first_name = fake.first_name(), last_name = fake.last_name(), age = random.randint(18,100))
            for _ in range(count)
        ]
        output = ', '.join(
            [f'id = {student.id} {student.first_name} {student.last_name}, age = {student.age};'
             for student in studentslist]
        )
    else:
        return HttpResponse(str(form.errors))
    return HttpResponse(str(output))










# def generate_students(request):
#     count = request.GET.get('count')
#     studentslist = []
#     for student in range(0, int(count)):
#         student = Student.objects.create(first_name = fake.first_name(), last_name = fake.last_name(), age =random.randint(18,100))
#         studentslist.append(student)
#     output = ', '.join(
#         [f"id = {student.id} {student.first_name} {student.last_name}, age = {student.age};" for student in studentslist]
#                       )
#     return HttpResponse(str(output))
    
     
     
    #  Student.objects.create