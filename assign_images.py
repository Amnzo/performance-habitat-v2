"""
Assigne une image pertinente à chaque article
en utilisant les images déjà présentes dans le projet.
"""
import os, shutil, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'performance_habitat.settings')
django.setup()

from main.models import Article

MEDIA = 'media'

# Copier les images sources vers media/blog/ avec des noms propres
copies = [
    # (source, destination dans media/blog/)
    ('projects/jolie_salle_de_bain.png',                        'blog/salle-de-bain-renovation-brest.png'),
    ('services/Travaux_de_rénovation_dans_lappartement.png',    'blog/travaux-renovation-appartement-brest.png'),
    ('services/Pose_de_carreaux_dans_un_patio_ensoleillé.png',  'blog/pose-carrelage-brest.png'),
    ('services/ChatGPT_Image_7_nov._2025_14_57_38.png',         'blog/artisan-renovation-finistere.png'),
    ('services/WhatsApp_Image_2025-11-06_at_14.28.11.jpeg',     'blog/chantier-renovation-brest.jpeg'),
    ('blog/cuisine-ouverte-guilers-renovation.jpg',             'blog/renovation-guilers-finistere.jpg'),
    ('projects/princ.webp',                                     'blog/realisation-renovation-brest.webp'),
    ('projects/pric.webp',                                      'blog/projet-renovation-finistere.webp'),
]

for src, dst in copies:
    src_path = os.path.join(MEDIA, src)
    dst_path = os.path.join(MEDIA, dst)
    if os.path.exists(src_path) and not os.path.exists(dst_path):
        shutil.copy2(src_path, dst_path)
        print(f"  Copié : {src} → {dst}")
    elif os.path.exists(dst_path):
        print(f"  Déjà là : {dst}")
    else:
        print(f"  ⚠️ Source introuvable : {src}")

# Assignations article → image (pertinence thématique)
assignments = {
    # Rénovation SDB Brest expertise → image salle de bain dédiée
    'renovation-salle-de-bain-brest-performance-habitat':
        'blog/salle-de-bain-renovation-brest.png',

    # Moderniser SDB → photo de réalisation SDB
    'moderniser-salle-de-bain-brest':
        'blog/renovation-salle-de-bain-brest-realisation.jpg',

    # SDB PMR → image 5 erreurs (salle de bain accessible)
    'salle-de-bain-pmr-brest':
        'blog/5-erreurs-renovation-salle-de-bain.jpg',

    # Réalisation SDB → image réalisation originale
    'renovation-salle-de-bain-brest-realisation':
        'blog/renovation-salle-de-bain-brest-realisation.jpg',

    '5-erreurs-renovation-salle-de-bain':
        'blog/5-erreurs-renovation-salle-de-bain.jpg',

    'pose-carrelage-salle-de-bain-brest':
        'blog/pose-carrelage-brest.png',

    'electricite-brest-renovation-normes':
        'blog/installation-electrique-norme-nf-c-15-100.jpg',

    'mise-aux-normes-electriques-brest-performance-habitat':
        'blog/installation-electrique-norme-nf-c-15-100.jpg',

    'pompe-a-chaleur-brest-finistere-performance-habitat':
        'blog/renovation-energetique-economies-chauffage.jpg',

    'renovation-energetique-economies-chauffage':
        'blog/renovation-energetique-economies-chauffage.jpg',

    'quand-changer-plomberie-signes':
        'blog/quand-changer-plomberie-signes.jpg',

    # Artisan Guilers → chantier rénovation (pas cuisine)
    'artisan-renovation-guilers':
        'blog/travaux-renovation-appartement-brest.png',

    'artisan-renovation-plouzane':
        'blog/travaux-renovation-appartement-brest.png',

    'renovation-appartement-relecq-kerhuon':
        'blog/chantier-renovation-brest.jpeg',

    'renovation-maison-finistere':
        'blog/projet-renovation-finistere.webp',
}

print("\nAssignation des images :")
updated = 0
for slug, img_path in assignments.items():
    try:
        a = Article.objects.get(slug=slug)
        full_path = os.path.join(MEDIA, img_path)
        if os.path.exists(full_path):
            a.image = img_path
            a.save()
            print(f"  ✅ {a.titre[:50]}")
            updated += 1
        else:
            print(f"  ⚠️ Image manquante pour : {slug} ({img_path})")
    except Article.DoesNotExist:
        print(f"  ⚠️ Article introuvable : {slug}")

print(f"\n🎯 {updated} articles mis à jour.")
