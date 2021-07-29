from django.shortcuts import render
from django.http import HttpResponse
from .models import Teacher
# Create your views here.

def list_teachers(request):
    output = [f"id={teacher.id},{teacher.last_name} {teacher.first_name} {teacher.specialisation};" for teacher in Teacher.objects.all()]
    return HttpResponse(output)   
       
#       from django.shortcuts import render

# Create your views here.
