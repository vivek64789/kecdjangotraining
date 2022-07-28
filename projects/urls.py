from django.urls import path
from . import views

urlpatterns = [
    path('',views.projects, name='projects'),
    path('single-project/<str:id>/',views.project, name='singleProject'),
    path('project/update/<str:id>/',views.updateProject, name='updateProject'),
    path('project/delete/<str:id>/',views.deleteProject, name='deleteProject'),
    path('project/add',views.addProject, name='addProject')
]