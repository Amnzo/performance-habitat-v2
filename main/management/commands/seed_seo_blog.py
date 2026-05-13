from django.core.management.base import BaseCommand
from main.models import Article

WEAK_SLUGS = ['cuisine-ouverte-guilers-renovation']

ARTICLES = [
    # ── ARTICLE 1 ── Rénovation salle de bain Brest (guide principal)
    {
        "titre": "Rénovation salle de bain à Brest : guide complet et prix 2025",
        "slug": "renovation-salle-de-bain-brest-guide",
        "categorie": "conseil",
        "image": "blog/renovation-salle-de-bain-brest-realisation.jpg",
        "resume": "Tout savoir sur la rénovation de salle de bain à Brest : étapes, budget, tendances 2025 et conseils d'expert. Performance Habitat, artisan local en Finistère.",
        "meta_description": "Rénovation salle de bain à Brest : étapes, prix 2025 et conseils d'expert. Devis gratuit — Performance Habitat, artisan Finistère ☎ 06 50 03 47 77",
        "contenu": """
<h2>Rénover sa salle de bain à Brest : par où commencer ?</h2>
<p>Vous habitez à <strong>Brest</strong> ou dans le Finistère et vous souhaitez rénover votre salle de bain ? <strong>Performance Habitat</strong>, artisan local basé à Guilers, réalise des rénovations complètes de salle de bain à Brest et dans tout le Finistère. Dans ce guide, nous vous expliquons tout ce qu'il faut savoir avant de vous lancer.</p>

<h2>Pourquoi rénover sa salle de bain à Brest en 2025 ?</h2>
<p>La salle de bain est l'une des pièces qui valorisent le plus un bien immobilier. À Brest, une salle de bain moderne peut augmenter la valeur d'un appartement de 5 à 10 %. Mais au-delà de la plus-value, c'est votre confort quotidien qui s'améliore durablement.</p>

<h3>Les principales raisons de rénover</h3>
<ul>
  <li>Salle de bain vieillissante (carrelage fissuré, joints noircis, humidité)</li>
  <li>Manque de fonctionnalité et de rangements</li>
  <li>Mise aux normes de la plomberie et de l'installation électrique</li>
  <li>Adaptation PMR pour les personnes âgées ou à mobilité réduite</li>
  <li>Économies d'eau et d'énergie grâce à des équipements plus récents</li>
</ul>

<h2>Les étapes d'une rénovation salle de bain à Brest</h2>

<h3>1. Diagnostic et conception</h3>
<p>Notre équipe se déplace chez vous à Brest pour évaluer l'état de la plomberie, de l'électricité, de l'étanchéité et du carrelage existant. Nous identifions les contraintes techniques et vous proposons un plan adapté à votre espace et votre budget.</p>

<h3>2. Démolition et gros œuvre</h3>
<p>Dépose de l'ancien carrelage, enlèvement des sanitaires, modification éventuelle de cloisons. Nos artisans protègent vos autres pièces et gèrent l'évacuation des déchets. Cette phase dure généralement 1 à 2 jours.</p>

<h3>3. Plomberie et électricité</h3>
<p>Le cœur technique de votre rénovation. Nos plombiers et électriciens qualifiés réalisent les arrivées et évacuations d'eau, la mise aux normes électriques (zones de sécurité, câblage, tableau). Découvrez nos <a href="/services/">services de plomberie et d'électricité</a>.</p>

<h3>4. Étanchéité et carrelage</h3>
<p>Pose du système d'étanchéité sous la douche, application de résines dans les zones humides, puis pose du carrelage et de la faïence avec joints de qualité. Un travail de précision pour une durabilité maximale.</p>

<h3>5. Installation des équipements</h3>
<p>Douche à l'italienne, meuble vasque suspendu, robinetterie, miroir LED anti-buée, radiateur sèche-serviettes — tout est installé soigneusement selon vos choix.</p>

<h2>Quel budget pour une rénovation salle de bain à Brest ?</h2>

<h3>Rénovation légère (2 000 € – 4 500 €)</h3>
<p>Remplacement des sanitaires, peinture ou faïence partielle, changement du mitigeur. Idéal pour rafraîchir sans tout refaire.</p>

<h3>Rénovation complète (5 000 € – 9 000 €)</h3>
<p>Dépose totale, nouvelle plomberie, nouveau carrelage sol et mur, douche italienne, meuble vasque suspendu, radiateur sèche-serviettes. C'est le projet le plus courant à Brest.</p>

<h3>Rénovation haut de gamme (10 000 € – 18 000 €)</h3>
<p>Grandes surfaces, matériaux premium, double vasque, domotique, colonne hydromassante.</p>

<blockquote>Performance Habitat propose des devis gratuits et transparents. Tout est chiffré avant le début des travaux — aucune mauvaise surprise.</blockquote>

<h2>Tendances salle de bain 2025 à Brest</h2>

<h3>La douche à l'italienne</h3>
<p>Incontournable en 2025, la douche à l'italienne offre un gain d'espace visuel et facilite l'entretien. Performance Habitat réalise des <a href="/blog/douche-italienne-brest/">douches à l'italienne à Brest</a> sur mesure, avec receveur extra-plat ou carrelage au sol.</p>

<h3>Le carrelage grand format</h3>
<p>Les carreaux 60×60 cm ou 90×90 cm donnent un effet de grandeur, réduisent les joints et modernisent instantanément l'espace.</p>

<h3>Le style épuré</h3>
<p>Robinetterie encastrée, meuble suspendu, miroir LED large — le minimalisme est la tendance forte de 2025.</p>

<h2>Pourquoi choisir Performance Habitat pour votre salle de bain à Brest ?</h2>
<ul>
  <li><strong>Artisan local</strong> basé à Guilers, à deux minutes de Brest</li>
  <li><strong>Équipe complète</strong> : plombier, électricien, carreleur — un seul interlocuteur</li>
  <li><strong>Délais respectés</strong> et communication transparente tout au long du chantier</li>
  <li><strong>Garantie décennale</strong> sur tous nos travaux</li>
</ul>

<p>Retrouvez quelques-unes de nos <a href="/realisations/">réalisations de salle de bain à Brest et en Finistère</a>.</p>

<div style="background:rgba(196,255,14,0.08);border-left:4px solid #c4ff0e;padding:1.5rem;margin:2rem 0;border-radius:0 8px 8px 0;">
  <h3 style="color:#c4ff0e;margin-top:0;">Votre projet de rénovation à Brest</h3>
  <p>Contactez Performance Habitat pour un devis gratuit et sans engagement. Nous nous déplaçons à Brest, Guilers, Plouzané, Le Relecq-Kerhuon, Bohars, Gouesnou et dans tout le Finistère.</p>
  <p><a href="/#contact"><strong>→ Demander mon devis gratuit</strong></a> &nbsp;|&nbsp; <a href="tel:0650034777"><strong>☎ 06 50 03 47 77</strong></a></p>
</div>
""",
    },

    # ── ARTICLE 2 ── Douche italienne Brest
    {
        "titre": "Douche à l'italienne à Brest : prix, installation et conseils 2025",
        "slug": "douche-italienne-brest",
        "categorie": "conseil",
        "image": "blog/renovation-salle-de-bain-brest-realisation.jpg",
        "resume": "La douche à l'italienne est la tendance phare de la rénovation salle de bain à Brest. Prix, installation, matériaux : tout ce qu'il faut savoir avant de se lancer.",
        "meta_description": "Douche à l'italienne à Brest : prix, installation et conseils 2025. Artisan Performance Habitat — Finistère. Devis gratuit ☎ 06 50 03 47 77",
        "contenu": """
<h2>La douche à l'italienne à Brest : la transformation la plus demandée</h2>
<p>À Brest et dans tout le Finistère, la <strong>douche à l'italienne</strong> est de loin la transformation la plus demandée lors d'une rénovation de salle de bain. Accessible, esthétique et facile d'entretien, elle transforme radicalement l'espace. Performance Habitat réalise des douches à l'italienne clé en main sur toute la zone de Brest.</p>

<h2>Qu'est-ce qu'une douche à l'italienne ?</h2>
<p>La douche à l'italienne (ou douche de plain-pied) est une douche sans bac ni rebord : le sol de la douche est dans la continuité du sol de la salle de bain, avec simplement une légère pente vers le siphon de sol. Elle peut être fermée par une paroi en verre trempé, un demi-mur ou être totalement ouverte.</p>

<h3>Les avantages</h3>
<ul>
  <li><strong>Esthétique</strong> : espace ouvert, lignes épurées, effet hôtel de luxe</li>
  <li><strong>Accessibilité</strong> : idéale pour les personnes âgées ou à mobilité réduite (pas de rebord à enjamber)</li>
  <li><strong>Entretien simplifié</strong> : moins de joints, moins de recoins</li>
  <li><strong>Gain d'espace visuel</strong> : la salle de bain paraît plus grande</li>
  <li><strong>Valorisation immobilière</strong> : très appréciée des acheteurs à Brest</li>
</ul>

<h2>Quel est le prix d'une douche à l'italienne à Brest ?</h2>

<h3>Douche à l'italienne standard (900 € – 2 500 €)</h3>
<p>Receveur extra-plat 80×80 ou 90×90 cm, paroi en verre trempé simple, mitigeur thermostatique et pommeau de douche de qualité. Solution économique et fiable.</p>

<h3>Douche à l'italienne carrelée (2 500 € – 5 500 €)</h3>
<p>Le sol est carrellé (même carrelage que le reste de la salle de bain), siphon de sol linéaire, paroi en verre ou niche de rangement encastrée. Le résultat est haut de gamme et entièrement personnalisable.</p>

<h3>Douche à l'italienne premium (5 500 € – 9 000 €)</h3>
<p>Colonne de douche avec jets latéraux, carrelage grand format, niches murales, paroi en verre sur mesure, robinetterie encastrée dans la paroi.</p>

<blockquote>Le prix inclut la démolition de l'existant, les travaux d'étanchéité, la plomberie, la pose du carrelage et l'installation des équipements.</blockquote>

<h2>Les étapes d'installation par Performance Habitat</h2>

<h3>1. Étude technique</h3>
<p>Vérification de la faisabilité : hauteur de plancher disponible pour le siphon, état des évacuations existantes, contraintes d'étanchéité.</p>

<h3>2. Travaux d'étanchéité</h3>
<p>L'étanchéité est la partie la plus critique. Nous appliquons un système d'étanchéité sous carrelage (SPEC) certifié, qui protège durablement la structure de votre logement contre les infiltrations d'eau.</p>

<h3>3. Pose du carrelage et du siphon</h3>
<p>Le carrelage est posé avec la pente réglementaire (1 à 2 %) vers le siphon de sol ou linéaire. Nous utilisons des carreaux antidérapants de qualité (norme R10 minimum en zone humide).</p>

<h3>4. Pose de la paroi et des équipements</h3>
<p>Paroi en verre trempé sécurit, mitigeur thermostatique, pommeau de douche ou colonne — tout est installé et réglé.</p>

<h2>Douche à l'italienne et salle de bain PMR</h2>
<p>La douche de plain-pied est particulièrement adaptée aux <strong>salles de bain PMR</strong> (Personnes à Mobilité Réduite). Sans rebord, elle facilite l'accès pour les personnes âgées, handicapées ou en fauteuil roulant. Performance Habitat réalise des <a href="/blog/salle-de-bain-pmr-brest/">salles de bain PMR à Brest</a> conformes aux normes d'accessibilité.</p>

<h2>Nos réalisations à Brest et en Finistère</h2>
<p>Découvrez nos <a href="/realisations/">projets de rénovation de salle de bain</a> réalisés à Brest, Guilers, Plouzané et dans tout le Finistère. Chaque réalisation est unique — nous adaptons chaque douche à l'italienne à la configuration de votre espace.</p>

<div style="background:rgba(196,255,14,0.08);border-left:4px solid #c4ff0e;padding:1.5rem;margin:2rem 0;border-radius:0 8px 8px 0;">
  <h3 style="color:#c4ff0e;margin-top:0;">Vous voulez une douche à l'italienne à Brest ?</h3>
  <p>Contactez Performance Habitat pour un devis gratuit. Nous nous déplaçons à Brest, Guilers, Plouzané, Bohars, Gouesnou et dans tout le Finistère.</p>
  <p><a href="/#contact"><strong>→ Demander mon devis gratuit</strong></a> &nbsp;|&nbsp; <a href="tel:0650034777"><strong>☎ 06 50 03 47 77</strong></a></p>
</div>
""",
    },

    # ── ARTICLE 3 ── Salle de bain PMR Brest
    {
        "titre": "Salle de bain PMR à Brest : accessibilité, normes et réalisation",
        "slug": "salle-de-bain-pmr-brest",
        "categorie": "conseil",
        "image": "blog/renovation-salle-de-bain-brest-realisation.jpg",
        "resume": "Adapter votre salle de bain pour les personnes à mobilité réduite à Brest. Normes PMR, aides financières et réalisations par Performance Habitat en Finistère.",
        "meta_description": "Salle de bain PMR à Brest : adaptation, normes et aides financières. Performance Habitat réalise votre salle de bain accessible en Finistère.",
        "contenu": """
<h2>Salle de bain PMR à Brest : l'accessibilité pour tous</h2>
<p>La rénovation d'une <strong>salle de bain PMR</strong> (Personne à Mobilité Réduite) est un projet qui concerne de nombreux foyers à Brest et dans le Finistère. Que vous souhaitiez adapter votre salle de bain pour une personne âgée, un proche handicapé ou anticiper votre propre vieillissement, <strong>Performance Habitat</strong> vous accompagne de A à Z.</p>

<h2>Qu'est-ce qu'une salle de bain PMR ?</h2>
<p>Une salle de bain PMR est conçue pour être utilisée de manière autonome et sécurisée par des personnes à mobilité réduite, en fauteuil roulant, âgées ou souffrant de handicaps moteurs. Elle intègre des équipements spécifiques et respecte des normes d'espace et d'accessibilité précises.</p>

<h3>Les équipements d'une salle de bain PMR</h3>
<ul>
  <li><strong>Douche à l'italienne</strong> : sans rebord, accessible en fauteuil, avec siège de douche rabattable</li>
  <li><strong>Barres d'appui</strong> : fixées dans la douche, près des WC et du lavabo</li>
  <li><strong>Lavabo à hauteur variable</strong> ou ergonomique, dégagé en dessous pour le fauteuil</li>
  <li><strong>Mitigeur thermostatique</strong> : évite les risques de brûlure, facile à manipuler</li>
  <li><strong>Sol antidérapant</strong> : carrelage classe R11 minimum dans la zone de douche</li>
  <li><strong>Espace de circulation</strong> : au moins 80 cm de passage libre, aire de rotation de 150 cm de diamètre</li>
</ul>

<h2>Les normes à respecter pour une salle de bain PMR à Brest</h2>
<p>Pour les logements neufs ou les travaux importants, la réglementation impose des critères d'accessibilité. Pour une adaptation de l'existant, les normes sont moins contraignantes mais nous vous guidons pour créer un espace vraiment fonctionnel.</p>

<h3>Espaces minimaux recommandés</h3>
<ul>
  <li>Largeur de porte : minimum 80 cm (90 cm idéal)</li>
  <li>Espace libre devant le lavabo : 70 cm de profondeur</li>
  <li>Aire de rotation en fauteuil : cercle de 150 cm de diamètre</li>
  <li>Douche : dimension minimale 90×90 cm, idéalement 120×90 cm</li>
</ul>

<h2>Les aides financières pour une salle de bain PMR</h2>

<h3>MaPrimeAdapt'</h3>
<p>Depuis 2024, <strong>MaPrimeAdapt'</strong> finance jusqu'à 70 % des travaux d'adaptation du logement pour les personnes âgées et handicapées, dans la limite de 22 000 € de travaux. C'est l'aide principale pour une rénovation PMR à Brest.</p>

<h3>Aide de l'ANAH</h3>
<p>L'Agence Nationale de l'Habitat (ANAH) finance les travaux d'adaptation aux personnes à faibles revenus. Le montant peut couvrir jusqu'à 50 % du coût des travaux.</p>

<h3>Aide des caisses de retraite</h3>
<p>Certaines caisses de retraite (CARSAT notamment) proposent des aides pour les travaux d'accessibilité du domicile, sous conditions de ressources.</p>

<h3>Crédit d'impôt</h3>
<p>Un crédit d'impôt est disponible pour les équipements spécifiques PMR (barres d'appui, siège de douche, lavabo adapté) — renseignez-vous auprès de votre conseiller fiscal.</p>

<blockquote>Performance Habitat vous aide à identifier et à monter votre dossier d'aides financières. Nous vous accompagnons dans chaque démarche.</blockquote>

<h2>Nos réalisations de salle de bain PMR en Finistère</h2>
<p>Performance Habitat a réalisé de nombreuses adaptations de salle de bain PMR à Brest, Guilers, Plouzané et dans tout le Finistère. Chaque projet est unique — nous adaptons les solutions à votre espace et à vos besoins spécifiques. Consultez nos <a href="/realisations/">réalisations</a> pour vous inspirer.</p>

<p>Vous souhaitez également envisager une <a href="/blog/douche-italienne-brest/">douche à l'italienne</a> dans votre projet PMR ? C'est la combinaison idéale.</p>

<div style="background:rgba(196,255,14,0.08);border-left:4px solid #c4ff0e;padding:1.5rem;margin:2rem 0;border-radius:0 8px 8px 0;">
  <h3 style="color:#c4ff0e;margin-top:0;">Adapter votre salle de bain à Brest</h3>
  <p>Contactez Performance Habitat pour un devis gratuit. Nous vous conseillons sur les équipements, les aides disponibles et réalisons vos travaux à Brest et dans tout le Finistère.</p>
  <p><a href="/#contact"><strong>→ Demander mon devis gratuit</strong></a> &nbsp;|&nbsp; <a href="tel:0650034777"><strong>☎ 06 50 03 47 77</strong></a></p>
</div>
""",
    },

    # ── ARTICLE 4 ── Électricité Brest
    {
        "titre": "Installation électrique à Brest : rénovation, mise aux normes et sécurité",
        "slug": "electricite-brest-renovation-normes",
        "categorie": "conseil",
        "image": "blog/installation-electrique-norme-nf-c-15-100.jpg",
        "resume": "Rénovation et mise aux normes de votre installation électrique à Brest. Tableau, câblage, sécurité : conseils d'expert par Performance Habitat, électricien en Finistère.",
        "meta_description": "Installation électrique à Brest : mise aux normes, rénovation et sécurité. Électricien qualifié Performance Habitat — Finistère. Devis gratuit.",
        "contenu": """
<h2>Installation électrique à Brest : quand et pourquoi rénover ?</h2>
<p>Une installation électrique vieillissante est à la fois un danger pour votre famille et une contrainte lors de la vente de votre bien. À <strong>Brest</strong> et dans le Finistère, <strong>Performance Habitat</strong> réalise des travaux d'électricité complets : diagnostic, mise aux normes, création de circuits, rénovation de tableau électrique.</p>

<h2>Les signes d'une installation électrique à risque</h2>
<ul>
  <li>Disjoncteurs qui sautent fréquemment</li>
  <li>Prises sans prise de terre (les anciennes prises à deux fiches rondes sans trou de terre)</li>
  <li>Tableau électrique avec fusibles à vis (avant les disjoncteurs)</li>
  <li>Fils apparents, gaines abîmées ou brûlées</li>
  <li>Odeur de brûlé près des prises ou interrupteurs</li>
  <li>Installation de plus de 25-30 ans sans diagnostic</li>
</ul>

<blockquote>En France, environ 30 % des incendies domestiques ont une cause électrique. Une installation conforme réduit drastiquement ce risque.</blockquote>

<h2>La norme NF C 15-100 à Brest</h2>
<p>La <strong>norme NF C 15-100</strong> est le référentiel français des installations électriques résidentielles. Obligatoire pour toute installation neuve ou entièrement rénovée, elle impose notamment :</p>
<ul>
  <li>Un tableau équipé d'un disjoncteur différentiel 30 mA</li>
  <li>Des circuits dédiés pour les gros électroménagers (four, lave-linge, lave-vaisselle)</li>
  <li>Un nombre minimal de prises par pièce (5 en salon, 3 en chambre)</li>
  <li>Des règles strictes en salle de bain (zones de sécurité 0, 1 et 2)</li>
  <li>Une mise à la terre de toute l'installation</li>
</ul>

<h2>Nos prestations d'électricité à Brest</h2>

<h3>Diagnostic électrique</h3>
<p>Avant tout travaux, nous réalisons un diagnostic complet de votre installation : état du tableau, présence de la mise à la terre, conformité des circuits, état des gaines et des fils. Ce diagnostic permet d'établir un devis précis et de prioriser les interventions.</p>

<h3>Remplacement du tableau électrique</h3>
<p>Un tableau électrique moderne, avec disjoncteurs différentiels et parafoudre, protège efficacement vos équipements et votre famille. Le remplacement d'un tableau complet à Brest est généralement réalisé en une journée.</p>

<h3>Création ou modification de circuits</h3>
<p>Ajout de prises, création d'un circuit dédié pour un équipement, déplacement d'interrupteurs — nous réalisons tous les travaux de second œuvre électrique à Brest et dans le Finistère.</p>

<h3>Électricité en salle de bain</h3>
<p>La salle de bain est la pièce la plus réglementée sur le plan électrique. Nos électriciens respectent scrupuleusement les zones de sécurité (0, 1 et 2) définies par la norme. Voir notre article sur la <a href="/blog/renovation-salle-de-bain-brest-guide/">rénovation salle de bain à Brest</a>.</p>

<h3>Remise du certificat de conformité (CONSUEL)</h3>
<p>À la fin des travaux, nous vous remettons le dossier CONSUEL si requis, attestant la conformité de votre installation aux normes en vigueur.</p>

<h2>Pourquoi confier vos travaux d'électricité à Performance Habitat à Brest ?</h2>
<ul>
  <li>Électriciens qualifiés, formés aux dernières normes en vigueur</li>
  <li>Intervention à Brest, Guilers, Plouzané, Le Relecq-Kerhuon, Bohars, Gouesnou et tout le Finistère</li>
  <li>Devis détaillé et transparent avant tout travaux</li>
  <li>Un seul interlocuteur pour l'électricité et tous vos autres travaux de rénovation</li>
</ul>

<p>Découvrez l'ensemble de nos <a href="/services/">services de rénovation</a> à Brest et en Finistère.</p>

<div style="background:rgba(196,255,14,0.08);border-left:4px solid #c4ff0e;padding:1.5rem;margin:2rem 0;border-radius:0 8px 8px 0;">
  <h3 style="color:#c4ff0e;margin-top:0;">Votre installation électrique à Brest</h3>
  <p>Contactez Performance Habitat pour un diagnostic ou un devis gratuit. Nous intervenons rapidement à Brest et dans tout le Finistère.</p>
  <p><a href="/#contact"><strong>→ Demander mon devis gratuit</strong></a> &nbsp;|&nbsp; <a href="tel:0650034777"><strong>☎ 06 50 03 47 77</strong></a></p>
</div>
""",
    },

    # ── ARTICLE 5 ── Pompe à chaleur Brest
    {
        "titre": "Pompe à chaleur à Brest et Finistère : installation, prix et économies 2025",
        "slug": "pompe-a-chaleur-brest-finistere",
        "categorie": "conseil",
        "image": "blog/renovation-energetique-economies-chauffage.jpg",
        "resume": "Installation de pompe à chaleur à Brest et en Finistère : types, prix, économies d'énergie et aides MaPrimeRénov' 2025. Performance Habitat, artisan local.",
        "meta_description": "Pompe à chaleur à Brest et Finistère : installation, prix 2025 et aides MaPrimeRénov'. Performance Habitat, artisan local. Devis gratuit.",
        "contenu": """
<h2>Pompe à chaleur à Brest : le chauffage économique et écologique</h2>
<p>La <strong>pompe à chaleur (PAC)</strong> est la solution de chauffage la plus efficiente en 2025. À Brest et dans tout le Finistère, le climat breton — doux et humide — est particulièrement favorable aux PAC air-air et air-eau. <strong>Performance Habitat</strong> installe et entretient des pompes à chaleur pour les particuliers à Brest, Guilers, Plouzané et dans tout le Finistère.</p>

<h2>Les types de pompes à chaleur disponibles à Brest</h2>

<h3>PAC air-air</h3>
<p>La pompe à chaleur air-air capte les calories dans l'air extérieur pour chauffer (et rafraîchir en été) votre logement via des unités intérieures. C'est la solution la plus économique à l'installation (4 000 € – 8 000 €) et la plus rapide à mettre en place.</p>

<h3>PAC air-eau</h3>
<p>La PAC air-eau alimente votre système de radiateurs ou de plancher chauffant existant. Elle peut également produire l'eau chaude sanitaire. Plus coûteuse à l'installation (8 000 € – 15 000 €), elle offre un meilleur confort thermique global et des économies plus importantes sur le long terme.</p>

<h3>PAC géothermique</h3>
<p>La PAC géothermique capte les calories dans le sol. Plus performante mais aussi plus chère à installer (15 000 € – 25 000 €), elle est adaptée aux grandes maisons avec terrain disponible.</p>

<h2>Pourquoi la pompe à chaleur est idéale à Brest ?</h2>
<p>Le climat brestois, avec ses températures douces (rarement inférieures à 0°C), est optimal pour les PAC air-air et air-eau. Ces équipements sont particulièrement efficaces entre 0°C et 15°C — exactement les températures hivernales habituelles à Brest.</p>

<blockquote>Une PAC air-eau bien dimensionnée à Brest peut réduire votre facture de chauffage de 40 à 60 % par rapport à un chauffage électrique classique.</blockquote>

<h2>Les aides financières pour une PAC à Brest en 2025</h2>

<h3>MaPrimeRénov'</h3>
<p>La principale aide de l'État pour l'installation d'une pompe à chaleur. Le montant varie selon vos revenus et le type de PAC :</p>
<ul>
  <li>PAC air-eau : jusqu'à 4 000 € pour les revenus modestes</li>
  <li>PAC géothermique : jusqu'à 10 000 €</li>
</ul>

<h3>Prime CEE (Certificats d'Économies d'Énergie)</h3>
<p>Les fournisseurs d'énergie financent une partie de l'installation via les CEE. Cette prime est cumulable avec MaPrimeRénov'.</p>

<h3>TVA à 5,5 %</h3>
<p>L'installation d'une PAC dans un logement de plus de 2 ans bénéficie du taux de TVA réduit à 5,5 % (au lieu de 20 %).</p>

<h3>Éco-PTZ</h3>
<p>Un prêt à taux zéro jusqu'à 50 000 € pour financer des travaux de rénovation énergétique, dont l'installation d'une PAC.</p>

<h2>Notre process d'installation à Brest</h2>
<ul>
  <li><strong>Étude de faisabilité</strong> : analyse de votre logement, calcul des besoins en chauffage, choix du modèle adapté</li>
  <li><strong>Montage du dossier d'aides</strong> : nous vous accompagnons dans vos démarches MaPrimeRénov'</li>
  <li><strong>Installation</strong> : pose de l'unité extérieure, installation des unités intérieures ou raccordement au circuit hydraulique</li>
  <li><strong>Mise en service et réglage</strong> : optimisation de la pompe à chaleur pour votre logement</li>
</ul>

<p>Découvrez aussi notre article sur la <a href="/blog/renovation-energetique-economies-chauffage/">rénovation énergétique et les économies de chauffage</a>.</p>

<div style="background:rgba(196,255,14,0.08);border-left:4px solid #c4ff0e;padding:1.5rem;margin:2rem 0;border-radius:0 8px 8px 0;">
  <h3 style="color:#c4ff0e;margin-top:0;">Votre projet pompe à chaleur à Brest</h3>
  <p>Performance Habitat vous propose une étude gratuite et sans engagement pour votre installation de pompe à chaleur à Brest, Guilers, Plouzané et dans tout le Finistère.</p>
  <p><a href="/#contact"><strong>→ Demander mon étude gratuite</strong></a> &nbsp;|&nbsp; <a href="tel:0650034777"><strong>☎ 06 50 03 47 77</strong></a></p>
</div>
""",
    },

    # ── ARTICLE 6 ── Carrelage salle de bain Brest
    {
        "titre": "Carrelage salle de bain à Brest : pose, tendances et conseils 2025",
        "slug": "carrelage-salle-de-bain-brest",
        "categorie": "conseil",
        "image": "blog/5-erreurs-renovation-salle-de-bain.jpg",
        "resume": "Tout savoir sur le carrelage salle de bain à Brest : choix des carreaux, pose professionnelle, tendances 2025. Artisan carreleur Performance Habitat en Finistère.",
        "meta_description": "Carrelage salle de bain à Brest : pose, choix et tendances 2025. Carreleur professionnel Performance Habitat — Finistère. Devis gratuit.",
        "contenu": """
<h2>Carrelage salle de bain à Brest : l'importance du bon choix</h2>
<p>Le carrelage est l'élément central de toute rénovation de salle de bain. À <strong>Brest</strong> et dans le Finistère, <strong>Performance Habitat</strong> réalise la pose de carrelage et faïence pour salle de bain, avec une expertise artisanale qui garantit un résultat durable et esthétique.</p>

<h2>Comment choisir son carrelage de salle de bain ?</h2>

<h3>La résistance à l'eau et à l'humidité</h3>
<p>En salle de bain, le carrelage doit obligatoirement présenter une absorption d'eau très faible (groupe BIa ou BIb selon la norme EN 14411). Les carreaux en grès cérame émaillé ou en grès cérame pleine masse sont les plus adaptés.</p>

<h3>L'antidérapance</h3>
<p>Pour le sol de la douche et de la salle de bain, choisissez un carrelage antidérapant classé au minimum <strong>R10</strong> (usage domestique humide) ou <strong>R11</strong> pour la zone de douche. Une surface glissante est un risque de chute, surtout pour les personnes âgées.</p>

<h3>Le format des carreaux</h3>
<ul>
  <li><strong>Petit format (10×10, 20×20 cm)</strong> : style vintage, idéal pour les petites salles de bain</li>
  <li><strong>Format moyen (30×60, 45×45 cm)</strong> : polyvalent, effet classique</li>
  <li><strong>Grand format (60×60, 60×120, 90×90 cm)</strong> : tendance 2025, agrandit visuellement l'espace et réduit les joints</li>
  <li><strong>Format rectangulaire en pose verticale</strong> : donne de la hauteur à la pièce</li>
</ul>

<h2>Les tendances carrelage salle de bain 2025 à Brest</h2>

<h3>L'effet béton ciré</h3>
<p>Le carrelage imitation béton ciré est la tendance numéro 1 en 2025. Discret, moderne et masculin, il s'associe parfaitement au bois et au métal noir. Disponible en grand format pour un effet maximal.</p>

<h3>Le carrelage marbre</h3>
<p>Le marbre de synthèse (grès cérame imitation marbre) offre un rendu luxueux à prix maîtrisé. Très prisé à Brest pour les salles de bain d'appartements haut de gamme.</p>

<h3>Le zellige et les carreaux de ciment</h3>
<p>Pour un style méditerranéen ou bohème, les carreaux de ciment colorés et le zellige font un retour en force. Idéaux en crédence ou en bandeau décoratif.</p>

<h3>Le large format uni</h3>
<p>Les dalles 120×120 cm en grès cérame blanc ou gris clair transforment une petite salle de bain en espace aérien et hôtelier.</p>

<h2>La pose de carrelage salle de bain par Performance Habitat</h2>

<h3>Préparation du support</h3>
<p>Un carrelage dure dans le temps seulement si le support est parfaitement préparé : planéité, absence d'humidité montante, étanchéité sous la douche. Nous préparons soigneusement chaque support avant toute pose.</p>

<h3>Pose avec colle adaptée</h3>
<p>Le choix de la colle est crucial : colle C2 pour les grands formats, joint désolidarisant pour les grandes surfaces, colle hydrofuge dans les zones humides. Nos carreleurs utilisent systématiquement les produits adaptés à chaque situation.</p>

<h3>Joints de qualité</h3>
<p>Les joints sont la partie la plus fragile d'un carrelage. Nous utilisons des joints époxy dans les zones de douche (résistance aux moisissures et aux produits ménagers) et des joints ciment de qualité professionnelle dans les autres zones.</p>

<blockquote>Un carrelage mal posé, c'est des carreaux qui se décollent en 2 ans. Un carrelage bien posé par un professionnel, c'est 20 ans de tranquillité.</blockquote>

<p>Retrouvez nos réalisations de <a href="/realisations/">carrelage salle de bain à Brest et en Finistère</a>.</p>

<div style="background:rgba(196,255,14,0.08);border-left:4px solid #c4ff0e;padding:1.5rem;margin:2rem 0;border-radius:0 8px 8px 0;">
  <h3 style="color:#c4ff0e;margin-top:0;">Pose de carrelage à Brest et en Finistère</h3>
  <p>Contactez Performance Habitat pour un devis de pose de carrelage. Nous intervenons à Brest, Guilers, Plouzané, Le Relecq-Kerhuon et dans tout le Finistère.</p>
  <p><a href="/#contact"><strong>→ Demander mon devis gratuit</strong></a> &nbsp;|&nbsp; <a href="tel:0650034777"><strong>☎ 06 50 03 47 77</strong></a></p>
</div>
""",
    },

    # ── ARTICLE 7 ── Artisan rénovation Plouzané
    {
        "titre": "Artisan rénovation à Plouzané : salle de bain, électricité et carrelage",
        "slug": "artisan-renovation-plouzane",
        "categorie": "conseil",
        "image": "blog/renovation-salle-de-bain-brest-realisation.jpg",
        "resume": "Votre artisan rénovation à Plouzané : salle de bain, électricité, carrelage et plomberie. Performance Habitat intervient à Plouzané et dans tout le Finistère.",
        "meta_description": "Artisan rénovation à Plouzané : salle de bain, électricité, carrelage. Performance Habitat, votre expert local en Finistère. Devis gratuit.",
        "contenu": """
<h2>Votre artisan rénovation à Plouzané</h2>
<p>Vous habitez à <strong>Plouzané</strong> et vous cherchez un artisan de confiance pour vos travaux de rénovation ? <strong>Performance Habitat</strong>, basé à Guilers à quelques minutes de Plouzané, intervient régulièrement dans votre commune pour tous types de travaux : rénovation de salle de bain, installation électrique, carrelage, plomberie et chauffage.</p>

<h2>Nos services à Plouzané</h2>

<h3>Rénovation salle de bain à Plouzané</h3>
<p>La rénovation de salle de bain est notre spécialité. À Plouzané, nous réalisons des projets complets ou partiels : remplacement de la baignoire par une douche à l'italienne, pose de carrelage grand format, installation d'un meuble vasque suspendu, mise aux normes de la plomberie et de l'électricité.</p>
<p>En savoir plus sur notre <a href="/blog/renovation-salle-de-bain-brest-guide/">guide complet de rénovation salle de bain</a>.</p>

<h3>Électricité à Plouzané</h3>
<p>Tableau électrique vétuste, prises sans terre, installation non conforme à la norme NF C 15-100 — nos électriciens qualifiés réalisent le diagnostic et la mise aux normes de votre installation à Plouzané. En savoir plus sur notre <a href="/blog/electricite-brest-renovation-normes/">service d'installation électrique</a>.</p>

<h3>Carrelage et faïence à Plouzané</h3>
<p>Pose de carrelage sol et mur, faïence salle de bain, terrasse ou cuisine : notre carreleur intervient à Plouzané avec les matériaux de votre choix. Découvrez nos conseils sur le <a href="/blog/carrelage-salle-de-bain-brest/">carrelage de salle de bain</a>.</p>

<h3>Plomberie à Plouzané</h3>
<p>Fuite d'eau, remplacement de chauffe-eau, canalisation bouchée ou rénovation complète de la plomberie — Performance Habitat intervient à Plouzané pour toutes vos urgences et projets de plomberie.</p>

<h3>Chauffage et pompe à chaleur à Plouzané</h3>
<p>Installation ou remplacement de votre système de chauffage : radiateurs, plancher chauffant, pompe à chaleur air-air ou air-eau. Performance Habitat vous aide à choisir la solution la plus adaptée à votre logement à Plouzané. En savoir plus sur notre <a href="/blog/pompe-a-chaleur-brest-finistere/">service pompe à chaleur</a>.</p>

<h2>Pourquoi choisir Performance Habitat à Plouzané ?</h2>

<h3>Un artisan local, à deux pas de chez vous</h3>
<p>Basés à Guilers, nous intervenons régulièrement à Plouzané. Notre proximité garantit des délais d'intervention courts et une réactivité que ne peuvent pas offrir les grandes entreprises éloignées.</p>

<h3>Un seul interlocuteur pour tous vos travaux</h3>
<p>Plomberie, électricité, carrelage, peinture : Performance Habitat est une équipe pluridisciplinaire. Vous avez un seul contact pour l'ensemble de votre projet de rénovation à Plouzané — un gain de temps et de tranquillité considérable.</p>

<h3>Devis gratuit et transparence totale</h3>
<p>Nous nous déplaçons gratuitement chez vous à Plouzané pour établir un devis détaillé. Pas de frais cachés, pas de mauvaise surprise en cours de chantier.</p>

<blockquote>Votre satisfaction est notre priorité. Chaque chantier à Plouzané est réalisé dans les règles de l'art et dans les délais convenus.</blockquote>

<p>Consultez également nos <a href="/realisations/">réalisations récentes</a> pour découvrir la qualité de notre travail.</p>

<div style="background:rgba(196,255,14,0.08);border-left:4px solid #c4ff0e;padding:1.5rem;margin:2rem 0;border-radius:0 8px 8px 0;">
  <h3 style="color:#c4ff0e;margin-top:0;">Votre projet de rénovation à Plouzané</h3>
  <p>Contactez Performance Habitat pour discuter de votre projet à Plouzané. Devis gratuit, déplacement offert.</p>
  <p><a href="/#contact"><strong>→ Demander mon devis gratuit</strong></a> &nbsp;|&nbsp; <a href="tel:0650034777"><strong>☎ 06 50 03 47 77</strong></a></p>
</div>
""",
    },

    # ── ARTICLE 8 ── Rénovation Le Relecq-Kerhuon
    {
        "titre": "Artisan rénovation au Relecq-Kerhuon : salle de bain et travaux",
        "slug": "renovation-appartement-relecq-kerhuon",
        "categorie": "conseil",
        "image": "blog/renovation-salle-de-bain-brest-realisation.jpg",
        "resume": "Artisan rénovation au Relecq-Kerhuon : salle de bain, plomberie, électricité et carrelage. Performance Habitat, votre expert local en Finistère.",
        "meta_description": "Artisan rénovation au Relecq-Kerhuon : salle de bain, électricité, carrelage. Performance Habitat, expert Finistère. Devis gratuit ☎ 06 50 03 47 77",
        "contenu": """
<h2>Votre artisan rénovation au Relecq-Kerhuon</h2>
<p>Vous habitez au <strong>Relecq-Kerhuon</strong> (communément appelé Le Relecq-Kerhuon ou Le Relec) et vous cherchez un artisan qualifié pour vos travaux de rénovation ? <strong>Performance Habitat</strong>, installé à Guilers, est votre partenaire de proximité pour tous vos projets au Relecq-Kerhuon : rénovation de salle de bain, mise aux normes électrique, carrelage, plomberie et chauffage.</p>

<h2>Nos interventions au Relecq-Kerhuon</h2>

<h3>Rénovation salle de bain au Relecq-Kerhuon</h3>
<p>Que vous habitiez dans un appartement ou une maison au Relecq-Kerhuon, nos artisans rénovent votre salle de bain de A à Z. Dépose de l'ancienne installation, travaux de plomberie et d'électricité, pose du carrelage, installation des équipements (douche à l'italienne, meuble vasque, radiateur sèche-serviettes) — tout est géré par notre équipe.</p>

<h3>Douche à l'italienne au Relecq-Kerhuon</h3>
<p>La <a href="/blog/douche-italienne-brest/">douche à l'italienne</a> est la transformation la plus demandée au Relecq-Kerhuon. Idéale pour moderniser une salle de bain d'appartement, elle offre un gain d'espace visuel important et facilite l'entretien au quotidien.</p>

<h3>Électricité au Relecq-Kerhuon</h3>
<p>Nos électriciens qualifiés réalisent la mise aux normes de votre installation électrique au Relecq-Kerhuon : remplacement du tableau, création de circuits, mise à la terre. Voir notre article sur l'<a href="/blog/electricite-brest-renovation-normes/">installation électrique à Brest et en Finistère</a>.</p>

<h3>Plomberie au Relecq-Kerhuon</h3>
<p>Fuite, canalisation bouchée, remplacement de chauffe-eau ou rénovation complète de la plomberie : nos plombiers interviennent rapidement au Relecq-Kerhuon pour toutes vos urgences et projets.</p>

<h2>Rénovation d'appartement au Relecq-Kerhuon</h2>
<p>Le Relecq-Kerhuon est une commune très résidentielle de la métropole brestoise, avec de nombreux appartements des années 70-80 dont les salles de bain et installations méritent d'être rénovées. Performance Habitat est spécialisé dans ce type de rénovation d'appartement : nous savons travailler dans des espaces réduits, en minimisant les nuisances pour les voisins et en respectant les règles de copropriété.</p>

<blockquote>Rénovation d'appartement ou de maison, grand projet ou petit chantier : nous intervenons au Relecq-Kerhuon avec le même soin et la même rigueur.</blockquote>

<h2>Délais et organisation au Relecq-Kerhuon</h2>
<p>Notre proximité (Guilers est à 10 minutes du Relecq-Kerhuon) nous permet d'intervenir rapidement. Pour une rénovation complète de salle de bain, comptez généralement 8 à 14 jours ouvrés selon la surface et les travaux.</p>

<p>Consultez nos <a href="/realisations/">réalisations</a> pour voir des exemples de projets similaires dans la région brestoise.</p>

<div style="background:rgba(196,255,14,0.08);border-left:4px solid #c4ff0e;padding:1.5rem;margin:2rem 0;border-radius:0 8px 8px 0;">
  <h3 style="color:#c4ff0e;margin-top:0;">Votre projet au Relecq-Kerhuon</h3>
  <p>Contactez Performance Habitat pour un devis gratuit et sans engagement. Nous nous déplaçons au Relecq-Kerhuon et dans tout le Finistère.</p>
  <p><a href="/#contact"><strong>→ Demander mon devis gratuit</strong></a> &nbsp;|&nbsp; <a href="tel:0650034777"><strong>☎ 06 50 03 47 77</strong></a></p>
</div>
""",
    },

    # ── ARTICLE 9 ── Rénovation maison Finistère
    {
        "titre": "Rénovation maison en Finistère : votre artisan local Performance Habitat",
        "slug": "renovation-maison-finistere",
        "categorie": "conseil",
        "image": "blog/renovation-energetique-economies-chauffage.jpg",
        "resume": "Rénovation complète de maison en Finistère : salle de bain, électricité, plomberie, chauffage et carrelage. Performance Habitat, artisan local à Guilers.",
        "meta_description": "Rénovation maison en Finistère : salle de bain, électricité, plomberie. Performance Habitat, artisan local basé à Guilers. Devis gratuit.",
        "contenu": """
<h2>Rénover votre maison en Finistère avec Performance Habitat</h2>
<p>Propriétaire d'une maison en <strong>Finistère</strong> et vous souhaitez la rénover ? <strong>Performance Habitat</strong>, artisan local basé à Guilers depuis 2013, vous accompagne dans tous vos projets de rénovation à Brest, Guilers, Plouzané, Le Relecq-Kerhuon, Bohars, Gouesnou, Lannilis, Plabennec et dans tout le Finistère.</p>

<h2>Nos domaines d'expertise en rénovation de maison</h2>

<h3>Rénovation salle de bain</h3>
<p>La salle de bain est souvent le premier chantier lors d'une rénovation de maison. Performance Habitat réalise des rénovations complètes : dépose de l'ancien, plomberie, électricité, carrelage, équipements. Découvrez notre <a href="/blog/renovation-salle-de-bain-brest-guide/">guide complet de rénovation salle de bain en Finistère</a>.</p>

<h3>Installation et rénovation électrique</h3>
<p>Les maisons bretonnes des années 60, 70 et 80 ont souvent des installations électriques vieillissantes et non conformes. Nos électriciens qualifiés réalisent le diagnostic et la mise aux normes complète. En savoir plus sur notre <a href="/blog/electricite-brest-renovation-normes/">service d'électricité en Finistère</a>.</p>

<h3>Plomberie et sanitaires</h3>
<p>Remplacement de canalisations, installation d'un nouveau chauffe-eau, rénovation de salle de bain — nos plombiers interviennent dans tout le Finistère avec réactivité et professionnalisme.</p>

<h3>Chauffage et pompe à chaleur</h3>
<p>Installation d'une pompe à chaleur air-eau ou air-air, remplacement d'une chaudière, pose d'un plancher chauffant — Performance Habitat vous aide à choisir la solution la plus adaptée à votre maison en Finistère. Voir notre article sur la <a href="/blog/pompe-a-chaleur-brest-finistere/">pompe à chaleur en Finistère</a>.</p>

<h3>Carrelage et sols</h3>
<p>Pose de carrelage en salle de bain, cuisine, couloir ou terrasse — notre carreleur réalise des poses soignées sur tout le Finistère. Découvrez nos conseils sur le <a href="/blog/carrelage-salle-de-bain-brest/">carrelage de salle de bain</a>.</p>

<h3>Peinture</h3>
<p>Peinture intérieure, lessivage des murs, plafonds — nos peintres donnent un coup de neuf à vos pièces en respectant votre palette de couleurs et votre budget.</p>

<h2>Zone d'intervention en Finistère</h2>
<p>Performance Habitat intervient dans toute la zone de Brest et ses environs :</p>
<ul>
  <li>Brest (29200, 29000)</li>
  <li>Guilers (29820) — notre base</li>
  <li>Plouzané (29280)</li>
  <li>Le Relecq-Kerhuon (29480)</li>
  <li>Bohars (29820)</li>
  <li>Gouesnou (29850)</li>
  <li>Plabennec (29860)</li>
  <li>Lannilis (29870)</li>
  <li>Et plus largement dans tout le Finistère (29)</li>
</ul>

<h2>Pourquoi choisir un artisan local en Finistère ?</h2>
<p>Faire appel à un artisan local comme Performance Habitat, c'est choisir la réactivité, la transparence et un engagement fort envers la qualité. Nous connaissons le bâti breton, ses contraintes (humidité, granit, isolation des maisons d'avant 1975) et nous adaptons nos solutions en conséquence.</p>

<blockquote>Aucune sous-traitance : tous nos travaux sont réalisés par notre propre équipe. Vous savez toujours qui intervient chez vous.</blockquote>

<div style="background:rgba(196,255,14,0.08);border-left:4px solid #c4ff0e;padding:1.5rem;margin:2rem 0;border-radius:0 8px 8px 0;">
  <h3 style="color:#c4ff0e;margin-top:0;">Votre projet de rénovation en Finistère</h3>
  <p>Contactez Performance Habitat pour un devis gratuit. Nous vous rencontrons chez vous pour évaluer vos besoins et vous proposer une solution adaptée à votre budget.</p>
  <p><a href="/#contact"><strong>→ Demander mon devis gratuit</strong></a> &nbsp;|&nbsp; <a href="tel:0650034777"><strong>☎ 06 50 03 47 77</strong></a></p>
</div>
""",
    },

    # ── ARTICLE 10 ── Artisan rénovation Guilers (remplace cuisine ouverte)
    {
        "titre": "Artisan rénovation à Guilers : salle de bain, plomberie et électricité",
        "slug": "artisan-renovation-guilers",
        "categorie": "conseil",
        "image": "blog/renovation-salle-de-bain-brest-realisation.jpg",
        "resume": "Performance Habitat, artisan rénovation basé à Guilers depuis 2013. Salle de bain, plomberie, électricité, carrelage — votre expert local en Finistère.",
        "meta_description": "Artisan rénovation à Guilers : salle de bain, plomberie, électricité. Performance Habitat, basé à Guilers depuis 2013. Devis gratuit ☎ 06 50 03 47 77",
        "contenu": """
<h2>Performance Habitat : votre artisan rénovation à Guilers</h2>
<p><strong>Performance Habitat</strong> est une entreprise artisanale de rénovation basée à <strong>Guilers</strong> (Lieu-dit Penfeld, 29820), à deux pas de Brest. Depuis 2013, nous intervenons à Guilers et dans tout le Finistère pour des travaux de rénovation de salle de bain, plomberie, électricité, carrelage, chauffage et peinture.</p>

<h2>Pourquoi Guilers est notre zone d'excellence</h2>
<p>Basés à Guilers depuis notre création, nous connaissons parfaitement le tissu résidentiel local : maisons individuelles des années 70-80, lotissements plus récents, appartements en centre-bourg. Cette connaissance du terrain nous permet d'intervenir efficacement et de conseiller nos clients guilerois avec précision.</p>

<h2>Nos services à Guilers</h2>

<h3>Rénovation salle de bain à Guilers</h3>
<p>Notre spécialité principale. À Guilers, nous rénovons des salles de bain de toutes tailles : petites salles d'eau d'appartement, grandes salles de bain de maison individuelle. Chaque projet est unique — nous l'abordons avec la même rigueur.</p>
<ul>
  <li>Remplacement baignoire → douche à l'italienne</li>
  <li>Nouveau carrelage sol et mur</li>
  <li>Meuble vasque suspendu et miroir LED</li>
  <li>Radiateur sèche-serviettes</li>
  <li>Mise aux normes plomberie et électricité</li>
</ul>
<p>Découvrez notre <a href="/blog/renovation-salle-de-bain-brest-guide/">guide complet de rénovation salle de bain</a>.</p>

<h3>Plomberie à Guilers</h3>
<p>Intervention rapide pour toutes urgences plomberie à Guilers : fuite d'eau, canalisation bouchée, chauffe-eau en panne. Nous réalisons aussi les rénovations complètes de plomberie.</p>

<h3>Électricité à Guilers</h3>
<p>Mise aux normes NF C 15-100, remplacement de tableau électrique, création de circuits — nos électriciens qualifiés interviennent à Guilers pour toute demande. Voir notre article sur l'<a href="/blog/electricite-brest-renovation-normes/">installation électrique en Finistère</a>.</p>

<h3>Carrelage à Guilers</h3>
<p>Pose de carrelage salle de bain, salon, cuisine ou terrasse à Guilers. Nos carreleurs maîtrisent les grands formats, les motifs complexes et les matériaux exigeants.</p>

<h3>Pompe à chaleur à Guilers</h3>
<p>Installation de PAC air-air ou air-eau à Guilers — nous vous conseillons sur le meilleur équipement pour votre logement et vous accompagnons dans vos démarches MaPrimeRénov'. En savoir plus sur la <a href="/blog/pompe-a-chaleur-brest-finistere/">pompe à chaleur en Finistère</a>.</p>

<h2>Un artisan local, une équipe engagée</h2>
<p>Performance Habitat, c'est une équipe pluridisciplinaire qui partage les mêmes valeurs : qualité d'exécution, respect des délais, transparence avec le client. <strong>Aucune sous-traitance</strong> — tous nos travaux sont réalisés par nos propres artisans.</p>

<blockquote>Notre adresse à Guilers, c'est aussi notre engagement : nous sommes ici, nous connaissons vos voisins, nous avons rénové dans votre rue. Votre satisfaction est notre meilleure publicité.</blockquote>

<p>Consultez nos <a href="/realisations/">réalisations récentes</a> à Guilers et dans la région brestoise.</p>

<div style="background:rgba(196,255,14,0.08);border-left:4px solid #c4ff0e;padding:1.5rem;margin:2rem 0;border-radius:0 8px 8px 0;">
  <h3 style="color:#c4ff0e;margin-top:0;">Votre projet de rénovation à Guilers</h3>
  <p>Contactez-nous pour un devis gratuit. Nous nous déplaçons chez vous à Guilers et dans tout le Finistère sans frais.</p>
  <p><a href="/#contact"><strong>→ Demander mon devis gratuit</strong></a> &nbsp;|&nbsp; <a href="tel:0650034777"><strong>☎ 06 50 03 47 77</strong></a></p>
</div>
""",
    },

    # ── EXISTING ARTICLES UPDATED ── (update_or_create will update them)
    {
        "titre": "5 erreurs à éviter lors de la rénovation de votre salle de bain",
        "slug": "5-erreurs-renovation-salle-de-bain",
        "categorie": "conseil",
        "image": "blog/5-erreurs-renovation-salle-de-bain.jpg",
        "resume": "Rénover sa salle de bain à Brest ou en Finistère réserve des pièges. Découvrez les 5 erreurs les plus coûteuses — et comment les éviter avec les conseils de Performance Habitat.",
        "meta_description": "5 erreurs coûteuses en rénovation salle de bain à Brest. Conseils d'expert de Performance Habitat, artisan en Finistère. Devis gratuit.",
        "contenu": """
<h2>1. Négliger la ventilation</h2>
<p>À <strong>Brest</strong> et dans le Finistère, l'humidité est un enjeu particulièrement important. Une salle de bain mal ventilée est un nid à moisissures. Beaucoup de propriétaires oublient d'installer ou de remplacer la VMC (Ventilation Mécanique Contrôlée), pensant que c'est un détail. C'est pourtant l'une des erreurs les plus coûteuses à corriger après coup.</p>
<blockquote>Un taux d'humidité élevé en salle de bain peut réduire la durée de vie de votre carrelage et de vos joints de moitié — encore plus en Bretagne où l'air est naturellement chargé en humidité.</blockquote>

<h2>2. Sous-estimer le budget</h2>
<p>La rénovation d'une salle de bain à Brest réserve souvent des surprises : canalisations à remplacer, sol à reprendre, isolation à renforcer. Prévoyez toujours une <strong>marge de 15 à 20 %</strong> sur votre budget initial. Consultez notre <a href="/blog/renovation-salle-de-bain-brest-guide/">guide des prix de rénovation salle de bain à Brest</a> pour avoir une idée précise des fourchettes.</p>

<h2>3. Choisir le mauvais carrelage</h2>
<p>Tous les carreaux ne se valent pas. Un carrelage non adapté à une zone humide (indice de résistance à l'abrasion insuffisant, mauvaise tenue à l'eau) peut se fissurer en quelques mois. En salle de bain, exigez un carrelage groupe BIa/BIb et antidérapant (R10 minimum pour la douche). Voir nos <a href="/blog/carrelage-salle-de-bain-brest/">conseils sur le carrelage salle de bain</a>.</p>

<h2>4. Ignorer les normes électriques</h2>
<p>En salle de bain, des zones de sécurité strictes (zones 0, 1 et 2) définissent quels équipements peuvent être installés et où. Une prise mal positionnée peut être dangereuse et vous coûter une mise en conformité lors de la revente. Nos électriciens respectent scrupuleusement ces normes. Voir notre article sur l'<a href="/blog/electricite-brest-renovation-normes/">électricité en salle de bain à Brest</a>.</p>

<h2>5. Vouloir tout faire soi-même</h2>
<p>Les tutoriels donnent parfois l'illusion que la plomberie ou l'électricité sont à la portée de tous. En réalité, une mauvaise installation peut entraîner des dégâts des eaux, des risques d'électrocution et l'invalidation de votre assurance habitation. À Brest et en Finistère, faire appel à un artisan qualifié comme Performance Habitat est un investissement qui protège votre famille et votre patrimoine.</p>

<div style="background:rgba(196,255,14,0.08);border-left:4px solid #c4ff0e;padding:1.5rem;margin:2rem 0;border-radius:0 8px 8px 0;">
  <h3 style="color:#c4ff0e;margin-top:0;">Évitez ces erreurs avec Performance Habitat</h3>
  <p>Notre équipe réalise votre rénovation de salle de bain à Brest et en Finistère dans les règles de l'art. Devis gratuit, déplacement offert.</p>
  <p><a href="/#contact"><strong>→ Demander mon devis gratuit</strong></a> &nbsp;|&nbsp; <a href="tel:0650034777"><strong>☎ 06 50 03 47 77</strong></a></p>
</div>
""",
    },
    {
        "titre": "Rénovation complète d'une salle de bain à Brest : notre réalisation",
        "slug": "renovation-salle-de-bain-brest-realisation",
        "categorie": "realisation",
        "image": "blog/renovation-salle-de-bain-brest-realisation.jpg",
        "resume": "Transformation totale d'une salle de bain vieillissante à Brest : douche à l'italienne, carrelage grand format, meuble suspendu. Résultat et détails du chantier.",
        "meta_description": "Réalisation rénovation salle de bain à Brest : douche italienne, carrelage grand format, meuble suspendu. Performance Habitat, artisan Finistère.",
        "contenu": """
<h2>Le projet : une salle de bain des années 90 transformée à Brest</h2>
<p>Nos clients, un couple installé à <strong>Brest</strong> depuis 15 ans, souhaitaient transformer leur salle de bain datant des années 90 en un espace contemporain, lumineux et pratique. Budget : 8 500 € — Durée des travaux : 12 jours ouvrés.</p>

<h2>Ce qui a été réalisé</h2>
<ul>
  <li>Dépose complète de l'ancienne installation (baignoire, carrelage, cloisons)</li>
  <li>Mise aux normes de la plomberie et de l'électricité (zones de sécurité salle de bain)</li>
  <li>Pose d'une <a href="/blog/douche-italienne-brest/">douche à l'italienne</a> (90×120 cm) avec paroi en verre trempé</li>
  <li>Carrelage grand format 60×60 cm effet béton ciré</li>
  <li>Installation d'un meuble vasque suspendu double vasque</li>
  <li>Miroir LED avec anti-buée intégré</li>
  <li>Radiateur sèche-serviettes électrique</li>
  <li>Peinture des murs en teinte minérale douce</li>
</ul>

<h2>Les défis techniques</h2>
<p>L'ancienne baignoire avait laissé des traces d'humidité sur le mur porteur. Nous avons traité le problème à la source : application d'une résine hydrofuge sur le mur, pose d'un système d'étanchéité complet sous la douche. Ce type de surprise est fréquent dans les logements brestois des années 80-90 — notre expérience locale nous permet d'y faire face sans impact sur le délai global.</p>

<h2>Le résultat</h2>
<p>Un espace de 6 m² qui semble deux fois plus grand grâce au carrelage clair et aux miroirs. Nos clients sont ravis : <em>« On ne reconnaît plus notre salle de bain, c'est comme être dans un hôtel 4 étoiles ! »</em></p>

<blockquote>Chaque réalisation est unique. Nous adaptons nos solutions à votre espace, vos goûts et votre budget — à Brest comme dans tout le Finistère.</blockquote>

<h2>Inspiré par ce projet ?</h2>
<p>Consultez nos <a href="/realisations/">autres réalisations</a> et découvrez notre <a href="/blog/renovation-salle-de-bain-brest-guide/">guide complet de rénovation salle de bain à Brest</a> pour estimer votre budget et préparer votre projet.</p>

<div style="background:rgba(196,255,14,0.08);border-left:4px solid #c4ff0e;padding:1.5rem;margin:2rem 0;border-radius:0 8px 8px 0;">
  <h3 style="color:#c4ff0e;margin-top:0;">Vous avez un projet similaire à Brest ?</h3>
  <p>Contactez Performance Habitat pour un devis gratuit. Nous nous déplaçons sur Brest, Guilers, Plouzané, Le Relecq-Kerhuon et dans tout le Finistère.</p>
  <p><a href="/#contact"><strong>→ Demander mon devis gratuit</strong></a> &nbsp;|&nbsp; <a href="tel:0650034777"><strong>☎ 06 50 03 47 77</strong></a></p>
</div>
""",
    },
    {
        "titre": "Quand faut-il changer sa plomberie à Brest ? Les signes qui ne trompent pas",
        "slug": "quand-changer-plomberie-signes",
        "categorie": "conseil",
        "image": "blog/quand-changer-plomberie-signes.jpg",
        "resume": "Eau colorée, pression en baisse, fuites récurrentes… Ces signes indiquent que votre plomberie arrive en fin de vie à Brest ou en Finistère. Performance Habitat fait le point.",
        "meta_description": "Quand changer sa plomberie à Brest ? Signes d'alerte et conseils de Performance Habitat, plombier en Finistère. Diagnostic gratuit.",
        "contenu": """
<h2>L'âge des canalisations à Brest et en Finistère</h2>
<p>De nombreuses maisons et appartements à <strong>Brest</strong> et dans le Finistère datent des années 60 à 80 et n'ont jamais eu leur plomberie rénovée. La durée de vie des canalisations varie selon le matériau : les tuyaux en plomb (toujours présents dans certaines maisons anciennes brestoises) doivent être remplacés d'urgence, les tuyaux en acier galvanisé ont une durée de vie de 40 à 70 ans, et le cuivre peut tenir 50 à 80 ans en bonne condition.</p>

<h2>Les 5 signes qui indiquent un changement nécessaire</h2>
<ul>
  <li><strong>Eau colorée ou rouillée</strong> : signe de corrosion interne des canalisations.</li>
  <li><strong>Chute de pression</strong> : peut indiquer des fuites cachées ou un dépôt calcaire important.</li>
  <li><strong>Bruit de canalisations</strong> : sifflements, claquements révèlent une usure avancée.</li>
  <li><strong>Fuites récurrentes</strong> : si vous réparez souvent les mêmes endroits, le réseau est fatigué.</li>
  <li><strong>Taches d'humidité</strong> : sur les murs ou plafonds, même sans fuite visible.</li>
</ul>

<blockquote>Un dégât des eaux non détecté peut causer jusqu'à 30 000 € de dommages. À Brest, où les hivers humides sollicitent davantage les installations, mieux vaut prévenir que guérir.</blockquote>

<h2>Plomberie et rénovation salle de bain : l'opportunité à saisir</h2>
<p>Si votre plomberie doit être rénovée, c'est souvent l'occasion idéale de rénover également votre salle de bain. Les travaux de plomberie nécessitent d'ouvrir les murs — autant en profiter pour moderniser l'ensemble. Consultez notre <a href="/blog/renovation-salle-de-bain-brest-guide/">guide de rénovation salle de bain à Brest</a> pour évaluer votre projet.</p>

<h2>Notre intervention plomberie à Brest et en Finistère</h2>
<p>Performance Habitat réalise des diagnostics de plomberie complets à Brest, Guilers, Plouzané, Le Relecq-Kerhuon et dans tout le Finistère. Nous évaluons l'état de vos canalisations et vous proposons les travaux strictement nécessaires — pas plus.</p>

<div style="background:rgba(196,255,14,0.08);border-left:4px solid #c4ff0e;padding:1.5rem;margin:2rem 0;border-radius:0 8px 8px 0;">
  <h3 style="color:#c4ff0e;margin-top:0;">Diagnostic plomberie gratuit à Brest</h3>
  <p>Vous avez un doute sur l'état de votre plomberie ? Contactez Performance Habitat pour un diagnostic gratuit à Brest et dans tout le Finistère.</p>
  <p><a href="/#contact"><strong>→ Demander mon diagnostic gratuit</strong></a> &nbsp;|&nbsp; <a href="tel:0650034777"><strong>☎ 06 50 03 47 77</strong></a></p>
</div>
""",
    },
    {
        "titre": "Rénovation énergétique en Finistère : économisez jusqu'à 40 % sur votre chauffage",
        "slug": "renovation-energetique-economies-chauffage",
        "categorie": "actualite",
        "image": "blog/renovation-energetique-economies-chauffage.jpg",
        "resume": "Rénovation énergétique à Brest et en Finistère : pompe à chaleur, aides MaPrimeRénov' et économies possibles. Guide complet par Performance Habitat.",
        "meta_description": "Rénovation énergétique à Brest et Finistère : aides 2025 et économies sur le chauffage. Guide complet par Performance Habitat, artisan local.",
        "contenu": """
<h2>Rénovation énergétique à Brest et en Finistère</h2>
<p>Face à la hausse des prix de l'énergie, la rénovation thermique est devenue une priorité pour de nombreux propriétaires bretons. À <strong>Brest</strong> et dans le <strong>Finistère</strong>, un logement classé F ou G peut voir sa facture de chauffage divisée par deux ou trois après travaux bien ciblés.</p>

<h2>Les travaux de rénovation énergétique les plus efficaces</h2>

<h3>La pompe à chaleur</h3>
<p>La PAC est la solution de chauffage la plus efficiente en Bretagne. Le climat brestois, doux et humide, est idéal pour les <a href="/blog/pompe-a-chaleur-brest-finistere/">pompes à chaleur air-air et air-eau</a>. Performance Habitat installe des PAC à Brest, Guilers, Plouzané et dans tout le Finistère.</p>

<h3>L'isolation thermique</h3>
<p>L'isolation des combles (jusqu'à 30 % d'économies) et des murs est le premier levier à activer. En Bretagne, l'isolation par l'extérieur (ITE) est particulièrement adaptée aux maisons en granit.</p>

<h3>Le remplacement du système de chauffage</h3>
<p>Chaudière à condensation, chaudière à granulés, pompe à chaleur — remplacer un système de chauffage vétuste est souvent le geste le plus rentable en termes d'économies d'énergie.</p>

<h2>Les aides disponibles en 2025</h2>
<ul>
  <li><strong>MaPrimeRénov'</strong> : jusqu'à 20 000 € selon vos revenus et les travaux</li>
  <li><strong>Éco-PTZ</strong> : prêt à taux zéro jusqu'à 50 000 €</li>
  <li><strong>TVA à 5,5 %</strong> sur les travaux de rénovation énergétique</li>
  <li><strong>CEE (Certificats d'Économies d'Énergie)</strong> : primes versées par les fournisseurs d'énergie</li>
  <li><strong>MaPrimeAdapt'</strong> : pour les adaptations liées à l'accessibilité PMR</li>
</ul>

<blockquote>Avec le cumul des aides, certains ménages modestes en Finistère peuvent bénéficier d'une rénovation énergétique à très faible reste à charge.</blockquote>

<h2>Performance Habitat vous accompagne</h2>
<p>Performance Habitat vous aide à identifier les travaux prioritaires, à monter votre dossier d'aides et réalise l'ensemble des travaux. Un seul interlocuteur pour toute votre rénovation énergétique à Brest et en Finistère.</p>

<div style="background:rgba(196,255,14,0.08);border-left:4px solid #c4ff0e;padding:1.5rem;margin:2rem 0;border-radius:0 8px 8px 0;">
  <h3 style="color:#c4ff0e;margin-top:0;">Bilan énergétique gratuit à Brest</h3>
  <p>Contactez Performance Habitat pour un bilan énergétique gratuit et découvrez les aides auxquelles vous avez droit en Finistère.</p>
  <p><a href="/#contact"><strong>→ Demander mon bilan gratuit</strong></a> &nbsp;|&nbsp; <a href="tel:0650034777"><strong>☎ 06 50 03 47 77</strong></a></p>
</div>
""",
    },
    {
        "titre": "Installation électrique aux normes NF C 15-100 à Brest : pourquoi c'est crucial",
        "slug": "installation-electrique-norme-nf-c-15-100",
        "categorie": "conseil",
        "image": "blog/installation-electrique-norme-nf-c-15-100.jpg",
        "resume": "La norme NF C 15-100 est obligatoire pour toute installation électrique rénovée à Brest. Performance Habitat vous explique ses exigences et pourquoi c'est vital.",
        "meta_description": "Norme NF C 15-100 à Brest : installation électrique conforme et sécurisée. Electricien qualifié Performance Habitat en Finistère. Devis gratuit.",
        "contenu": """
<h2>La norme NF C 15-100 à Brest : l'essentiel à savoir</h2>
<p>La <strong>norme NF C 15-100</strong> est le référentiel français qui définit les règles de conception et de réalisation des installations électriques dans les habitations. À <strong>Brest</strong> et en Finistère, de nombreux logements des années 60 à 80 présentent des installations non conformes — un risque réel pour vos occupants.</p>

<h2>Ce que la norme impose</h2>
<ul>
  <li>Un tableau électrique avec disjoncteur différentiel 30 mA</li>
  <li>Des circuits dédiés pour les gros appareils (four, lave-linge, lave-vaisselle)</li>
  <li>Un nombre minimal de prises par pièce (5 prises en salon, 3 en chambre)</li>
  <li>Des règles strictes en salle de bain (zones de sécurité 0, 1 et 2)</li>
  <li>Une mise à la terre de toute l'installation</li>
</ul>

<blockquote>Une installation non conforme peut invalider votre assurance habitation en cas de sinistre électrique — et vous rendre responsable en cas d'accident.</blockquote>

<h2>Les risques d'une installation vieillissante à Brest</h2>
<p>En France, environ 30 % des incendies domestiques ont une cause électrique. Un tableau vétuste, des prises sans terre ou des fils à nu sont des dangers silencieux mais réels dans les logements brestois d'avant 1980.</p>

<h2>Notre intervention à Brest</h2>
<p>Nos électriciens qualifiés réalisent le diagnostic de votre installation actuelle, planifient la mise aux normes complète et vous remettent un dossier de conformité. Découvrez l'ensemble de notre <a href="/blog/electricite-brest-renovation-normes/">offre d'électricité à Brest et en Finistère</a>.</p>

<p>Si vous rénovez votre salle de bain, la mise aux normes électrique est incluse dans notre <a href="/blog/renovation-salle-de-bain-brest-guide/">rénovation complète salle de bain à Brest</a>.</p>

<div style="background:rgba(196,255,14,0.08);border-left:4px solid #c4ff0e;padding:1.5rem;margin:2rem 0;border-radius:0 8px 8px 0;">
  <h3 style="color:#c4ff0e;margin-top:0;">Diagnostic électrique gratuit à Brest</h3>
  <p>Performance Habitat réalise un diagnostic complet de votre installation et vous propose un devis de mise aux normes à Brest et dans tout le Finistère.</p>
  <p><a href="/#contact"><strong>→ Demander mon diagnostic gratuit</strong></a> &nbsp;|&nbsp; <a href="tel:0650034777"><strong>☎ 06 50 03 47 77</strong></a></p>
</div>
""",
    },
]


