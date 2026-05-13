from django.core.management.base import BaseCommand
from main.models import Article

WEAK_SLUGS = [
    'cuisine-ouverte-guilers-renovation',
    'douche-italienne-brest',
]

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
  <li>Adaptation pour les personnes âgées ou à mobilité réduite</li>
  <li>Économies d'eau grâce à des équipements plus récents</li>
</ul>

<h2>Les étapes d'une rénovation salle de bain à Brest</h2>

<h3>1. Diagnostic et conception</h3>
<p>Notre équipe se déplace chez vous à Brest pour évaluer l'état de la plomberie, de l'électricité, de l'étanchéité et du carrelage existant. Nous identifions les contraintes techniques et vous proposons un plan adapté à votre espace et votre budget.</p>

<h3>2. Démolition et gros œuvre</h3>
<p>Dépose de l'ancien carrelage, enlèvement des sanitaires, modification éventuelle de cloisons. Nos artisans protègent vos autres pièces et gèrent l'évacuation des déchets. Cette phase dure généralement 1 à 2 jours.</p>

<h3>3. Plomberie et électricité</h3>
<p>Le cœur technique de votre rénovation. Nos plombiers et électriciens qualifiés réalisent les arrivées et évacuations d'eau, la mise aux normes électriques (zones de sécurité, câblage, tableau). Découvrez nos <a href="/services/">services de plomberie et d'électricité</a>.</p>

<h3>4. Étanchéité et carrelage</h3>
<p>Pose du système d'étanchéité dans la zone de douche, puis pose du carrelage et de la faïence avec joints de qualité. Un travail de précision pour une durabilité maximale.</p>

<h3>5. Installation des équipements</h3>
<p>Bac à douche avec paroi en verre, meuble vasque suspendu, robinetterie, miroir LED anti-buée, radiateur sèche-serviettes — tout est installé soigneusement selon vos choix.</p>

<h2>Quel budget pour une rénovation salle de bain à Brest ?</h2>

<h3>Rénovation légère (2 000 € – 4 500 €)</h3>
<p>Remplacement des sanitaires, peinture ou faïence partielle, changement du mitigeur. Idéal pour rafraîchir sans tout refaire.</p>

<h3>Rénovation complète (5 000 € – 9 000 €)</h3>
<p>Dépose totale, nouvelle plomberie, nouveau carrelage sol et mur, bac à douche avec paroi, meuble vasque suspendu, radiateur sèche-serviettes. C'est le projet le plus courant à Brest.</p>

<h3>Rénovation haut de gamme (10 000 € – 18 000 €)</h3>
<p>Grandes surfaces, matériaux premium, double vasque, domotique, colonne hydromassante.</p>

<blockquote>Performance Habitat propose des devis gratuits et transparents. Tout est chiffré avant le début des travaux — aucune mauvaise surprise.</blockquote>

<h2>Tendances salle de bain 2025 à Brest</h2>

<h3>Le carrelage grand format</h3>
<p>Les carreaux 60×60 cm ou 90×90 cm donnent un effet de grandeur, réduisent les joints et modernisent instantanément l'espace. Très prisés à Brest pour les salles de bain de taille moyenne.</p>

<h3>Le meuble vasque suspendu</h3>
<p>Plus facile à entretenir, il donne une impression de légèreté et agrandit visuellement la salle de bain. Disponible en bois, laqué blanc ou effet béton.</p>

<h3>Le style épuré</h3>
<p>Robinetterie encastrée, miroir LED large, radiateur sèche-serviettes design — le minimalisme est la tendance forte de 2025.</p>

<h2>Pourquoi choisir Performance Habitat pour votre salle de bain à Brest ?</h2>
<ul>
  <li><strong>Artisan local</strong> basé à Guilers, à deux minutes de Brest</li>
  <li><strong>Équipe complète</strong> : plombier, électricien, carreleur — un seul interlocuteur</li>
  <li><strong>Délais respectés</strong> et communication transparente tout au long du chantier</li>
  <li><strong>Garantie décennale</strong> sur tous nos travaux</li>
  <li><strong>Aucune sous-traitance</strong> — nos propres artisans interviennent chez vous</li>
</ul>

<p>Retrouvez quelques-unes de nos <a href="/realisations/">réalisations de salle de bain à Brest et en Finistère</a>.</p>

<div style="background:rgba(196,255,14,0.08);border-left:4px solid #c4ff0e;padding:1.5rem;margin:2rem 0;border-radius:0 8px 8px 0;">
  <h3 style="color:#c4ff0e;margin-top:0;">Votre projet de rénovation à Brest</h3>
  <p>Contactez Performance Habitat pour un devis gratuit et sans engagement. Nous nous déplaçons à Brest, Guilers, Plouzané, Le Relecq-Kerhuon, Bohars, Gouesnou et dans tout le Finistère.</p>
  <p><a href="/#contact"><strong>→ Demander mon devis gratuit</strong></a> &nbsp;|&nbsp; <a href="tel:0650034777"><strong>☎ 06 50 03 47 77</strong></a></p>
</div>
""",
    },

    # ── ARTICLE 2 ── Peinture intérieure Brest (remplace douche italienne)
    {
        "titre": "Peinture intérieure à Brest : rénover vos pièces avec style",
        "slug": "peinture-interieure-brest",
        "categorie": "conseil",
        "image": "blog/renovation-salle-de-bain-brest-realisation.jpg",
        "resume": "Peinture intérieure à Brest : conseils pour choisir vos couleurs, préparer vos murs et obtenir un résultat professionnel. Performance Habitat, artisan peintre en Finistère.",
        "meta_description": "Peinture intérieure à Brest : conseils, tarifs et réalisation par Performance Habitat. Artisan peintre en Finistère. Devis gratuit ☎ 06 50 03 47 77",
        "contenu": """
<h2>Peinture intérieure à Brest : donnez un coup de neuf à votre logement</h2>
<p>La peinture intérieure est l'un des travaux les plus efficaces pour transformer rapidement l'ambiance d'un logement. À <strong>Brest</strong> et dans le Finistère, <strong>Performance Habitat</strong> réalise vos travaux de peinture intérieure avec soin et précision — du lessivage des murs jusqu'à la finition.</p>

