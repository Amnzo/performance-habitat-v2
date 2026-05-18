"""
Renomme toutes les images de réalisations avec des noms SEO-friendly.
Renomme les fichiers ET met à jour la base de données.
Lancer avec : python rename_project_images.py
"""
import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'performance_habitat.settings')
django.setup()

from main.models import Project, ProjectImage

MEDIA = 'media'

seo_names = {
    'dressing-moderne_dressing':                          'dressing-moderne-guilers',
    'salle-de-bain-et-wc-suspendu-modernes-performance': 'renovation-salle-de-bain-wc-brest',
    'pose-de-cuisine-avec-credence-en-faience-performan': 'pose-cuisine-faience-brest',
    'renovation-totale-dappartement-pfh':                 'renovation-appartement-brest',
    'terrasse-exterieure':                                'terrasse-exterieure-brest',
    'plomberie-chauffage-installation-et-renovation':     'plomberie-chauffage-brest',
}

for slug, base in seo_names.items():
    try:
        p = Project.objects.get(slug=slug)
    except Project.DoesNotExist:
        print(f'⚠️  Projet introuvable : {slug}')
        continue

    print(f'\n=== {slug} → {base} ===')

    # Image principale
    old_main = str(p.image)
    if old_main:
        ext = os.path.splitext(old_main)[1]
        new_main = f'projects/{base}{ext}'
        old_path = os.path.join(MEDIA, old_main)
        new_path = os.path.join(MEDIA, new_main)
        if os.path.exists(old_path) and not os.path.exists(new_path):
            os.rename(old_path, new_path)
            p.image = new_main
            p.save()
            print(f'  ✅ principale renommée → {os.path.basename(new_main)}')
        elif os.path.exists(new_path):
            p.image = new_main
            p.save()
            print(f'  ↩️  principale déjà renommée')
        else:
            print(f'  ⚠️  fichier principal introuvable : {old_main}')

    # Images de détail
    counter = 1
    for pi in p.images.all():
        old_img = str(pi.image)
        ext = os.path.splitext(old_img)[1]
        new_img = f'projects/details/{base}-{counter}{ext}'
        old_path = os.path.join(MEDIA, old_img)
        new_path = os.path.join(MEDIA, new_img)
        if os.path.exists(old_path) and not os.path.exists(new_path):
            os.rename(old_path, new_path)
            pi.image = new_img
            pi.save()
            print(f'  ✅ détail {counter} → {os.path.basename(new_img)}')
        elif os.path.exists(new_path):
            pi.image = new_img
            pi.save()
            print(f'  ↩️  détail {counter} déjà renommé')
        else:
            print(f'  ⚠️  détail introuvable : {old_img}')
        counter += 1

print('\n🎯 Terminé.')
