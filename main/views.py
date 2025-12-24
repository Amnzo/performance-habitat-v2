from django.shortcuts import render, get_object_or_404, redirect
from .models import Service, Project, Testimonial ,Temoignage ,PhotoGalerie , CategorieGalerie
from .forms import ContactForm


from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.conf import settings


from django.http import HttpResponse


from django.http import JsonResponse
from django.core.mail import EmailMessage
from django.conf import settings
import traceback

def contact(request):
    if request.method == "POST":
        try:
            name = request.POST.get("name")
            email = request.POST.get("email")
            message = request.POST.get("message")

            mail = EmailMessage(
                subject=f"Demande de contact de {name}",
                body=f"Email: {email}\n\nMessage:\n{message}",
                from_email=settings.EMAIL_HOST_USER,
                to=[settings.EMAIL_HOST_USER],
                reply_to=[email],
            )

            # Gestion des fichiers joints
            for f in request.FILES.getlist("files[]"):
                mail.attach(f.name, f.read(), f.content_type)

            mail.send()

            # Retour JSON OK
            return JsonResponse({'success': True, 'message': 'Formulaire envoyé avec succès !'})

        except Exception as e:
            # Log de l'erreur pour debug
            print("Erreur envoi email :", e)
            traceback.print_exc()
            return JsonResponse(
                {'success': False, 'message': 'Erreur lors de l\'envoi du formulaire.'}, status=500
            )

    # Si la méthode n'est pas POST
    return JsonResponse(
        {'success': False, 'message': 'Méthode non autorisée.'}, status=405
    )


def contactt(request):
    return
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        service = request.POST.get("service")
        message = request.POST.get("message")

        subject = f"Nouvelle demande de devis - {service}"
        body = f"""
Nom : {name}
Email : {email}
Téléphone : {phone}
Service : {service}

Message :
{message}
"""

        mail = EmailMessage(
            subject,
            body,
            settings.EMAIL_HOST_USER,
            [settings.EMAIL_HOST_USER],  # tu reçois l’email
            reply_to=[email],
        )

        # Gestion des fichiers
        for file in request.FILES.getlist("files[]"):
            mail.attach(file.name, file.read(), file.content_type)

        mail.send()

        return redirect("contact_success")  # ou render direct

    return render(request, "contact.html")





import traceback


# Ajoutez cette fonction après les imports
def test_email_configuration():
    """Test manuel de la configuration email"""
    print("\n" + "=" * 60)
    print("TEST DE CONFIGURATION EMAIL")
    print("=" * 60)

    try:
        # Test de connexion SMTP
        import smtplib
        server = smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT)
        server.ehlo()
        server.starttls()
        print(f"✅ Connexion à {settings.EMAIL_HOST}:{settings.EMAIL_PORT} réussie")

        # Test d'authentification
        try:
            server.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
            print("✅ Authentification réussie")
        except Exception as auth_error:
            print(f"❌ Erreur d'authentification: {auth_error}")
            print("\nPROBABLE CAUSE :")
            print("- Vérifiez que le mot de passe est correct")
            print("- Activez la vérification en 2 étapes sur Google")
            print("- Générez un mot de passe d'application")

        server.quit()

    except Exception as e:
        print(f"❌ Erreur de connexion SMTP: {e}")

    print("=" * 60)

