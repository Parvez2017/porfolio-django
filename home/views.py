from django.shortcuts import render, get_object_or_404
from .models import Project, Skill

# Create your views here.
def index(request):
    projects = Project.objects.all()
    skills = Skill.objects.all()

    context = {
        'projects': projects,
        'skills': skills
    }
    return render(request, 'index.html', context)

def about(request):
    skills = Skill.objects.all()

    context = {
        'skills': skills
    }
    return render(request, 'about.html', context)

def projects(request):
    projects = Project.objects.all()

    context = {
        'projects': projects
    }
    return render(request, 'projects.html', context)

def project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    context = {
        'project': project
    }

    return render(request, 'project.html', context)
