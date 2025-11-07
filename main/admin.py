from django.contrib import admin
from .models import Service, Project, Testimonial, ContactRequest , ServiceDetail
from django.utils.html import format_html



@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('titre',)}
    list_display = ('titre', 'date', 'is_featured')

admin.site.register(Testimonial)
admin.site.register(ContactRequest)

class ServiceDetailInline(admin.TabularInline):
    model = ServiceDetail
    extra = 1  # nombre de lignes vides à afficher pour ajouter rapidement un nouveau détail

# On personnalise l'affichage du modèle Service
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('titre', 'icone_display')  # affiche titre et icône dans la liste
    prepopulated_fields = {'slug': ('titre',)}  # le slug se remplit automatiquement
    inlines = [ServiceDetailInline]

    # pour afficher visuellement l’icône dans l’admin
    def icone_display(self, obj):
        # 1️⃣ If the image is a Font Awesome icon string
        if isinstance(obj.image, str) and "fa-" in obj.image:
            return format_html(f'<i class="{obj.image}" style="font-size:18px;"></i>')

        # 2️⃣ If the image file exists
        elif obj.image and hasattr(obj.image, 'url'):
            return format_html(
                f'<img src="{obj.image.url}" width="80" height="80" style="object-fit:cover;border-radius:8px;" />')

        # 3️⃣ Otherwise: no image
        else:
            return "—"

    icone_display.short_description = "Image / Icône"


# Si tu veux voir aussi ServiceDetail séparément (optionnel)
@admin.register(ServiceDetail)
class ServiceDetailAdmin(admin.ModelAdmin):
    list_display = ('service', 'texte')
