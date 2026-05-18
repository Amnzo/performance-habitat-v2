import os, re, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'performance_habitat.settings')
django.setup()

from main.models import Article

# 1. Rénovation SDB Brest — guide complet prix 2025
a = Article.objects.get(slug='renovation-salle-de-bain-brest-guide')
a.titre = "Rénovation salle de bain à Brest : l'expertise Performance Habitat"
a.slug  = 'renovation-salle-de-bain-brest-performance-habitat'
a.meta_description = "Rénovation de salle de bain à Brest par Performance Habitat, artisan local à Guilers depuis 2013. Plomberie, carrelage, électricité. Devis gratuit ☎ 06 50 03 47 77"
a.save()
print("✅ 1 - Rénovation SDB Brest renommé")

# 2. Douche italienne → Moderniser sa salle de bain
a2 = Article.objects.get(slug='douche-italienne-brest')
a2.titre  = "Moderniser sa salle de bain à Brest : nos solutions et réalisations"
a2.slug   = 'moderniser-salle-de-bain-brest'
a2.meta_description = "Modernisez votre salle de bain à Brest avec Performance Habitat. Carrelage, plomberie, électricité : un seul artisan pour tout. Devis gratuit."
a2.resume = "Votre salle de bain à Brest mérite un coup de jeune ? Performance Habitat, artisan local à Guilers, réalise des transformations complètes clé en main dans toute la région brestoise."
a2.contenu = """<h2>Moderniser sa salle de bain à Brest : par où commencer ?</h2>
<p>Vous habitez à Brest, Guilers, Plouzané ou ailleurs dans le Finistère et votre salle de bain commence à vieillir ? Performance Habitat, artisan local basé à Guilers depuis 2013, réalise des transformations complètes de salle de bain dans toute la région brestoise.</p>
<p>Que vous souhaitiez rafraîchir l'espace ou le repenser entièrement, notre équipe vous accompagne de la conception jusqu'à la livraison clé en main.</p>

<h2>Les transformations les plus demandées à Brest</h2>
<p>Chez nos clients à Brest et dans le Finistère, les projets les plus fréquents sont :</p>
<ul>
<li>Remplacement de la baignoire par une grande douche de plain-pied</li>
<li>Installation d'une nouvelle robinetterie et d'un meuble vasque moderne</li>
<li>Pose de grand format de carrelage effet béton ou marbre</li>
<li>Mise aux normes de l'installation électrique (VMC, éclairage LED)</li>
<li>Amélioration de l'accessibilité (barre d'appui, seuil bas)</li>
</ul>

<h2>Performance Habitat : votre artisan rénovation à Brest</h2>
<p>Ce qui fait la différence avec Performance Habitat, c'est la prise en charge complète de votre projet. Pas de coordination entre plusieurs corps de métier : notre équipe gère la plomberie, le carrelage, l'électricité et les finitions. Un seul interlocuteur du début à la fin.</p>
<p>Nous intervenons sur Brest, Guilers, Plouzané, Le Relecq-Kerhuon, Landerneau, Saint-Renan et tout le Finistère.</p>

<h2>Comment se déroule votre projet avec nous ?</h2>
<ul>
<li><strong>Devis gratuit</strong> : nous nous déplaçons chez vous pour évaluer le chantier</li>
<li><strong>Conception</strong> : nous vous proposons un aménagement adapté à votre espace</li>
<li><strong>Travaux</strong> : notre équipe intervient dans les délais convenus</li>
<li><strong>Livraison</strong> : vous récupérez une salle de bain entièrement terminée et propre</li>
</ul>

<h2>Questions fréquentes</h2>
<p><strong>Combien de temps durent les travaux ?</strong><br>
Une modernisation de salle de bain dure en général entre 7 et 15 jours ouvrés selon l'ampleur du projet.</p>
<p><strong>Intervenez-vous uniquement à Brest ?</strong><br>
Non, Performance Habitat intervient dans tout le Finistère : Guilers, Plouzané, Le Relecq-Kerhuon, Landerneau, Saint-Renan, Landivisiau et les communes voisines.</p>
<p><strong>Proposez-vous des devis gratuits ?</strong><br>
Oui, tous nos devis sont gratuits et sans engagement. Appelez-nous au 06 50 03 47 77 ou utilisez le formulaire de contact.</p>"""
a2.save()
print("✅ 2 - Douche italienne → Moderniser SDB Brest réécrit")

# 3. Pompe à chaleur
a3 = Article.objects.get(slug='pompe-a-chaleur-brest-finistere')
a3.titre = "Pompe à chaleur à Brest et Finistère : installation par Performance Habitat"
a3.slug  = 'pompe-a-chaleur-brest-finistere-performance-habitat'
a3.meta_description = "Installation de pompe à chaleur à Brest et dans le Finistère par Performance Habitat. Artisan qualifié. Devis gratuit ☎ 06 50 03 47 77"
a3.save()
print("✅ 3 - Pompe à chaleur renommé")

# 4. Carrelage
a4 = Article.objects.get(slug='carrelage-salle-de-bain-brest')
a4.titre = "Pose de carrelage salle de bain à Brest : l'artisan Performance Habitat"
a4.slug  = 'pose-carrelage-salle-de-bain-brest'
a4.meta_description = "Pose de carrelage et faïence salle de bain à Brest et Finistère par Performance Habitat. Artisan local, travail soigné. Devis gratuit."
a4.save()
print("✅ 4 - Carrelage renommé")

# 5. Réalisation SDB — supprimer mentions de budget/prix
a5 = Article.objects.get(slug='renovation-salle-de-bain-brest-realisation')
a5.contenu = re.sub(r'Budget\s*:\s*[\d\s&nbsp;]+€', '', a5.contenu)
a5.contenu = re.sub(r'8\s*500\s*€', '', a5.contenu)
a5.contenu = re.sub(r'8&nbsp;500\s*€', '', a5.contenu)
a5.save()
print("✅ 5 - Mentions budget supprimées de la réalisation")

# 6. Électricité NF C 15-100
a6 = Article.objects.get(slug='installation-electrique-norme-nf-c-15-100')
a6.titre = "Mise aux normes électriques à Brest : l'expertise Performance Habitat"
a6.slug  = 'mise-aux-normes-electriques-brest-performance-habitat'
a6.meta_description = "Mise aux normes de votre installation électrique à Brest et Finistère par Performance Habitat. Sécurité garantie. Devis gratuit ☎ 06 50 03 47 77"
a6.save()
print("✅ 6 - Électricité NF C 15-100 renommé")

print("\n🎯 Tous les articles mis à jour avec succès.")
