from django.shortcuts import render, get_object_or_404, redirect
from .models import Service, Project, Testimonial
from .forms import ContactForm

def index(request):
    services = Service.objects.all()
    projects = Project.objects.all()[:3]
    testimonials = Testimonial.objects.all()[:5]
    for t in testimonials:
        t.range = range(t.note)
    return render(request, 'index.html', {
        'services': services,
        'projects': projects,
        'testimonials': testimonials,
    })

def services_list(request):
    services = Service.objects.all()
    return render(request, 'services.html', {'services': services})

def projects_list(request):
    projects = Project.objects.all()
    return render(request, 'projects.html', {'projects': projects})

def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    return render(request, 'project_detail.html', {'project': project})

def contact(request):
    success = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            success = True
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form, 'success': success})
