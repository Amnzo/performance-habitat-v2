"""
Script d'import des avis Google → modèle Temoignage
Lancer avec : python manage.py shell < load_avis.py
"""
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'performance_habitat.settings')
django.setup()

from main.models import Temoignage

# Supprimer les anciens témoignages avant import
Temoignage.objects.all().delete()

avis = [
    {
        "nom": "jean-edouard jarniou",
        "localisation": "Brest, Finistère",
        "texte": "J'ai fait appel à eux pour une rénovation d'appartement et je suis extrêmement satisfait de leur travail et de leurs conseils. Les tarifs sont cohérents aussi. Je recommande vivement.",
        "note": 5,
    },
    {
        "nom": "marbaud ivan",
        "localisation": "Finistère",
        "texte": "J'ai fait appel à cette entreprise pour la rénovation de ma maison (électricité, plomberie, création et rénovation de salles de bain). Travail sérieux, équipe professionnelle. Je recommande.",
        "note": 5,
    },
    {
        "nom": "H D",
        "localisation": "Brest",
        "texte": "Performance Habitat est une équipe très professionnelle et propre. Ils ont refait mon électricité et ma salle de bain. Très beau travail et de qualité. Je recommande cette entreprise à tous.",
        "note": 5,
    },
    {
        "nom": "Laurent Allamigeon",
        "localisation": "Finistère",
        "texte": "Pose de parquet dans toute ma maison. Le résultat est parfait. Rien à redire sur la prestation, la sympathie et le professionnalisme de Performance Habitat. Je recommande vivement !",
        "note": 5,
    },
    {
        "nom": "Pascal Glevarec",
        "localisation": "Finistère",
        "texte": "Entreprise sérieuse, pas de soucis de coordination entre les différents corps de métier : ils font tout ! Force de proposition, à l'écoute, travail propre et soigné. Je recommande.",
        "note": 5,
    },
    {
        "nom": "GAUTHIER Annie",
        "localisation": "Guilers",
        "texte": "Je suis très satisfaite de cette entreprise pour leur professionnalisme, leur écoute, leur travail précis et de plus une équipe très sympathique. Je vais maintenant pouvoir profiter de ma terrasse sur plots.",
        "note": 5,
    },
    {
        "nom": "François Dorval",
        "localisation": "Brest",
        "texte": "Très bonne entreprise, l'équipe est efficace, rapide et sympathique. Les travaux réalisés nous ont donné entière satisfaction.",
        "note": 5,
    },
    {
        "nom": "hirel cyrille",
        "localisation": "Finistère",
        "texte": "Travail de qualité, chantier livré en temps et en heure. Le patron très sympa en plus de cela. Merci Performance Habitat.",
        "note": 5,
    },
    {
        "nom": "Vinicius Junior",
        "localisation": "Brest",
        "texte": "Entreprise très professionnelle, à l'écoute et efficace du début à la fin, avec un travail de grande qualité. Je recommande vivement !",
        "note": 5,
    },
    {
        "nom": "Ariipaea Rocka",
        "localisation": "Finistère",
        "texte": "Une équipe très professionnelle et rigoureuse. À l'écoute de vos projets, ils savent vous proposer les meilleures solutions. Je recommande.",
        "note": 5,
    },
    {
        "nom": "Pierre Pors",
        "localisation": "Brest",
        "texte": "Très satisfait de la rénovation de ma salle de bain et de mes WC. Travail de qualité avec de belles finitions. Equipe sérieuse et professionnelle. Je recommande sans hésitation.",
        "note": 5,
    },
    {
        "nom": "jean-yves noret",
        "localisation": "Finistère",
        "texte": "Personnel très compétent et très réactif. Jamais de problème, toujours des solutions. Je recommande.",
        "note": 5,
    },
    {
        "nom": "yann de jonghe",
        "localisation": "Guilers",
        "texte": "Entreprise réactive, sérieuse et force de proposition. À l'écoute de mes demandes, je recommande vivement les yeux fermés.",
        "note": 5,
    },
    {
        "nom": "Steven Martin",
        "localisation": "Brest",
        "texte": "Je recommande vivement ! Très professionnel et résultat impeccable, délais honorés. Allez-y les yeux fermés.",
        "note": 5,
    },
    {
        "nom": "Marie louise Ker vella",
        "localisation": "Finistère",
        "texte": "Bon travail, rapide, personnel compétent et prise en charge complète de l'appartement, à l'écoute. Je conseille vivement.",
        "note": 5,
    },
    {
        "nom": "Huguette Prigent",
        "localisation": "Finistère",
        "texte": "Travail très bien exécuté par une équipe bien sympathique et compétente.",
        "note": 5,
    },
    {
        "nom": "Laurent BLIN",
        "localisation": "Brest",
        "texte": "Travaux parfaitement réalisés par Performance Habitat pour un résultat qui correspondait tout à fait à nos attentes. Équipe sérieuse et professionnelle.",
        "note": 5,
    },
    {
        "nom": "ROCKA marion",
        "localisation": "Finistère",
        "texte": "Un plaisir d'avoir fait appel à cette équipe, toujours à l'écoute des besoins et qui met à notre service toutes leurs compétences.",
        "note": 5,
    },
    {
        "nom": "f guennoc",
        "localisation": "Finistère",
        "texte": "Équipe sérieuse et ponctuelle, tarifs compétitifs. Je conseille vivement !",
        "note": 5,
    },
    {
        "nom": "Audrey Abily",
        "localisation": "Brest",
        "texte": "Efficace et agréable. Je recommande sans hésitation.",
        "note": 5,
    },
]

created = 0
for a in avis:
    Temoignage.objects.create(**a)
    created += 1

print(f"✅ {created} avis importés avec succès.")
