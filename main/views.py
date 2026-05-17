from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.core.mail import EmailMessage
from django.conf import settings
import traceback

from .models import Service, Project, Temoignage, Article
from .forms import ContactForm


def index(request):
    services = Service.objects.all()
    projects = Project.objects.all()
    temoignages = Temoignage.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        service = request.POST.get('service')
        message = request.POST.get('message')
        files = request.FILES.getlist('files[]')

        if not all([name, email, phone, service, message]):
            return JsonResponse({'success': False, 'message': 'Veuillez remplir tous les champs obligatoires.'})

        if len(files) > 5:
            return JsonResponse({'success': False, 'message': 'Maximum 5 fichiers autorisés.'})

        for file in files:
            if file.size > 5 * 1024 * 1024:
                return JsonResponse({'success': False, 'message': f'Le fichier {file.name} est trop volumineux (max 5 Mo).'})

        email_subject = f'Nouvelle demande de devis - {service}'
        email_body = f"""Nouvelle demande de devis reçue depuis le site Performance Habitat

Nom et Prénom : {name}
Email : {email}
Téléphone : {phone}
Service demandé : {service}

Message :
{message}

{len(files)} fichier(s) joint(s)
"""

        try:
            email_message = EmailMessage(
                subject=email_subject,
                body=email_body,
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[settings.CONTACT_EMAIL],
                reply_to=[email],
            )
            for file in files:
                email_message.attach(file.name, file.read(), file.content_type)
            email_message.send(fail_silently=False)

            return JsonResponse({'success': True, 'message': 'Votre demande a été envoyée avec succès ! Nous vous recontacterons rapidement.'})

        except Exception:
            traceback.print_exc()
            return JsonResponse({'success': False, 'message': 'Une erreur est survenue lors de l\'envoi. Veuillez réessayer ou nous appeler directement.'}, status=500)

    context = {
        'services': services,
        'projects': projects,
        'temoignages': temoignages,
        'articles_recents': Article.objects.filter(is_published=True)[:3],
    }
    return render(request, 'index.html', context)


def blog_list(request):
    qs = Article.objects.filter(is_published=True)
    categorie = request.GET.get('categorie')
    featured = None
    if categorie:
        articles = qs.filter(categorie=categorie)
    else:
        featured = qs.first()
        articles = qs[1:] if featured else qs
    counts = {
        'total':       qs.count(),
        'conseil':     qs.filter(categorie='conseil').count(),
        'realisation': qs.filter(categorie='realisation').count(),
        'actualite':   qs.filter(categorie='actualite').count(),
    }
    return render(request, 'blog.html', {
        'articles': articles,
        'featured': featured,
        'categorie_active': categorie,
        'counts': counts,
    })


def blog_detail(request, slug):
    article = get_object_or_404(Article, slug=slug, is_published=True)
    articles_recents = Article.objects.filter(is_published=True).exclude(pk=article.pk)[:3]
    return render(request, 'blog_detail.html', {
        'article': article,
        'articles_recents': articles_recents,
    })


def services_list(request):
    return render(request, 'services.html', {'services': Service.objects.all()})


def projects_list(request):
    return render(request, 'projects.html', {'projects': Project.objects.all()})


def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    images = project.images.all()
    return render(request, 'project_detail.html', {'project': project, 'images': images})


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