<h2>Nos prestations de peinture intérieure à Brest</h2>

<h3>Préparation des surfaces</h3>
<p>Un bon résultat commence par une bonne préparation. Nos peintres réalisent le lessivage des murs, le rebouchage des fissures et trous, la pose d'enduit de lissage si nécessaire, et l'application d'une sous-couche adaptée au support. Cette étape est souvent négligée dans les travaux en amateur — elle fait pourtant toute la différence sur la tenue de la peinture dans le temps.</p>

<h3>Peinture des murs et plafonds</h3>
<p>Application de la peinture en deux couches minimum, avec un travail soigné aux raccords, angles et bords de fenêtres. Nous utilisons des peintures professionnelles de qualité, lessivables et durables.</p>

<h3>Peinture de boiseries et menuiseries</h3>
<p>Portes, fenêtres, plinthes, radiateurs — nos peintres réalisent également la peinture de toutes les boiseries intérieures, avec la préparation adaptée (décapage, ponçage, impression).</p>

<h3>Remise en peinture complète d'appartement</h3>
<p>Pour les logements à rénover entièrement, nous réalisons la remise en peinture complète : toutes les pièces, plafonds, murs et boiseries. Idéal pour un déménagement, une mise en location ou une rénovation globale.</p>

<h2>Comment choisir ses couleurs de peinture ?</h2>

<h3>Les teintes claires pour agrandir</h3>
<p>Blanc cassé, gris clair, beige lin — les teintes claires reflètent la lumière et donnent une sensation d'espace. Idéales pour les petites pièces ou les logements peu lumineux, fréquents dans certains quartiers de Brest.</p>

<h3>Les teintes foncées pour créer une ambiance</h3>
<p>Bleu nuit, vert forêt, terracotta — une couleur foncée sur un mur accent (un seul mur) crée un effet graphique fort sans alourdir l'ensemble. Très tendance en 2025.</p>

<h3>Le blanc pour les plafonds</h3>
<p>Un plafond blanc ou blanc cassé est toujours la valeur sûre — il maximise la luminosité et met en valeur les murs colorés.</p>

<blockquote>Un conseil : testez toujours vos couleurs sur une surface de 50×50 cm avant de vous engager. Les couleurs changent beaucoup selon la luminosité naturelle de chaque pièce.</blockquote>

<h2>Peinture et rénovation salle de bain</h2>
<p>La peinture est aussi une partie importante de la <a href="/blog/renovation-salle-de-bain-brest-guide/">rénovation salle de bain à Brest</a>. Nous utilisons des peintures spéciales pièces humides, résistantes à l'humidité et aux moisissures, pour les murs non carrelés de votre salle de bain.</p>

<h2>Prix de la peinture intérieure à Brest</h2>
<p>Le prix dépend de la surface, de l'état des murs et des finitions souhaitées :</p>
<ul>
  <li><strong>Peinture murale simple</strong> (préparation + 2 couches) : 15 à 25 € / m²</li>
  <li><strong>Peinture avec reprise d'enduit importante</strong> : 25 à 40 € / m²</li>
  <li><strong>Peinture plafond</strong> : 12 à 20 € / m²</li>
</ul>
<p>Ces tarifs sont indicatifs — demandez un devis gratuit pour une estimation précise selon votre logement à Brest.</p>

<p>Découvrez aussi nos <a href="/services/">autres services de rénovation à Brest</a> et nos <a href="/realisations/">réalisations récentes en Finistère</a>.</p>

<div style="background:rgba(196,255,14,0.08);border-left:4px solid #c4ff0e;padding:1.5rem;margin:2rem 0;border-radius:0 8px 8px 0;">
  <h3 style="color:#c4ff0e;margin-top:0;">Votre projet de peinture à Brest</h3>
  <p>Contactez Performance Habitat pour un devis gratuit. Nous intervenons à Brest, Guilers, Plouzané, Le Relecq-Kerhuon et dans tout le Finistère.</p>
  <p><a href="/#contact"><strong>→ Demander mon devis gratuit</strong></a> &nbsp;|&nbsp; <a href="tel:0650034777"><strong>☎ 06 50 03 47 77</strong></a></p>
</div>
""",
    },

    # ── ARTICLE 3 ── Salle de bain PMR Brest
    {
        "titre": "Salle de bain PMR à Brest : accessibilité et réalisation",
        "slug": "salle-de-bain-pmr-brest",
        "categorie": "conseil",
        "image": "blog/renovation-salle-de-bain-brest-realisation.jpg",
        "resume": "Adapter votre salle de bain pour les personnes à mobilité réduite à Brest. Équipements PMR, normes et réalisations par Performance Habitat en Finistère.",
        "meta_description": "Salle de bain PMR à Brest : adaptation et réalisation pour personnes à mobilité réduite. Performance Habitat, artisan Finistère. Devis gratuit.",
        "contenu": """
<h2>Salle de bain PMR à Brest : l'accessibilité pour tous</h2>
<p>La rénovation d'une <strong>salle de bain PMR</strong> (Personne à Mobilité Réduite) concerne de nombreux foyers à Brest et dans le Finistère. Que ce soit pour une personne âgée, un proche handicapé ou pour anticiper l'avenir, <strong>Performance Habitat</strong> adapte votre salle de bain avec les bons équipements, dans les règles de l'art.</p>

<h2>Qu'est-ce qu'une salle de bain PMR ?</h2>
<p>Une salle de bain PMR est conçue pour être utilisée de manière autonome et sécurisée par des personnes à mobilité réduite, en fauteuil roulant, âgées ou souffrant de handicaps moteurs. Elle intègre des équipements spécifiques et respecte des normes d'espace précises.</p>

