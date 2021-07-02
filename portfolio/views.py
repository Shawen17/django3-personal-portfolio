from django.shortcuts import render
from django.http import HttpResponse
from .models import Project



# Create your views here.

def home(request):
    projects= Project.objects.all()
    a=[]
    for project in projects:
        a.append(project)
    b= a[0]
    c= a[1]

    return render(request,'portfolio/home.html',{'projects':projects,'b':b,'c':c})