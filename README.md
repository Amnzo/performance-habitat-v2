<<<<<<< HEAD
# Performancehabitat
=======
# Performance Habitat - Site Django (squelette)

Ce projet est un squelette Django prêt à personnaliser pour le site vitrine "Performance Habitat".

## Structure
- `main/` : application principale (models, views, templates)
- `performance_habitat/` : paramètres du projet
- `db.sqlite3` : base de données (sera créée après `migrate`)

## Couleurs
- Vert fluo: #A6FF00
- Gris clair: #B0B0B0
- Noir: #1C1C1C
- Blanc: #FFFFFF

## Installer
1. `python -m venv venv && source venv/bin/activate`
2. `pip install -r requirements.txt`
3. `python manage.py migrate`
4. `python manage.py createsuperuser`
5. `python manage.py runserver`

## Notes
- Le formulaire de contact **enregistre les demandes dans la base** (pas d'envoi email).
- Remplace `SECRET_KEY` dans `performance_habitat/settings.py` pour la production.
>>>>>>> b13cc0e (fist push)