<h3>Les équipements essentiels</h3>
<ul>
  <li><strong>Bac à douche PMR à seuil bas</strong> : accès facilité sans enjamber un rebord haut, avec siège de douche rabattable</li>
  <li><strong>Barres d'appui</strong> : fixées solidement dans les murs (pas sur du placo seul), dans la douche et près des WC</li>
  <li><strong>Lavabo ergonomique</strong> : hauteur adaptée, dégagé en dessous pour un accès en fauteuil</li>
  <li><strong>Mitigeur thermostatique</strong> : évite les risques de brûlure, facile à manœuvrer d'une seule main</li>
  <li><strong>Sol antidérapant</strong> : carrelage classé R11 dans la zone de douche</li>
  <li><strong>Espace de circulation</strong> : passage libre d'au moins 80 cm, espace de rotation suffisant</li>
</ul>

<h2>Les normes d'espace pour une salle de bain PMR</h2>
<ul>
  <li>Largeur de porte : minimum 80 cm (90 cm recommandé)</li>
  <li>Espace libre devant le lavabo : 70 cm de profondeur</li>
  <li>Zone de douche : dimension minimale 90×90 cm, 120×90 cm recommandé</li>
  <li>Espace de rotation en fauteuil : cercle de 150 cm de diamètre</li>
</ul>

<blockquote>Chaque adaptation est unique. Nous analysons votre espace et vos besoins précis pour proposer les solutions les plus adaptées — même dans les petites salles de bain brestoises.</blockquote>

<h2>Nos réalisations de salle de bain PMR en Finistère</h2>
<p>Performance Habitat a réalisé de nombreuses adaptations de salle de bain à Brest, Guilers, Plouzané et dans tout le Finistère. Chaque projet est abordé avec la même rigueur : sécurité, confort et esthétique. Consultez nos <a href="/realisations/">réalisations</a> pour vous inspirer.</p>

<p>La rénovation PMR fait souvent partie d'un projet plus large de <a href="/blog/renovation-salle-de-bain-brest-guide/">rénovation complète de salle de bain à Brest</a>.</p>

<div style="background:rgba(196,255,14,0.08);border-left:4px solid #c4ff0e;padding:1.5rem;margin:2rem 0;border-radius:0 8px 8px 0;">
  <h3 style="color:#c4ff0e;margin-top:0;">Adapter votre salle de bain à Brest</h3>
  <p>Contactez Performance Habitat pour un devis gratuit. Nous vous conseillons sur les équipements et réalisons vos travaux à Brest et dans tout le Finistère.</p>
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
  <li>Prises sans prise de terre (les anciennes prises à deux fiches rondes)</li>
  <li>Tableau électrique avec fusibles à vis (avant les disjoncteurs modernes)</li>
  <li>Fils apparents, gaines abîmées ou brûlées</li>
  <li>Odeur de brûlé près des prises ou interrupteurs</li>
  <li>Installation de plus de 25 ans sans diagnostic</li>
</ul>

<blockquote>En France, environ 30 % des incendies domestiques ont une cause électrique. Une installation conforme réduit drastiquement ce risque.</blockquote>

<h2>La norme NF C 15-100 à Brest</h2>
<p>La <strong>norme NF C 15-100</strong> est le référentiel français des installations électriques résidentielles. Elle impose notamment :</p>
<ul>
  <li>Un tableau équipé d'un disjoncteur différentiel 30 mA</li>
  <li>Des circuits dédiés pour les gros électroménagers (four, lave-linge, lave-vaisselle)</li>
  <li>Un nombre minimal de prises par pièce (5 en salon, 3 en chambre)</li>
  <li>Des règles strictes en salle de bain (zones de sécurité 0, 1 et 2)</li>
  <li>Une mise à la terre de toute l'installation</li>
</ul>

<h2>Nos prestations d'électricité à Brest</h2>

<h3>Diagnostic électrique</h3>
<p>Avant tout travaux, nous réalisons un diagnostic complet : état du tableau, présence de la mise à la terre, conformité des circuits, état des gaines et des fils. Ce diagnostic permet d'établir un devis précis et de prioriser les interventions.</p>

<h3>Remplacement du tableau électrique</h3>
<p>Un tableau moderne avec disjoncteurs différentiels protège efficacement vos équipements et votre famille. Le remplacement d'un tableau complet à Brest est généralement réalisé en une journée.</p>

<h3>Création ou modification de circuits</h3>
<p>Ajout de prises, création d'un circuit dédié, déplacement d'interrupteurs — nous réalisons tous les travaux de second œuvre électrique à Brest et dans le Finistère.</p>

<h3>Électricité en salle de bain</h3>
<p>La salle de bain est la pièce la plus réglementée sur le plan électrique. Nos électriciens respectent scrupuleusement les zones de sécurité définies par la norme. Voir notre article sur la <a href="/blog/renovation-salle-de-bain-brest-guide/">rénovation salle de bain à Brest</a>.</p>