class Command(BaseCommand):
    help = "Crée et met à jour les articles de blog SEO optimisés de Performance Habitat"

    def add_arguments(self, parser):
        parser.add_argument(
            '--delete-weak',
            action='store_true',
            help='Supprime les articles hors-sujet (cuisine ouverte)',
        )

    def handle(self, *args, **options):
        if options['delete_weak']:
            deleted, _ = Article.objects.filter(slug__in=WEAK_SLUGS).delete()
            self.stdout.write(self.style.WARNING(f"Supprimés : {deleted} article(s) hors-sujet"))

        created = updated = 0

        for data in ARTICLES:
            image_path = data.pop('image', None)
            article, is_new = Article.objects.update_or_create(
                slug=data['slug'],
                defaults={
                    'titre': data['titre'],
                    'categorie': data['categorie'],
                    'resume': data['resume'],
                    'contenu': data['contenu'],
                    'meta_description': data['meta_description'],
                    'is_published': True,
                },
            )
            # Assign image only if no image set yet (avoid overwriting manual uploads)
            if image_path and not article.image:
                article.image = image_path
                article.save(update_fields=['image'])

            if is_new:
                created += 1
                self.stdout.write(self.style.SUCCESS(f"  CRÉÉ   : {data['titre'][:70]}"))
            else:
                updated += 1
                self.stdout.write(f"  Mis à jour : {data['titre'][:70]}")

        self.stdout.write(self.style.SUCCESS(f"\n✓ {created} créé(s), {updated} mis à jour."))
