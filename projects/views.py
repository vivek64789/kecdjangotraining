from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

allProjects = [
    {
        'id':"1",
        'title': 'Django Application',
        'description':'This is description',
        'category':'server'
    },
    {
        'id':"2",
        'title': 'React Application',
        'description':'This is description',
        'category':'client'
    },
    {
        'id':"3",
        'title': 'Angular Application',
        'description':'This is description',
        'category':'client'
    },
]

def projects(request):
    return render(request, 'projects/projects.html', {'projects':allProjects})

def project(request, id):
    project = {}
    for i in allProjects:
        if i['id'] == id:
            project = i

    context ={'project':project}

    return render(request, 'projects/single-project.html', context=context)