<h2>Pourquoi confier vos travaux d'électricité à Performance Habitat ?</h2>
<ul>
  <li>Électriciens qualifiés, formés aux dernières normes en vigueur</li>
  <li>Intervention à Brest, Guilers, Plouzané, Le Relecq-Kerhuon et tout le Finistère</li>
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

    # ── ARTICLE 5 ── Pompe à chaleur air-air Brest (SEULEMENT air-air, sans aides)
    {
        "titre": "Pompe à chaleur à Brest : installation PAC air-air par votre artisan local",
        "slug": "pompe-a-chaleur-brest-finistere",
        "categorie": "conseil",
        "image": "blog/renovation-energetique-economies-chauffage.jpg",
        "resume": "Installation de pompe à chaleur air-air à Brest et en Finistère. Performance Habitat installe votre PAC pour chauffer et rafraîchir votre logement efficacement.",
        "meta_description": "Pompe à chaleur air-air à Brest : installation par Performance Habitat, artisan local en Finistère. Devis gratuit ☎ 06 50 03 47 77",
        "contenu": """
<h2>Pompe à chaleur à Brest : le chauffage économique pour le climat breton</h2>
<p>La <strong>pompe à chaleur air-air (PAC)</strong> est une solution de chauffage particulièrement adaptée au climat de Brest et du Finistère. Doux et humide, le climat breton — avec des températures rarement inférieures à 0°C en hiver — est idéal pour ce type d'équipement. <strong>Performance Habitat</strong> installe des pompes à chaleur air-air à Brest, Guilers, Plouzané et dans tout le Finistère.</p>

<h2>Qu'est-ce qu'une pompe à chaleur air-air ?</h2>
<p>La PAC air-air capte les calories présentes dans l'air extérieur et les transfère à l'intérieur du logement via des unités intérieures (splits). Elle fonctionne en mode chauffage en hiver et en mode rafraîchissement en été — un équipement deux-en-un particulièrement pratique.</p>

<h3>Avantages de la PAC air-air à Brest</h3>
<ul>
  <li><strong>Efficacité climatique</strong> : le climat doux de Brest maximise les performances de la PAC toute l'année</li>
  <li><strong>Chauffage et climatisation</strong> : un seul équipement pour le chaud et le froid</li>
  <li><strong>Économies d'énergie</strong> : jusqu'à 3 fois moins de consommation qu'un radiateur électrique classique</li>
  <li><strong>Installation rapide</strong> : généralement réalisée en 1 à 2 jours par notre équipe</li>
  <li><strong>Fonctionnement silencieux</strong> : les modèles récents sont très discrets</li>
</ul>

<h2>Comment fonctionne une PAC air-air ?</h2>
<p>L'unité extérieure (placée sur la façade ou au sol) capte la chaleur de l'air extérieur même par temps froid. Un fluide frigorigène transporte cette énergie vers les unités intérieures qui soufflent de l'air chaud dans les pièces. En été, le cycle s'inverse pour rafraîchir.</p>

<blockquote>À Brest, où les températures hivernales oscillent entre 4°C et 10°C, une PAC air-air fonctionne à pleine efficacité la quasi-totalité de la saison de chauffe.</blockquote>

<h2>Notre installation PAC air-air à Brest</h2>

<h3>Étude de votre logement</h3>
<p>Avant tout, nous analysons votre logement : surface à chauffer, isolation existante, nombre de pièces, configuration des murs pour l'unité extérieure. Cette étude permet de dimensionner correctement votre PAC et de choisir le bon modèle.</p>

<h3>Installation par nos techniciens</h3>
<p>Pose de l'unité extérieure, installation des unités intérieures (splits) dans les pièces choisies, raccordement électrique, liaison frigorifique entre les unités. Tout est réalisé par notre équipe qualifiée.</p>

<h3>Mise en service et réglages</h3>
<p>Après installation, nous mettons en service votre PAC, effectuons les réglages de confort (températures, programmation horaire) et vous expliquons son fonctionnement.</p>

<h2>Prix d'une pompe à chaleur air-air à Brest</h2>
<p>Le prix varie selon la puissance et le nombre d'unités intérieures :</p>
<ul>
  <li><strong>Monosplit (1 pièce)</strong> : 1 500 € – 3 500 € fourniture et pose</li>
  <li><strong>Multisplit (2 à 4 pièces)</strong> : 3 000 € – 7 000 € fourniture et pose</li>
</ul>

<p>Retrouvez tous nos <a href="/services/">services de chauffage à Brest et en Finistère</a>.</p>

<div style="background:rgba(196,255,14,0.08);border-left:4px solid #c4ff0e;padding:1.5rem;margin:2rem 0;border-radius:0 8px 8px 0;">
  <h3 style="color:#c4ff0e;margin-top:0;">Votre projet PAC à Brest</h3>
  <p>Contactez Performance Habitat pour une étude gratuite et sans engagement. Nous installons votre pompe à chaleur à Brest, Guilers, Plouzané et dans tout le Finistère.</p>
  <p><a href="/#contact"><strong>→ Demander mon devis gratuit</strong></a> &nbsp;|&nbsp; <a href="tel:0650034777"><strong>☎ 06 50 03 47 77</strong></a></p>
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
<p>En salle de bain, le carrelage doit présenter une absorption d'eau très faible. Les carreaux en grès cérame émaillé ou en grès cérame pleine masse sont les plus adaptés aux pièces humides.</p>

<h3>L'antidérapance</h3>
<p>Pour le sol de la salle de bain, choisissez un carrelage antidérapant classé au minimum <strong>R10</strong>. Une surface glissante est un risque de chute, surtout pour les personnes âgées.</p>

<h3>Le format des carreaux</h3>
<ul>
  <li><strong>Petit format (10×10, 20×20 cm)</strong> : style vintage, idéal pour les petites salles de bain</li>
  <li><strong>Format moyen (30×60, 45×45 cm)</strong> : polyvalent, effet classique</li>
  <li><strong>Grand format (60×60, 60×120 cm)</strong> : tendance 2025, agrandit visuellement l'espace et réduit les joints</li>
</ul>

<h2>Les tendances carrelage salle de bain 2025 à Brest</h2>

<h3>L'effet béton ciré</h3>
<p>Le carrelage imitation béton ciré est la tendance numéro 1 en 2025. Discret, moderne, il s'associe parfaitement au bois et au métal noir. Disponible en grand format pour un effet maximal.</p>

<h3>Le carrelage imitation marbre</h3>
<p>Le grès cérame imitation marbre offre un rendu luxueux à prix maîtrisé. Très prisé à Brest pour les salles de bain d'appartements haut de gamme.</p>

<h3>Le large format uni</h3>
<p>Les dalles 120×120 cm en grès cérame blanc ou gris clair transforment une petite salle de bain en espace aérien.</p>

<h2>La pose de carrelage par Performance Habitat</h2>

<h3>Préparation du support</h3>
<p>Un carrelage tient dans le temps seulement si le support est parfaitement préparé : planéité, absence d'humidité, étanchéité dans la zone de douche. Nous préparons soigneusement chaque support avant toute pose.</p>

<h3>Pose avec colle adaptée</h3>
<p>Colle C2 pour les grands formats, colle hydrofuge dans les zones humides — nos carreleurs utilisent systématiquement les produits adaptés à chaque configuration.</p>

<h3>Joints de qualité</h3>
<p>Joints époxy dans la zone de douche (résistance aux moisissures), joints ciment de qualité professionnelle dans les autres zones. Un carrelage bien jointoyé dure deux fois plus longtemps.</p>

<blockquote>Un carrelage mal posé, c'est des carreaux qui se décollent en 2 ans. Un carrelage posé par un professionnel, c'est 20 ans de tranquillité.</blockquote>

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
<p>La rénovation de salle de bain est notre spécialité. À Plouzané, nous réalisons des projets complets ou partiels : remplacement de la baignoire par un bac à douche moderne avec paroi en verre, pose de carrelage grand format, installation d'un meuble vasque suspendu, mise aux normes de la plomberie et de l'électricité.</p>
<p>En savoir plus sur notre <a href="/blog/renovation-salle-de-bain-brest-guide/">guide complet de rénovation salle de bain</a>.</p>

<h3>Électricité à Plouzané</h3>
<p>Tableau électrique vétuste, prises sans terre, installation non conforme — nos électriciens qualifiés réalisent le diagnostic et la mise aux normes de votre installation à Plouzané. En savoir plus sur notre <a href="/blog/electricite-brest-renovation-normes/">service d'installation électrique</a>.</p>

<h3>Carrelage et faïence à Plouzané</h3>
<p>Pose de carrelage sol et mur, faïence salle de bain, terrasse — notre carreleur intervient à Plouzané avec les matériaux de votre choix. Découvrez nos conseils sur le <a href="/blog/carrelage-salle-de-bain-brest/">carrelage de salle de bain</a>.</p>

<h3>Plomberie à Plouzané</h3>
<p>Fuite d'eau, remplacement de chauffe-eau, canalisation bouchée ou rénovation complète de la plomberie — Performance Habitat intervient à Plouzané pour toutes vos urgences et projets.</p>

<h3>Pompe à chaleur à Plouzané</h3>
<p>Installation de pompe à chaleur air-air à Plouzané — un équipement particulièrement adapté au climat breton pour chauffer et rafraîchir votre logement efficacement. En savoir plus sur notre <a href="/blog/pompe-a-chaleur-brest-finistere/">service pompe à chaleur</a>.</p>

<h3>Peinture intérieure à Plouzané</h3>
<p>Remise en peinture d'appartement ou de maison à Plouzané : préparation des murs, application professionnelle, finitions soignées. Voir notre article sur la <a href="/blog/peinture-interieure-brest/">peinture intérieure à Brest et en Finistère</a>.</p>

<h2>Pourquoi choisir Performance Habitat à Plouzané ?</h2>

<h3>Un artisan local, à deux pas de chez vous</h3>
<p>Basés à Guilers, nous intervenons régulièrement à Plouzané. Notre proximité garantit des délais d'intervention courts et une réactivité que ne peuvent pas offrir les grandes entreprises éloignées.</p>

<h3>Un seul interlocuteur pour tous vos travaux</h3>
<p>Plomberie, électricité, carrelage, peinture : Performance Habitat est une équipe pluridisciplinaire. Vous avez un seul contact pour l'ensemble de votre projet — un gain de temps considérable.</p>

<blockquote>Aucune sous-traitance : tous nos travaux à Plouzané sont réalisés par notre propre équipe.</blockquote>

<p>Consultez nos <a href="/realisations/">réalisations récentes</a> pour découvrir la qualité de notre travail.</p>

<div style="background:rgba(196,255,14,0.08);border-left:4px solid #c4ff0e;padding:1.5rem;margin:2rem 0;border-radius:0 8px 8px 0;">
  <h3 style="color:#c4ff0e;margin-top:0;">Votre projet de rénovation à Plouzané</h3>
  <p>Contactez Performance Habitat pour un devis gratuit. Déplacement offert à Plouzané et dans tout le Finistère.</p>
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
<p>Vous habitez au <strong>Relecq-Kerhuon</strong> et vous cherchez un artisan qualifié pour vos travaux ? <strong>Performance Habitat</strong>, installé à Guilers, est votre partenaire de proximité pour tous vos projets : rénovation de salle de bain, mise aux normes électrique, carrelage, plomberie et chauffage.</p>

<h2>Nos interventions au Relecq-Kerhuon</h2>

<h3>Rénovation salle de bain au Relecq-Kerhuon</h3>
<p>Que vous habitiez dans un appartement ou une maison au Relecq-Kerhuon, nos artisans rénovent votre salle de bain de A à Z. Dépose de l'ancienne installation, travaux de plomberie et d'électricité, pose du carrelage, installation des équipements (bac à douche avec paroi, meuble vasque, radiateur sèche-serviettes) — tout est géré par notre équipe.</p>

<h3>Électricité au Relecq-Kerhuon</h3>
<p>Nos électriciens qualifiés réalisent la mise aux normes de votre installation électrique au Relecq-Kerhuon : remplacement du tableau, création de circuits, mise à la terre. Voir notre article sur l'<a href="/blog/electricite-brest-renovation-normes/">installation électrique en Finistère</a>.</p>

<h3>Plomberie au Relecq-Kerhuon</h3>
<p>Fuite, canalisation bouchée, remplacement de chauffe-eau ou rénovation complète de la plomberie : nos plombiers interviennent rapidement au Relecq-Kerhuon.</p>

<h3>Carrelage au Relecq-Kerhuon</h3>
<p>Pose de carrelage salle de bain, salon ou cuisine au Relecq-Kerhuon. Voir nos conseils sur le <a href="/blog/carrelage-salle-de-bain-brest/">carrelage salle de bain</a>.</p>

<h2>Rénovation d'appartement au Relecq-Kerhuon</h2>
<p>Le Relecq-Kerhuon est une commune résidentielle de la métropole brestoise avec de nombreux appartements des années 70-80 dont les salles de bain et installations méritent d'être rénovées. Performance Habitat est spécialisé dans ce type de rénovation : nous travaillons dans des espaces réduits, en minimisant les nuisances pour les voisins et en respectant les règles de copropriété.</p>

<blockquote>Grand projet ou petit chantier : nous intervenons au Relecq-Kerhuon avec le même soin et la même rigueur.</blockquote>

<p>Consultez nos <a href="/realisations/">réalisations</a> pour voir des exemples de projets dans la région brestoise.</p>

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
<p>La salle de bain est souvent le premier chantier lors d'une rénovation de maison. Performance Habitat réalise des rénovations complètes : dépose de l'ancien, plomberie, électricité, carrelage, équipements neufs. Découvrez notre <a href="/blog/renovation-salle-de-bain-brest-guide/">guide complet de rénovation salle de bain en Finistère</a>.</p>

<h3>Installation et rénovation électrique</h3>
<p>Les maisons bretonnes des années 60-80 ont souvent des installations électriques vieillissantes. Nos électriciens qualifiés réalisent le diagnostic et la mise aux normes complète. En savoir plus sur notre <a href="/blog/electricite-brest-renovation-normes/">service d'électricité en Finistère</a>.</p>

<h3>Plomberie et sanitaires</h3>
<p>Remplacement de canalisations, installation d'un nouveau chauffe-eau, rénovation de salle de bain — nos plombiers interviennent dans tout le Finistère avec réactivité et professionnalisme.</p>

<h3>Chauffage et pompe à chaleur</h3>
<p>Installation d'une pompe à chaleur air-air, remplacement d'un système de chauffage — Performance Habitat vous aide à choisir la solution la plus adaptée à votre maison en Finistère. Voir notre article sur la <a href="/blog/pompe-a-chaleur-brest-finistere/">pompe à chaleur en Finistère</a>.</p>

<h3>Carrelage et sols</h3>
<p>Pose de carrelage en salle de bain, cuisine, couloir ou terrasse — notre carreleur réalise des poses soignées sur tout le Finistère. Découvrez nos conseils sur le <a href="/blog/carrelage-salle-de-bain-brest/">carrelage de salle de bain</a>.</p>

<h3>Peinture intérieure</h3>
<p>Peinture intérieure, lessivage des murs, plafonds — nos peintres donnent un coup de neuf à vos pièces. Voir notre article sur la <a href="/blog/peinture-interieure-brest/">peinture intérieure à Brest</a>.</p>

<h2>Zone d'intervention en Finistère</h2>
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

<blockquote>Aucune sous-traitance : tous nos travaux sont réalisés par notre propre équipe. Vous savez toujours qui intervient chez vous.</blockquote>

<div style="background:rgba(196,255,14,0.08);border-left:4px solid #c4ff0e;padding:1.5rem;margin:2rem 0;border-radius:0 8px 8px 0;">
  <h3 style="color:#c4ff0e;margin-top:0;">Votre projet de rénovation en Finistère</h3>
  <p>Contactez Performance Habitat pour un devis gratuit. Nous vous rencontrons chez vous pour évaluer vos besoins et vous proposer une solution adaptée à votre budget.</p>
  <p><a href="/#contact"><strong>→ Demander mon devis gratuit</strong></a> &nbsp;|&nbsp; <a href="tel:0650034777"><strong>☎ 06 50 03 47 77</strong></a></p>
</div>
""",
    },

    # ── ARTICLE 10 ── Artisan rénovation Guilers
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

