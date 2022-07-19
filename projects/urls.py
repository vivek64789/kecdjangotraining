from django.urls import path
from . import views

urlpatterns = [
    path('projects/',views.projects, name='projects'),
    path('single-project/<str:id>/',views.project, name='singleProject'),
]