from django.shortcuts import render
from django.http import HttpResponse
from .models import Group
# Create your views here.

def list_group(request):
    output = ', '.join(
        [f"id = {group.id}, {group.discipline}, hours amount = {group.hours};;;" for group in Group.objects.all()]
                      )  
    return HttpResponse(output)   
       
#       