<h2>Nos services à Guilers</h2>

<h3>Rénovation salle de bain à Guilers</h3>
<p>Notre spécialité principale. À Guilers, nous rénovons des salles de bain de toutes tailles : petites salles d'eau d'appartement, grandes salles de bain de maison individuelle.</p>
<ul>
  <li>Remplacement baignoire par bac à douche avec paroi en verre</li>
  <li>Nouveau carrelage sol et mur grand format</li>
  <li>Meuble vasque suspendu et miroir LED</li>
  <li>Radiateur sèche-serviettes design</li>
  <li>Mise aux normes plomberie et électricité</li>
</ul>
<p>Découvrez notre <a href="/blog/renovation-salle-de-bain-brest-guide/">guide complet de rénovation salle de bain</a>.</p>

<h3>Plomberie à Guilers</h3>
<p>Intervention rapide pour toutes urgences plomberie à Guilers : fuite d'eau, canalisation bouchée, chauffe-eau en panne. Nous réalisons aussi les rénovations complètes de plomberie.</p>

<h3>Électricité à Guilers</h3>
<p>Mise aux normes, remplacement de tableau électrique, création de circuits — nos électriciens qualifiés interviennent à Guilers. Voir notre article sur l'<a href="/blog/electricite-brest-renovation-normes/">installation électrique en Finistère</a>.</p>

