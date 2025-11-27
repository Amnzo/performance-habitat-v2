from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index2', views.index2, name='index2'),
    path('services/', views.services_list, name='services'),
    path('realisations/', views.projects_list, name='projects'),
    path('realisations/<slug:slug>/', views.project_detail, name='project_detail'),
    path('contact/', views.contact, name='contact'),
]
