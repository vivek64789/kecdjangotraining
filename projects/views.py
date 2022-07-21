from http.client import PROCESSING
from django.http import HttpResponse
from django.shortcuts import render
from .models import Project

# Create your views here.


def projects(request):
    projects = Project.objects.all()
    return render(request, 'projects/projects.html', {'projects':projects})

def project(request, id):
    project = Project.objects.get(id=id)


    context ={'project':project}

    return render(request, 'projects/single-project.html', context=context)