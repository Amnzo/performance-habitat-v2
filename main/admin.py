from django.contrib import admin
from .models import (
    Service, Project, Testimonial, ContactRequest,
    ServiceDetail, Temoignage, CategorieGalerie, PhotoGalerie,
    ProjectImage
)
from django.utils.html import format_html


# ---------- Project Images Inline (slider images) ----------
class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 2  # Nombre de champs image affichés par défaut
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        if obj.image and hasattr(obj.image, "url"):
            return format_html(
                '<img src="{}" width="70" style="object-fit:cover;border-radius:6px;" />',
                obj.image.url
            )
        return "—"

    image_preview.short_description = "Aperçu"


# ---------- Project Admin ----------
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('titre',)}
    list_display = ('titre', 'date', 'is_featured')
    inlines = [ProjectImageInline]  # ✅ Ajout pour pouvoir uploader plusieurs images


# ---------- Other Models ----------
@admin.register(ServiceDetail)
class ServiceDetailAdmin(admin.ModelAdmin):
    list_display = ('service', 'texte')


class ServiceDetailInline(admin.TabularInline):
    model = ServiceDetail
    extra = 1


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('titre', 'icone_display')
    prepopulated_fields = {'slug': ('titre',)}
    inlines = [ServiceDetailInline]

    def icone_display(self, obj):
        if isinstance(obj.image, str) and "fa-" in obj.image:
            return format_html(
                '<i class="{}" style="font-size:18px;"></i>', obj.image
            )
        elif obj.image and hasattr(obj.image, "url"):
            return format_html(
                '<img src="{}" width="50" height="50" style="object-fit:cover;border-radius:6px;" />',
                obj.image.url
            )
        return "—"

    icone_display.short_description = "Image / Icône"


@admin.register(Temoignage)
class TemoignageAdmin(admin.ModelAdmin):
    list_display = ('nom', 'localisation', 'note', 'is_visible', 'date')
    list_filter = ('is_visible', 'note', 'date')
    search_fields = ('nom', 'localisation', 'texte')
    ordering = ('-date',)
    list_editable = ('is_visible',)
    readonly_fields = ('date',)


@admin.register(PhotoGalerie)
class PhotoGalerieAdmin(admin.ModelAdmin):
    list_display = ('titre', 'categorie', 'date_ajout', 'actif', 'ordre', 'image_preview')
    list_filter = ('categorie', 'actif', 'date_ajout')
    search_fields = ('titre', 'description')
    ordering = ('ordre', '-date_ajout')
    list_editable = ('actif', 'ordre')

    def image_preview(self, obj):
        if obj.image and hasattr(obj.image, "url"):
            return format_html(
                '<img src="{}" width="50" style="object-fit:cover;border-radius:6px;" />',
                obj.image.url
            )
        return "—"

    image_preview.short_description = "Preview"


admin.site.register(Testimonial)
admin.site.register(ContactRequest)
admin.site.register(CategorieGalerie)
