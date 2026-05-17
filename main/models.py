from django.db import models
from ckeditor.fields import RichTextField

class Service(models.Model):
    titre = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='services/', blank=True, null=True, default='services/default.jpg')
    description = models.TextField(blank=True, help_text="Description détaillée du service (visible sur la page)")
    meta_description = models.CharField(max_length=160, blank=True, help_text="Description SEO (max 160 caractères)")

    def __str__(self):
        return self.titre



class ServiceDetail(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='details')
    texte = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.service.titre} - {self.texte}"




class Temoignage(models.Model):
    nom = models.CharField(max_length=100)
    localisation = models.CharField(max_length=150, blank=True, null=True)
    texte = models.TextField()
    note = models.PositiveIntegerField(default=5)  # de 1 à 5
    date = models.DateField(auto_now_add=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nom} - {self.localisation or ''}"

class Project(models.Model):
    titre = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = RichTextField()
    image = models.ImageField(upload_to='projects/')
    date = models.DateField(null=True, blank=True)
    is_featured = models.BooleanField(default=False)
    meta_description = models.CharField(max_length=160, blank=True, help_text="Description SEO (max 160 caractères)")
    ville = models.CharField(max_length=100, blank=True, help_text="Ex: Brest, Guilers, Plouzané")
    type_travaux = models.CharField(max_length=100, blank=True, help_text="Ex: Salle de bain, Plomberie")

    def __str__(self):
        return self.titre

    class Meta:
        ordering = ['-date']


class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="projects/details/")
    ordre = models.PositiveIntegerField(default=0)

    # Nouveau champ pour dire si image avant/après
    ETAT_CHOICES = [
        ('avant', 'Avant les travaux'),
        ('apres', 'Après les travaux'),
    ]
    etat = models.CharField(max_length=10, choices=ETAT_CHOICES, default='avant')

    class Meta:
        ordering = ["ordre"]

    def __str__(self):
        return f"image {self.id} - {self.get_etat_display()}"


class Testimonial(models.Model):
    nom = models.CharField(max_length=100)
    contenu = models.TextField()
    note = models.PositiveSmallIntegerField(default=5)

    def __str__(self):
        return f"{self.nom} ({self.note})"

class ContactRequest(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    telephone = models.CharField(max_length=30, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_handled = models.BooleanField(default=False)

    def __str__(self):
        return f"Contact: {self.nom} - {self.email}"


# Dans votre fichier models.py

from django.db import models


class CategorieGalerie(models.Model):
    """Catégories pour filtrer la galerie"""
    nom = models.CharField(max_length=100, verbose_name="Nom de la catégorie")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="Slug (URL)")
    ordre = models.IntegerField(default=0, verbose_name="Ordre d'affichage")

    class Meta:
        verbose_name = "Catégorie de galerie"
        verbose_name_plural = "Catégories de galerie"
        ordering = ['ordre', 'nom']

    def __str__(self):
        return self.nom


class Article(models.Model):
    CATEGORIE_CHOICES = [
        ('conseil',      'Conseils & Astuces'),
        ('realisation',  'Réalisation'),
        ('actualite',    'Actualité'),
    ]

    titre             = models.CharField(max_length=200)
    slug              = models.SlugField(unique=True)
    resume            = models.CharField(max_length=300, help_text="Courte description (affiché dans la liste)")
    contenu           = RichTextField()
    image             = models.ImageField(upload_to='blog/', blank=True, null=True)
    categorie         = models.CharField(max_length=20, choices=CATEGORIE_CHOICES, default='conseil')
    meta_description  = models.CharField(max_length=160, blank=True, help_text="Description SEO (max 160 caractères)")
    mots_cles         = models.CharField(max_length=255, blank=True, help_text="Mots-clés SEO séparés par des virgules")
    auteur            = models.CharField(max_length=100, default='Performance Habitat', help_text="Nom de l'auteur")
    date_publication  = models.DateField(auto_now_add=True)
    date_modification = models.DateField(auto_now=True)
    is_published      = models.BooleanField(default=True, verbose_name="Publié")

    class Meta:
        ordering = ['-date_publication']
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __str__(self):
        return self.titre

    @property
    def temps_lecture(self):
        from django.utils.html import strip_tags
        words = len(strip_tags(self.contenu).split())
        return max(1, round(words / 200))


class PhotoGalerie(models.Model):
    """Photos de la galerie"""
    titre = models.CharField(max_length=200, verbose_name="Titre")
    description = models.TextField(blank=True, verbose_name="Description")
    image = models.ImageField(upload_to='galerie/', verbose_name="Image")
    categorie = models.ForeignKey(
        CategorieGalerie,
        on_delete=models.CASCADE,
        related_name='photos',
        verbose_name="Catégorie"
    )
    date_ajout = models.DateTimeField(auto_now_add=True, verbose_name="Date d'ajout")
    actif = models.BooleanField(default=True, verbose_name="Actif")
    ordre = models.IntegerField(default=0, verbose_name="Ordre d'affichage")

    class Meta:
        verbose_name = "Photo de galerie"
        verbose_name_plural = "Photos de galerie"
        ordering = ['ordre', '-date_ajout']

    def __str__(self):
        return self.titre
