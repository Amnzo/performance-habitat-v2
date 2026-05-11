import urllib.request
import ssl
from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from main.models import Article

ARTICLES = [
    {
        "titre": "5 erreurs à éviter lors de la rénovation de votre salle de bain",
        "slug": "5-erreurs-renovation-salle-de-bain",
        "categorie": "conseil",
        "resume": "Rénover sa salle de bain est un projet excitant, mais aussi source de nombreuses erreurs coûteuses. Découvrez les 5 pièges les plus fréquents et comment les éviter pour un résultat parfait.",
        "meta_description": "5 erreurs courantes en rénovation salle de bain et comment les éviter. Conseils d'expert par Performance Habitat à Brest.",
        "image_url": "https://images.unsplash.com/photo-1552321554-5fefe8c9ef14?w=800&h=500&fit=crop&auto=format&q=85",
        "contenu": """
<h2>1. Négliger la ventilation</h2>
<p>Une salle de bain mal ventilée est un nid à moisissures. Beaucoup de propriétaires oublient d'installer ou de remplacer la VMC (Ventilation Mécanique Contrôlée), pensant que c'est un détail. C'est pourtant l'une des erreurs les plus coûteuses à corriger après coup.</p>
<blockquote>Un taux d'humidité élevé en salle de bain peut réduire la durée de vie de votre carrelage et de vos joints de moitié.</blockquote>

<h2>2. Sous-estimer le budget</h2>
<p>La rénovation d'une salle de bain réserve souvent des surprises : canalisations à remplacer, sol à reprendre, isolation à renforcer. Prévoyez toujours une <strong>marge de 15 à 20 %</strong> sur votre budget initial pour faire face aux imprévus.</p>

<h2>3. Choisir le mauvais carrelage</h2>
<p>Tous les carreaux ne se valent pas. Un carrelage non adapté à une zone humide (indice de résistance à l'abrasion insuffisant, mauvaise tenue à l'eau) peut se fissurer en quelques mois. Demandez conseil à votre artisan avant d'acheter.</p>

<h2>4. Ignorer les normes électriques</h2>
<p>En salle de bain, des zones de sécurité strictes définissent quels équipements peuvent être installés et où. Une prise mal positionnée peut être dangereuse et vous coûter une mise en conformité lors de la revente de votre bien.</p>

<h2>5. Vouloir tout faire soi-même</h2>
<p>Les tutoriels YouTube donnent parfois l'illusion que la plomberie ou l'électricité sont à la portée de tous. En réalité, une mauvaise installation peut entraîner des dégâts des eaux, des risques d'électrocution et l'invalidation de votre assurance habitation.</p>

<p>Chez <strong>Performance Habitat</strong>, nous réalisons votre rénovation de A à Z, dans les règles de l'art et dans les délais convenus. <a href="/#contact">Contactez-nous pour un devis gratuit.</a></p>
""",
    },
    {
        "titre": "Rénovation complète d’une salle de bain à Brest : notre réalisation",
        "slug": "renovation-salle-de-bain-brest-realisation",
        "categorie": "realisation",
        "resume": "Retour sur la transformation totale d’une salle de bain vieillissante en un espace moderne et fonctionnel à Brest. Carrelage grand format, douche à l’italienne, meuble suspendu.",
        "meta_description": "Réalisation de rénovation salle de bain à Brest par Performance Habitat : douche italienne, carrelage grand format, meuble suspendu.",
        "image_url": "https://images.unsplash.com/photo-1584622650111-993a426fbf0a?w=800&h=500&fit=crop&auto=format&q=85",
        "contenu": """
<h2>Le projet</h2>
<p>Nos clients, un couple installé à Brest depuis 15 ans, souhaitaient transformer leur salle de bain datant des années 90 en un espace contemporain, lumineux et pratique. Budget : 8 500 € — Durée des travaux : 12 jours ouvrés.</p>

<h2>Ce qui a été réalisé</h2>
<ul>
  <li>Dépose complète de l'ancienne installation (baignoire, carrelage, cloisons)</li>
  <li>Mise aux normes de la plomberie et de l'électricité</li>
  <li>Pose d'une douche à l'italienne (90×120 cm) avec paroi en verre trempé</li>
  <li>Carrelage grand format 60×60 cm effet béton ciré</li>
  <li>Installation d'un meuble vasque suspendu double vasque</li>
  <li>Miroir LED avec anti-buée intégré</li>
  <li>Radiateur sèche-serviettes électrique</li>
</ul>

<h2>Le résultat</h2>
<p>Un espace de 6 m² qui semble deux fois plus grand grâce au carrelage clair et aux miroirs. Nos clients sont ravis : <em>« On ne reconnaît plus notre salle de bain, c'est comme être dans un hôtel 4 étoiles ! »</em></p>

<blockquote>Chaque réalisation est unique. Nous adaptons nos solutions à votre espace, vos goûts et votre budget.</blockquote>

<p>Vous avez un projet similaire ? <a href="/#contact">Demandez votre devis gratuit</a> — nous nous déplaçons sur tout le Finistère.</p>
""",
    },
    {
        "titre": "Quand faut-il changer sa plomberie ? Les signes qui ne trompent pas",
        "slug": "quand-changer-plomberie-signes",
        "categorie": "conseil",
        "resume": "Canalisation qui rouille, eau colorée, pression en baisse… Ces signaux d’alarme indiquent que votre installation de plomberie arrive en fin de vie. On fait le point.",
        "meta_description": "Comment savoir si votre plomberie doit être remplacée ? Signes d'alerte et conseils d'expert par Performance Habitat.",
        "image_url": "https://images.unsplash.com/photo-1585771724684-38269d6639fd?w=800&h=500&fit=crop&auto=format&q=85",
        "contenu": """
<h2>L’âge des canalisations</h2>
<p>La durée de vie des canalisations varie selon le matériau : les tuyaux en plomb (interdits mais encore présents dans certaines maisons anciennes) doivent être remplacés d'urgence, les tuyaux en acier galvanisé ont une durée de vie de 40 à 70 ans, et le cuivre peut tenir 50 à 80 ans dans de bonnes conditions.</p>

<h2>Les 5 signes d’alarme</h2>
<ul>
  <li><strong>Eau colorée ou rouillée</strong> : signe de corrosion interne des canalisations.</li>
  <li><strong>Chute de pression</strong> : peut indiquer des fuites ou un dépôt calcaire important.</li>
  <li><strong>Bruit de canalisations</strong> : sifflements, claquements révèlent une usure avancée.</li>
  <li><strong>Fuites récurrentes</strong> : si vous réparez souvent les mêmes endroits, c'est que le réseau est fatigué.</li>
  <li><strong>Taches d'humidité</strong> : sur les murs ou plafonds, même sans fuite visible.</li>
</ul>

<blockquote>Un dégât des eaux non détecté peut causer jusqu'à 30 000 € de dommages. Mieux vaut prévenir que guérir.</blockquote>

<h2>Que faire ?</h2>
<p>La première étape est un <strong>diagnostic complet de votre installation</strong>. Performance Habitat intervient à Brest et dans tout le Finistère pour évaluer l'état de vos canalisations et vous proposer les travaux strictement nécessaires — pas plus.</p>

<p><a href="/#contact">Prenez rendez-vous pour un diagnostic gratuit →</a></p>
""",
    },
    {
        "titre": "Rénovation énergétique : économisez jusqu’à 40 % sur votre chauffage",
        "slug": "renovation-energetique-economies-chauffage",
        "categorie": "actualite",
        "resume": "Isolation, pompe à chaleur, chaudière à condensation… Avec les aides MaPrimeRénov’ et l’éco-PTZ, rénover son logement n’a jamais été aussi accessible. On vous explique tout.",
        "meta_description": "Rénovation énergétique à Brest : aides disponibles et économies possibles. Guide complet par Performance Habitat Finistère.",
        "image_url": "https://images.unsplash.com/photo-1570129477492-45c003edd2be?w=800&h=500&fit=crop&auto=format&q=85",
        "contenu": """
<h2>Pourquoi rénover maintenant ?</h2>
<p>Face à la hausse des prix de l'énergie, la rénovation thermique est devenue une priorité pour de nombreux propriétaires bretons. Un logement classé F ou G peut voir sa facture de chauffage divisée par deux ou trois après travaux.</p>

<h2>Les aides disponibles en 2024</h2>
<ul>
  <li><strong>MaPrimeRénov'</strong> : jusqu'à 20 000 € selon vos revenus et les travaux.</li>
  <li><strong>Éco-PTZ</strong> : prêt à taux zéro jusqu'à 50 000 €.</li>
  <li><strong>TVA à 5,5 %</strong> sur les travaux de rénovation énergétique.</li>
  <li><strong>CEE (Certificats d'Économies d'Énergie)</strong> : primes versées par les fournisseurs d'énergie.</li>
</ul>

<blockquote>Avec le cumul des aides, certains ménages modestes peuvent bénéficier d'une rénovation à 0 € de reste à charge.</blockquote>

<h2>Par où commencer ?</h2>
<p>L'isolation des combles et des murs est généralement le premier levier à activer : elle peut représenter jusqu'à <strong>30 % d'économies</strong> sur la facture annuelle de chauffage. Vient ensuite le remplacement du système de chauffage (pompe à chaleur, chaudière à condensation).</p>

<p>Performance Habitat vous accompagne dans le montage de votre dossier d'aides et réalise les travaux de A à Z. <a href="/#contact">Contactez-nous pour un bilan énergétique gratuit.</a></p>
""",
    },
    {
        "titre": "Installation électrique aux normes NF C 15-100 : pourquoi c’est crucial",
        "slug": "installation-electrique-norme-nf-c-15-100",
        "categorie": "conseil",
        "resume": "La norme électrique NF C 15-100 est obligatoire pour toute installation neuve ou rénovée. On vous explique ce qu’elle implique et pourquoi confier ces travaux à un professionnel.",
        "meta_description": "Norme NF C 15-100 et installation électrique à Brest : ce que vous devez savoir. Conseils Performance Habitat.",
        "image_url": "https://images.unsplash.com/photo-1621905251189-08b45d6a269e?w=800&h=500&fit=crop&auto=format&q=85",
        "contenu": """
<h2>Qu’est-ce que la norme NF C 15-100 ?</h2>
<p>La norme NF C 15-100 est le référentiel français qui définit les règles de conception, de réalisation et d'entretien des installations électriques basse tension dans les locaux d'habitation. Elle est obligatoire depuis 2003 pour toute installation neuve ou entièrement rénovée.</p>

<h2>Ce que la norme impose</h2>
<ul>
  <li>Un tableau électrique avec disjoncteur différentiel 30 mA.</li>
  <li>Des circuits dédiés pour les gros appareils (four, lave-linge, lave-vaisselle).</li>
  <li>Un nombre minimal de prises par pièce (5 prises en salon, 3 en chambre…).</li>
  <li>Des règles strictes en salle de bain (zones de sécurité 0, 1 et 2).</li>
  <li>Une mise à la terre de toute l'installation.</li>
</ul>

<blockquote>Une installation non conforme peut invalider votre assurance habitation en cas de sinistre électrique.</blockquote>

<h2>Les risques d’une installation vieillissante</h2>
<p>En France, environ 30 % des incendies domestiques ont une cause électrique. Un tableau vétuste, des prises sans terre ou des fils à nu sont des dangers silencieux mais réels.</p>

<h2>Notre intervention</h2>
<p>Nos électriciens qualifiés réalisent le diagnostic de votre installation actuelle, planifient la mise aux normes et vous remettent un certificat de conformité (CONSUEL). <a href="/#contact">Demandez votre devis en ligne →</a></p>
""",
    },
    {
        "titre": "Cuisine ouverte à Guilers : une transformation spectaculaire",
        "slug": "cuisine-ouverte-guilers-renovation",
        "categorie": "realisation",
        "resume": "Transformation d’une cuisine cloisonnée en espace de vie ouvert sur le salon. îlot central, plan de travail en quartz, crédence en verre : une réalisation dont nous sommes fiers.",
        "meta_description": "Rénovation cuisine ouverte à Guilers par Performance Habitat. îlot central, quartz, crédence verre. Résultat spectaculaire.",
        "image_url": "https://images.unsplash.com/photo-1556909114-f6e7ad7d3136?w=800&h=500&fit=crop&auto=format&q=85",
        "contenu": """
<h2>Le défi</h2>
<p>Notre client souhaitait abattre une cloison porteuse pour ouvrir sa cuisine sur le salon et créer un espace de vie moderne et convivial. Ce type de travaux nécessite une étude de structure préalable — nous avons fait appel à un bureau d'études pour valider la pose d'un IPN (poutre métallique de soutien).</p>

<h2>Les travaux réalisés</h2>
<ul>
  <li>Étude de structure et pose d'un IPN de 4 mètres</li>
  <li>Dépose de l'ancienne cuisine et de la cloison</li>
  <li>Création d'un îlot central avec rangements et coin repas</li>
  <li>Plan de travail en quartz blanc veiné (résistant et facile d'entretien)</li>
  <li>Crédence en verre laqué blanc</li>
  <li>Électroménager encastré haut de gamme</li>
  <li>Éclairage LED sous meubles et spots encastrés au plafond</li>
</ul>

<blockquote>« On ne voulait plus quitter notre cuisine. Cuisiner est devenu un plaisir depuis la rénovation ! » — M. &amp; Mme Lefebvre, Guilers</blockquote>

<h2>Budget et délais</h2>
<p>Durée des travaux : <strong>3 semaines</strong>. Budget total : <strong>14 200 €</strong> fourniture et pose. Un investissement qui valorise le bien et améliore le quotidien.</p>

<p>Vous souhaitez un projet similaire ? <a href="/#contact">Contactez-nous pour un devis gratuit</a> — déplacement offert sur Brest et le Finistère.</p>
""",
    },
]