def index(request):
    """Vue principale avec formulaire de contact"""
    services = Service.objects.all()
    projects = Project.objects.all()
    temoignages = Temoignage.objects.all()

    if request.method == 'POST':
        test_email_configuration()
        # Récupération des données du formulaire
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        service = request.POST.get('service')
        message = request.POST.get('message')
        files = request.FILES.getlist('files[]')

        # Validation basique
        if not all([name, email, phone, service, message]):
            return JsonResponse({
                'success': False,
                'message': 'Veuillez remplir tous les champs obligatoires.'
            })

        # Vérification du nombre de fichiers
        if len(files) > 5:
            return JsonResponse({
                'success': False,
                'message': 'Maximum 5 fichiers autorisés.'
            })

        # Vérification de la taille des fichiers
        for file in files:
            if file.size > 5 * 1024 * 1024:  # 5 Mo
                return JsonResponse({
                    'success': False,
                    'message': f'Le fichier {file.name} est trop volumineux (max 5 Mo).'
                })

        # DEBUG: Vérification de la configuration email
        print("=" * 50)
        print("DEBUG EMAIL CONFIGURATION:")
        print(f"EMAIL_HOST_USER: {getattr(settings, 'EMAIL_HOST_USER', 'NON CONFIGURÉ')}")
        print(f"EMAIL_HOST: {getattr(settings, 'EMAIL_HOST', 'NON CONFIGURÉ')}")
        print(f"EMAIL_PORT: {getattr(settings, 'EMAIL_PORT', 'NON CONFIGURÉ')}")
        print(f"EMAIL_USE_TLS: {getattr(settings, 'EMAIL_USE_TLS', 'NON CONFIGURÉ')}")
        print(f"CONTACT_EMAIL: {getattr(settings, 'CONTACT_EMAIL', 'NON CONFIGURÉ')}")
        print(f"DEFAULT_FROM_EMAIL: {getattr(settings, 'DEFAULT_FROM_EMAIL', 'NON CONFIGURÉ')}")
        print(f"Nombre de fichiers: {len(files)}")
        print("=" * 50)

        # Création du corps de l'email
        email_subject = f'Nouvelle demande de devis - {service}'
        email_body = f"""
Nouvelle demande de devis reçue depuis le site Performance Habitat

═══════════════════════════════════════════
INFORMATIONS DU CLIENT
═══════════════════════════════════════════

Nom et Prénom : {name}
Email : {email}
Téléphone : {phone}
Service demandé : {service}

═══════════════════════════════════════════
MESSAGE DU CLIENT
═══════════════════════════════════════════

{message}

═══════════════════════════════════════════
PIÈCES JOINTES
═══════════════════════════════════════════

{len(files) if files else 0} fichier(s) joint(s)

---
Email envoyé depuis le site Performance Habitat
https://www.performance-habitat.fr
"""

        # Création et envoi de l'email
        try:
            print("Création du message email...")
            email_message = EmailMessage(
                subject=email_subject,
                body=email_body,
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[settings.CONTACT_EMAIL],
                reply_to=[email]
            )

            # Ajout des pièces jointes
            print(f"Ajout de {len(files)} pièce(s) jointe(s)...")
            for file in files:
                email_message.attach(file.name, file.read(), file.content_type)

            print("Tentative d'envoi de l'email...")
            email_message.send(fail_silently=False)
            print("✅ Email envoyé avec succès!")

            return JsonResponse({
                'success': True,
                'message': 'Votre demande a été envoyée avec succès ! Nous vous recontacterons rapidement.'
            })

        except Exception as e:
            # Afficher l'erreur complète dans le terminal
            print("=" * 50)
            print("❌ ERREUR LORS DE L'ENVOI EMAIL:")
            print(f"Type d'erreur: {type(e).__name__}")
            print(f"Message d'erreur: {str(e)}")
            print("-" * 50)
            print("Traceback complet:")
            traceback.print_exc()
            print("=" * 50)

            return JsonResponse({
                'success': False,
                'message': f'Erreur d\'envoi: {str(e)}'
            })

    # GET request - affichage de la page
    context = {
        'services': services,
        'projects': projects,
        'temoignages': temoignages,
    }

    return render(request, 'index.html', context)


