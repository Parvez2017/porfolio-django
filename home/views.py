from django.shortcuts import render
from .models import Project, Skill

# Create your views here.
def index(request):
    projects = Project.objects.all()

    context = {
        'projects': projects
    }
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def projects(request):
    return render(request, 'projects.html')

def project(request, project_id):
    return render(request, 'project.html')

def resume(request):
    return render(request, 'resume.html')