class Command(BaseCommand):
    help = "Crée des articles de blog professionnels avec images Unsplash"

    def handle(self, *args, **options):
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE

        created = 0
        skipped = 0

        for data in ARTICLES:
            if Article.objects.filter(slug=data["slug"]).exists():
                self.stdout.write(f"  Existe déjà : {data['titre'][:50]}")
                skipped += 1
                continue

            article = Article(
                titre=data["titre"],
                slug=data["slug"],
                categorie=data["categorie"],
                resume=data["resume"],
                contenu=data["contenu"],
                meta_description=data["meta_description"],
                is_published=True,
            )

            img_url = data.get("image_url")
            if img_url:
                try:
                    req = urllib.request.Request(img_url, headers={"User-Agent": "Mozilla/5.0"})
                    with urllib.request.urlopen(req, context=ctx, timeout=20) as resp:
                        img_content = resp.read()
                    filename = data["slug"] + ".jpg"
                    article.image.save(filename, ContentFile(img_content), save=False)
                    self.stdout.write(f"  Image téléchargée : {filename}")
                except Exception as e:
                    self.stdout.write(self.style.WARNING(f"  Image non téléchargée ({e}) : {data['slug']}"))

            article.save()
            created += 1
            self.stdout.write(self.style.SUCCESS(f"  Créé : {data['titre'][:60]}"))

        self.stdout.write(self.style.SUCCESS(f"\n{created} article(s) créé(s), {skipped} ignoré(s)."))
