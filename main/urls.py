from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name="contact"),
    path('services/', views.services_list, name='services'),
    path('realisations/', views.projects_list, name='projects'),
    path('realisations/<slug:slug>/', views.project_detail, name='project_detail'),
    path('blog/', views.blog_list, name='blog'),
    path('blog/<slug:slug>/', views.blog_detail, name='blog_detail'),
]
