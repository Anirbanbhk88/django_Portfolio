from django.shortcuts import render
from projects.models import Project

'''
-----------
view templates for the projects app
-----------
There will be 2 different views for the projects app:
1. An index view that shows a snippet of information about each project
2. A detail view that shows more information on a particular topic
'''


# Create your views here.

def project_index(request):
    '''Fetches all the project data from sqlite db and renders into index page(project_index.html)
    Params:
        request: http request object for GET/POST
    Return:
        rendered index page
    '''
    objProjects = Project.objects.all()
    context = {
        'projects': objProjects
    }
    return render(request, 'project_index.html', context)

def project_detail(request, pk):
    '''Fetches a particular project data from sqlite db and renders into detail page(project_detail.html)
    Params:
        request: http request object for GET/POST
        id: project identifier
    Return:
        rendered index page
    '''
    objProject = Project.objects.get(pk=pk)
    context = {
        'project': objProject
    }
    return render(request, 'project_detail.html', context)