def index2(request):
    """Vue principale avec formulaire de contact"""
    services = Service.objects.all()
    projects = Project.objects.all()
    temoignages = Temoignage.objects.all()

    if request.method == 'POST':
        test_email_configuration()
        # Récupération des données du formulaire
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        service = request.POST.get('service')
        message = request.POST.get('message')
        files = request.FILES.getlist('files[]')

        # Validation basique
        if not all([name, email, phone, service, message]):
            return JsonResponse({
                'success': False,
                'message': 'Veuillez remplir tous les champs obligatoires.'
            })

        # Vérification du nombre de fichiers
        if len(files) > 5:
            return JsonResponse({
                'success': False,
                'message': 'Maximum 5 fichiers autorisés.'
            })

        # Vérification de la taille des fichiers
        for file in files:
            if file.size > 5 * 1024 * 1024:  # 5 Mo
                return JsonResponse({
                    'success': False,
                    'message': f'Le fichier {file.name} est trop volumineux (max 5 Mo).'
                })

        # DEBUG: Vérification de la configuration email
        print("=" * 50)
        print("DEBUG EMAIL CONFIGURATION:")
        print(f"EMAIL_HOST_USER: {getattr(settings, 'EMAIL_HOST_USER', 'NON CONFIGURÉ')}")
        print(f"EMAIL_HOST: {getattr(settings, 'EMAIL_HOST', 'NON CONFIGURÉ')}")
        print(f"EMAIL_PORT: {getattr(settings, 'EMAIL_PORT', 'NON CONFIGURÉ')}")
        print(f"EMAIL_USE_TLS: {getattr(settings, 'EMAIL_USE_TLS', 'NON CONFIGURÉ')}")
        print(f"CONTACT_EMAIL: {getattr(settings, 'CONTACT_EMAIL', 'NON CONFIGURÉ')}")
        print(f"DEFAULT_FROM_EMAIL: {getattr(settings, 'DEFAULT_FROM_EMAIL', 'NON CONFIGURÉ')}")
        print(f"Nombre de fichiers: {len(files)}")
        print("=" * 50)

        # Création du corps de l'email
        email_subject = f'Nouvelle demande de devis - {service}'
        email_body = f"""
Nouvelle demande de devis reçue depuis le site Performance Habitat

═══════════════════════════════════════════
INFORMATIONS DU CLIENT
═══════════════════════════════════════════

Nom et Prénom : {name}
Email : {email}
Téléphone : {phone}
Service demandé : {service}

═══════════════════════════════════════════
MESSAGE DU CLIENT
═══════════════════════════════════════════

{message}

═══════════════════════════════════════════
PIÈCES JOINTES
═══════════════════════════════════════════

{len(files) if files else 0} fichier(s) joint(s)

---
Email envoyé depuis le site Performance Habitat
https://www.performance-habitat.fr
"""

        # Création et envoi de l'email
        try:
            print("Création du message email...")
            email_message = EmailMessage(
                subject=email_subject,
                body=email_body,
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[settings.CONTACT_EMAIL],
                reply_to=[email]
            )

            # Ajout des pièces jointes
            print(f"Ajout de {len(files)} pièce(s) jointe(s)...")
            for file in files:
                email_message.attach(file.name, file.read(), file.content_type)

            print("Tentative d'envoi de l'email...")
            email_message.send(fail_silently=False)
            print("✅ Email envoyé avec succès!")

            return JsonResponse({
                'success': True,
                'message': 'Votre demande a été envoyée avec succès ! Nous vous recontacterons rapidement.'
            })

        except Exception as e:
            # Afficher l'erreur complète dans le terminal
            print("=" * 50)
            print("❌ ERREUR LORS DE L'ENVOI EMAIL:")
            print(f"Type d'erreur: {type(e).__name__}")
            print(f"Message d'erreur: {str(e)}")
            print("-" * 50)
            print("Traceback complet:")
            traceback.print_exc()
            print("=" * 50)

            return JsonResponse({
                'success': False,
                'message': f'Erreur d\'envoi: {str(e)}'
            })

    # GET request - affichage de la page
    context = {
        'services': services,
        'projects': projects,
        'temoignages': temoignages,
    }

    return render(request, 'index2.html', context)

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
