from http.client import PROCESSING
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Project
from .forms import ProjectForm

# Create your views here.


def projects(request):
    projects = Project.objects.all()
    return render(request, 'projects/projects.html', {'projects':projects})

def project(request, id):
    project = Project.objects.get(id=id)


    context ={'project':project}

    return render(request, 'projects/single-project.html', context=context)

def addProject(request):
    form = ProjectForm(request.POST)
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {
        'form': form
    }
    return render(request, 'projects/projects-form.html', context=context )

def updateProject(request, id):
    project = Project.objects.get(id=id)
    form=ProjectForm( instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST,request.FILES, instance = project )
        if form.is_valid():
            form.save()
            return redirect('projects')


    context = {
        'form':form,
        'isUpdate':True
    }
    return render(request, 'projects/projects-form.html', context=context )

def deleteProject(request, id):
    project = Project.objects.get(id=id).delete()
    
    return redirect('projects')