<h3>Carrelage à Guilers</h3>
<p>Pose de carrelage salle de bain, salon, cuisine ou terrasse à Guilers. Nos carreleurs maîtrisent les grands formats et les matériaux exigeants.</p>

<h3>Pompe à chaleur à Guilers</h3>
<p>Installation de PAC air-air à Guilers pour un chauffage économique adapté au climat breton. En savoir plus sur la <a href="/blog/pompe-a-chaleur-brest-finistere/">pompe à chaleur en Finistère</a>.</p>

<h3>Peinture intérieure à Guilers</h3>
<p>Remise en peinture de vos pièces à Guilers : préparation, lessivage, application professionnelle. Voir notre article sur la <a href="/blog/peinture-interieure-brest/">peinture intérieure</a>.</p>

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

    # ── EXISTING ARTICLES UPDATED ──
    {
        "titre": "5 erreurs à éviter lors de la rénovation de votre salle de bain",
        "slug": "5-erreurs-renovation-salle-de-bain",
        "categorie": "conseil",
        "image": "blog/5-erreurs-renovation-salle-de-bain.jpg",
        "resume": "Rénover sa salle de bain à Brest réserve des pièges. Découvrez les 5 erreurs les plus coûteuses — et comment les éviter avec les conseils de Performance Habitat.",
        "meta_description": "5 erreurs coûteuses en rénovation salle de bain à Brest. Conseils d'expert de Performance Habitat, artisan en Finistère. Devis gratuit.",
        "contenu": """
<h2>1. Négliger la ventilation</h2>
<p>À <strong>Brest</strong> et dans le Finistère, l'humidité est un enjeu particulièrement important. Une salle de bain mal ventilée est un nid à moisissures. Beaucoup de propriétaires oublient d'installer ou de remplacer la VMC (Ventilation Mécanique Contrôlée), pensant que c'est un détail. C'est pourtant l'une des erreurs les plus coûteuses à corriger après coup.</p>
<blockquote>Un taux d'humidité élevé en salle de bain réduit la durée de vie de votre carrelage et de vos joints — encore plus en Bretagne où l'air est naturellement chargé en humidité.</blockquote>

<h2>2. Sous-estimer le budget</h2>
<p>La rénovation d'une salle de bain à Brest réserve souvent des surprises : canalisations à remplacer, sol à reprendre, isolation à renforcer. Prévoyez toujours une <strong>marge de 15 à 20 %</strong> sur votre budget initial. Consultez notre <a href="/blog/renovation-salle-de-bain-brest-guide/">guide des prix de rénovation salle de bain à Brest</a> pour une estimation précise.</p>

<h2>3. Choisir le mauvais carrelage</h2>
<p>Tous les carreaux ne se valent pas. Un carrelage non adapté à une zone humide peut se fissurer en quelques mois. En salle de bain, exigez un carrelage grès cérame résistant à l'eau et antidérapant (R10 minimum). Voir nos <a href="/blog/carrelage-salle-de-bain-brest/">conseils sur le carrelage salle de bain à Brest</a>.</p>

<h2>4. Ignorer les normes électriques</h2>
<p>En salle de bain, des zones de sécurité strictes (zones 0, 1 et 2) définissent quels équipements peuvent être installés et où. Une prise mal positionnée peut être dangereuse et vous coûter une mise en conformité lors de la revente. Nos électriciens respectent scrupuleusement ces normes. Voir notre article sur l'<a href="/blog/electricite-brest-renovation-normes/">électricité en salle de bain à Brest</a>.</p>

<h2>5. Vouloir tout faire soi-même</h2>
<p>Les tutoriels donnent parfois l'illusion que la plomberie ou l'électricité sont à la portée de tous. En réalité, une mauvaise installation peut entraîner des dégâts des eaux, des risques d'électrocution et l'invalidation de votre assurance habitation. À Brest et en Finistère, faire appel à un artisan qualifié comme Performance Habitat protège votre famille et votre patrimoine.</p>

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
        "resume": "Transformation totale d'une salle de bain vieillissante à Brest : bac à douche avec paroi en verre, carrelage grand format, meuble suspendu. Détails du chantier.",
        "meta_description": "Réalisation rénovation salle de bain à Brest : bac à douche, carrelage grand format, meuble suspendu. Performance Habitat, artisan Finistère.",
        "contenu": """
<h2>Le projet : une salle de bain des années 90 transformée à Brest</h2>
<p>Nos clients, un couple installé à <strong>Brest</strong> depuis 15 ans, souhaitaient transformer leur salle de bain datant des années 90 en un espace contemporain, lumineux et pratique. Budget : 8 500 € — Durée des travaux : 12 jours ouvrés.</p>

<h2>Ce qui a été réalisé</h2>
<ul>
  <li>Dépose complète de l'ancienne installation (baignoire, carrelage, cloisons)</li>
  <li>Mise aux normes de la plomberie et de l'électricité (zones de sécurité)</li>
  <li>Installation d'un bac à douche extra-plat 90×120 cm avec paroi en verre trempé</li>
  <li>Carrelage grand format 60×60 cm effet béton ciré</li>
  <li>Meuble vasque suspendu double vasque</li>
  <li>Miroir LED avec anti-buée intégré</li>
  <li>Radiateur sèche-serviettes électrique design</li>
  <li>Peinture des murs en teinte minérale douce</li>
</ul>

<h2>Les défis techniques</h2>
<p>L'ancienne baignoire avait laissé des traces d'humidité sur le mur porteur. Nous avons traité le problème à la source : application d'une résine hydrofuge, pose d'un système d'étanchéité complet. Ce type de surprise est fréquent dans les logements brestois des années 80-90 — notre expérience locale nous permet d'y faire face sans impact sur le délai global.</p>

<h2>Le résultat</h2>
<p>Un espace de 6 m² qui semble deux fois plus grand grâce au carrelage clair et aux miroirs. Nos clients sont ravis : <em>« On ne reconnaît plus notre salle de bain, c'est comme être dans un hôtel 4 étoiles ! »</em></p>

<blockquote>Chaque réalisation est unique. Nous adaptons nos solutions à votre espace, vos goûts et votre budget — à Brest comme dans tout le Finistère.</blockquote>

<p>Consultez nos <a href="/realisations/">autres réalisations</a> et notre <a href="/blog/renovation-salle-de-bain-brest-guide/">guide de rénovation salle de bain à Brest</a>.</p>

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
<p>De nombreuses maisons et appartements à <strong>Brest</strong> datent des années 60-80 et n'ont jamais eu leur plomberie rénovée. La durée de vie varie selon le matériau : les tuyaux en plomb (encore présents dans certaines maisons brestoises) doivent être remplacés d'urgence, l'acier galvanisé dure 40 à 70 ans, le cuivre 50 à 80 ans en bonne condition.</p>

<h2>Les 5 signes qui indiquent un changement nécessaire</h2>
<ul>
  <li><strong>Eau colorée ou rouillée</strong> : signe de corrosion interne des canalisations</li>
  <li><strong>Chute de pression</strong> : fuites cachées ou dépôt calcaire important</li>
  <li><strong>Bruit de canalisations</strong> : sifflements, claquements révèlent une usure avancée</li>
  <li><strong>Fuites récurrentes</strong> : si vous réparez souvent les mêmes endroits, le réseau est fatigué</li>
  <li><strong>Taches d'humidité</strong> : sur les murs ou plafonds, même sans fuite visible</li>
</ul>

<blockquote>Un dégât des eaux non détecté peut causer jusqu'à 30 000 € de dommages. À Brest, où les hivers humides sollicitent davantage les installations, mieux vaut prévenir que guérir.</blockquote>

<h2>Plomberie et rénovation salle de bain : l'opportunité à saisir</h2>
<p>Si votre plomberie doit être rénovée, c'est souvent l'occasion idéale de rénover également votre salle de bain. Les travaux de plomberie nécessitent d'ouvrir les murs — autant en profiter pour moderniser l'ensemble. Consultez notre <a href="/blog/renovation-salle-de-bain-brest-guide/">guide de rénovation salle de bain à Brest</a> pour évaluer votre projet.</p>

<div style="background:rgba(196,255,14,0.08);border-left:4px solid #c4ff0e;padding:1.5rem;margin:2rem 0;border-radius:0 8px 8px 0;">
  <h3 style="color:#c4ff0e;margin-top:0;">Diagnostic plomberie gratuit à Brest</h3>
  <p>Contactez Performance Habitat pour un diagnostic gratuit à Brest et dans tout le Finistère.</p>
  <p><a href="/#contact"><strong>→ Demander mon diagnostic gratuit</strong></a> &nbsp;|&nbsp; <a href="tel:0650034777"><strong>☎ 06 50 03 47 77</strong></a></p>
</div>
""",
    },
    {
        "titre": "Rénovation énergétique en Finistère : économisez sur votre chauffage",
        "slug": "renovation-energetique-economies-chauffage",
        "categorie": "actualite",
        "image": "blog/renovation-energetique-economies-chauffage.jpg",
        "resume": "Rénovation énergétique à Brest et en Finistère : pompe à chaleur air-air et travaux d'isolation. Réduisez votre facture de chauffage avec Performance Habitat.",
        "meta_description": "Rénovation énergétique à Brest et Finistère : pompe à chaleur et isolation. Réduisez votre chauffage. Performance Habitat, artisan local.",
        "contenu": """
<h2>Rénovation énergétique à Brest et en Finistère</h2>
<p>Face à la hausse des prix de l'énergie, la rénovation thermique est devenue une priorité pour de nombreux propriétaires bretons. À <strong>Brest</strong> et dans le <strong>Finistère</strong>, un logement mal isolé ou équipé d'un chauffage vétuste peut voir sa facture réduite significativement après les bons travaux.</p>

<h2>Les travaux les plus efficaces</h2>

<h3>La pompe à chaleur air-air</h3>
<p>La PAC air-air est la solution que nous recommandons en priorité à Brest. Le climat breton doux est idéal pour ce type d'équipement qui chauffe en hiver et rafraîchit en été. Performance Habitat installe des pompes à chaleur air-air sur tout le Finistère. Découvrez notre <a href="/blog/pompe-a-chaleur-brest-finistere/">article dédié à la PAC air-air à Brest</a>.</p>

<h3>L'isolation thermique</h3>
<p>L'isolation des combles est le premier levier à activer : elle peut représenter jusqu'à 30 % d'économies sur la facture annuelle de chauffage. En Bretagne, l'isolation par l'extérieur (ITE) est particulièrement adaptée aux maisons en granit.</p>

<h3>Le remplacement du système de chauffage</h3>
<p>Remplacer un système de chauffage vétuste — radiateurs électriques à grille-pain, convecteurs anciens — par des équipements modernes est souvent le geste le plus rentable pour réduire la consommation énergétique.</p>

<blockquote>Le climat de Brest, doux et tempéré, est particulièrement favorable aux pompes à chaleur. Une PAC bien dimensionnée peut diviser par 3 votre consommation de chauffage.</blockquote>

<h2>Performance Habitat vous accompagne</h2>
<p>Performance Habitat réalise l'installation de pompes à chaleur air-air et les travaux de rénovation connexes à Brest et dans tout le Finistère. Un seul interlocuteur pour tous vos travaux d'amélioration énergétique.</p>

<p>Consultez également nos <a href="/services/">services de chauffage et rénovation</a>.</p>

<div style="background:rgba(196,255,14,0.08);border-left:4px solid #c4ff0e;padding:1.5rem;margin:2rem 0;border-radius:0 8px 8px 0;">
  <h3 style="color:#c4ff0e;margin-top:0;">Votre projet énergétique à Brest</h3>
  <p>Contactez Performance Habitat pour discuter de votre projet de rénovation énergétique à Brest et en Finistère.</p>
  <p><a href="/#contact"><strong>→ Demander mon devis gratuit</strong></a> &nbsp;|&nbsp; <a href="tel:0650034777"><strong>☎ 06 50 03 47 77</strong></a></p>
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
<p>La <strong>norme NF C 15-100</strong> est le référentiel français des installations électriques dans les habitations. À <strong>Brest</strong> et en Finistère, de nombreux logements des années 60-80 présentent des installations non conformes — un risque réel pour vos occupants.</p>

<h2>Ce que la norme impose</h2>
<ul>
  <li>Un tableau électrique avec disjoncteur différentiel 30 mA</li>
  <li>Des circuits dédiés pour les gros appareils (four, lave-linge, lave-vaisselle)</li>
  <li>Un nombre minimal de prises par pièce (5 en salon, 3 en chambre)</li>
  <li>Des règles strictes en salle de bain (zones de sécurité 0, 1 et 2)</li>
  <li>Une mise à la terre de toute l'installation</li>
</ul>

<blockquote>Une installation non conforme peut invalider votre assurance habitation en cas de sinistre électrique.</blockquote>

<h2>Les risques d'une installation vieillissante à Brest</h2>
<p>Environ 30 % des incendies domestiques en France ont une cause électrique. Un tableau vétuste, des prises sans terre ou des fils à nu sont des dangers silencieux dans les logements brestois d'avant 1980.</p>

<h2>Notre intervention à Brest</h2>
<p>Nos électriciens qualifiés réalisent le diagnostic de votre installation, planifient la mise aux normes complète et vous accompagnent jusqu'à la conformité. Découvrez l'ensemble de notre <a href="/blog/electricite-brest-renovation-normes/">offre d'électricité à Brest et en Finistère</a>.</p>

<div style="background:rgba(196,255,14,0.08);border-left:4px solid #c4ff0e;padding:1.5rem;margin:2rem 0;border-radius:0 8px 8px 0;">
  <h3 style="color:#c4ff0e;margin-top:0;">Diagnostic électrique gratuit à Brest</h3>
  <p>Performance Habitat réalise un diagnostic complet et un devis de mise aux normes à Brest et dans tout le Finistère.</p>
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
            help='Supprime les articles hors-sujet (cuisine ouverte, douche italienne)',
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
