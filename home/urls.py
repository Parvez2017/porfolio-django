from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('projects', views.projects, name='projects'),
    path('<int:project_id>', views.project, name='project'),
    path('resume', views.resume, name='resume'),

]
