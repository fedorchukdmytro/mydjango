"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from mysite.group.views import list_group - какого черта она создалась?
from django.contrib import admin
from django.urls import path

from students import views as students_views
from teachers import views as teachers_views 
from group import views as group_views

urlpatterns = [
    path('list-teachers/', teachers_views.list_teachers),
    path('list-groups/', group_views.list_group),
    path('generate-students/', students_views.generate_students),
    path('generate-student', students_views.generate_student),
    path('list-students', students_views.list_students),
    path('fourthpage', students_views.fourthpage),
    path('thirdpage', students_views.thirdpage),
    path('secondpage/', students_views.secondpage),
    path('hello/', students_views.hello),
    path('admin/', admin.site.urls),
]
 