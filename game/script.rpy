
define a = Character("Moi", color="#24C5EE")
define b = Character("Julia", color="#3124ee")
define c = Character("Lou", color ="#CA29D5")
define d = Character("Daniel", color="#D51515")
define e = Character("Sam", color="#FA7C00")
define f = Character("Frérot", color="#00fa7c")
define g = Character("Dr. Ysp", color="#fdfffe")
image a = im.Scale("Sprite F PinkH Professional Neutral01.png", 1050, 1350)
image b = im.Scale("Alice_Default.png", 500, 800)
image c = im.Scale("Eve_Neutral.png", 500, 800)
image d = im.Scale("Sprite Male Dark Hair Neu01.png", 1000, 1350)
image e = im.Scale("Male_Neutral.png", 750, 1250)
image g = im.Scale("5_normal.png", 850, 1000)
image b happy = im.Scale("Alice_Happy.png", 500, 800)
image c happy = im.Scale("Eve_Smile.png", 500, 800)
image d happy = im.Scale("Sprite Male Dark Hair Smi01.png", 1000, 1350)
image e happy = im.Scale("Male_Smile.png", 750, 1250)
image c laughing = im.Scale("Eve_Laugh.png", 500, 800)
image d laughing = im.Scale("Sprite Male Dark Hair Smi02.png", 1000, 1350)
image e laughing = im.Scale("Male_Happy.png", 750, 1250)
image b annoyed = im.Scale("Alice_Doubt.png", 500, 800)
image c annoyed = im.Scale("Eve_Angry.jpg", 500, 800)
image d annoyed = im.Scale("Sprite Male Dark Hair Ann01.png", 1000, 1350)
image e annoyed = im.Scale("Male_Angry.png", 750, 1250)
image d sport = im.Scale("Sprite Male Dark Hair Sport.png", 1000, 1350)
image e sport = im.Scale("Male_Neutral_sport.png", 750, 1250)
image b sad = im.Scale("Alice_Worried.png", 500, 800)
image e blush= im.Scale("Male_Blush.png", 750, 1250)
image cabinet_psy = Transform("cabinet.jpg", zoom=3, xoffset=-200)


init:
    $ Fe = 0
    $ Fi = 0
    $ Ne = 0
    $ Ni = 0
    $ Se = 0
    $ Si = 0
    $ Te = 0
    $ Ti = 0



screen debut_message1():
    text "Pour vivre pleinement cette expérience, nous vous conseillons de sélectionner les réponses qui corresponderaient le plus à votre manière d'agir/de penser si vous étiez confrontés à des situations similaires." size 100 color "#FFFFFF" xalign 0.5 yalign 0.5

screen debut_message2():
    text "Commençons" size 100 color "#FFFFFF" xalign 0.5 yalign 0.5


label start:
    show screen debut_message1
    $ renpy.pause()
    hide screen debut_message1
    show screen debut_message2
    $ renpy.pause()
    hide screen debut_message2
    jump debut
    

label debut:
    "???" "On est arrivés !"
    play music "music_base.mp3"
    scene interieur_voiture
    show a:
        xalign 0.5
        yalign -0.5
    "{i}La voix de ton ami te réveille en sursaut d'un rêve dont tu ne te souviens déjà plus.{\i}"
    "{i}Tu t'es endormie malgré toi pendant le trajet.{\i}"
    $ player_name = renpy.input("Quel est ton nom ?", default= "Alice")
    $ player_name = player_name.strip()
    if player_name == "" :
        $ player_name="Alice"
    scene chalet
    "{i}Vous êtes en effet arrivés devant le chalet de %(d)s. On voit que ses parents ont les moyens.{\i}"
    "{i}%(b)s finit de se parquer et vous descendez tous de sa voiture.{\i}"
    show b 
    b "Alors, bien dormi ?"
    a "Oui oui, j'aurais bien voulu discuter avec vous pendant le trajet mais j'étais trop crevée."
    b "C'est ça de se coucher à pas d'heure."
    menu choix_E :
        a "Oui mais je devais finir un projet ..."
        "Un de mes partenaire pour un projet s'y est pris à la dernière minute et j'ai du l'aider.":
            $ Te += 1
            $ Fe += 1
            b "Ha je vois, jamais facile les travaux de groupe."
            jump Fe_Te
        "Je n'arrive pas à me motiver à faire les choses à l'avance et j'ai du rush pour finir à temps.":
            $ Se += 1
            $ Ne += 1
            b "Tant que tu arrives à finir dans les temps ma foi."
            jump Ne_Se
label Fe_Te:
    "{i}Vous rejoignez %(c)s, %(d)s et %(e)s qui sont déjà en train de déverrouiller la porte.{\i}"
    scene interieur_chalet:
        zoom 1.75
    play music "music_games.mp3"
    "{i}Vous entrez encombrés de vos affaires.{\i}"
    show b:
        xalign 0.0
        yalign 1.0
    show c:
        xalign 0.33
        yalign 1.0
    show d:
        xpos 700
        ypos 200
    show e:
        xpos 1250
        ypos 150 
    "{i}À tes côtés se trouvent tes 4 meilleurs amis %(b)s, %(c)s, %(d)s et %(e)s avec qui tu as prévu de passer le week-end.{\i}"
    "{i}Vous vous êtes tous globalement rencontrés pendant votre scolarité quelques années auparavant et vous vous voyez régulièrement depuis.{\i}"
    hide b
    hide c
    hide d
    hide e
    show b
    "{i}%(b)s, toujours pleine de nouvelles idées à essayer et parle beaucoup. Elle se fait facilement de nouveaux amis et adore discuter avec tout le monde.{\i}"
    show c
    hide b
    "{i}%(c)s on ne sait pas souvent ce qu'elle pense mais quand elle s'exprime c'est souvent pour prédire quelque chose que personne d'autre n'avait vu venir. Elle adore expliquer aux gens ses dernières lubies. Elle rafole des chats.{\i}"
    show d:
        xpos 500
        ypos 200
    hide c
    "{i}%(d)s adore apprendre, surtout des choses qu'il peut concrétiser. Il aime beaucoup le sport, les sensations fortes et sait apprécier la bonne nourriture.{\i}"
    show e:
        xpos 600
        ypos 150 
    hide d
    "{i}%(e)s sait mettre la bonne ambiance dans un groupe. Il est toujours là pour aider s'il y a un problème. Il se plie d'ailleurs un peu trop en quatre par moments.{\i}"
    hide e
    "{i}Vous dirigez vers les chambres pour tout déposer.{\i}"
    scene chambre:
        zoom 1.2
    "{i}Il y a 3 chambres de 2 et tu te rends compte que %(d)s et %(e)s se sont mis d'accords pour dormir dans la même chambre pendant le trajet en voiture alors que tu dormais.{\i}"
    "{i}De son côté, %(c)s a déjà dit qu'elle irait dans une autre chambre que %(b)s.{\i}"
    "{i}Ceux qui n'ont jamais dormi avec %(b)s pourraient se demander pourquoi %(c)s s'est empressée de choisir une autre chambre.{\i}"
    "{i}La raison est simple; %(b)s ronfle comme un camion.{\i}"
    "{i}D'ailleurs, ça ne dérange pas %(c)s de dormir seule contrairement à %(b)s.{\i}"
    "{i}Car oui, en plus de faire le bruit d'une locomotive, tu sais très bien depuis le temps que tu la connais, que %(b)s se sent facilement rejettée et aime dormir avec quelqu'un dans la même pièce.{\i}"
    "{i}Bien sûr tu sais que c'est platoniquement, après tout vous êtes amies depuis des années et en plus ce sont des lits simples.{\i}"
    "{i}Ton manque de sommeil de la nuit passée picotte quand même un peu et tu n'es pas la personne avec le sommeil le plus lourd.{\i}"
    "{i}Ce week-end est sensé être un week-end de repos pour tous. Tu te sens un peu dupée que tes amis ait profité de discuter de ce sujet sans toi.{\i}"
    "{i}Tu es debout au milieu du couloir, juste à côté des chambres où vont dormir tes amis.{\i}"
    show b 
    "{i}%(b)s n'a même pas encore posé son sac qu'elle revient sur le seuil de la chambre qu'elle va occuper.{\i}"
    menu choix_Fe_Te :
        b "Tu veux venir dormir avec moi %(player_name)s ou tu vas dormir avec %(c)s ?"
        "{i}Si elle ne ronflait pas, tu aurais bien voulu lui faire plaisir mais elle peut survivre à dormir seule. Vous allez de toute façon passer le plus clair de votre temps les 5.{\i}":
            $ Te += 1
            a "Désolée je vais dormir avec %(c)s, j'ai besoin de rattraper du sommeil cette nuit !"
            show b sad
            b "Oh pas de soucis, je comprends tout à fait. C'est vrai que je ronfle beaucoup."
            hide b sad 
            jump Te_i
        "{i}Tu devrais pouvoir survivre à ce bruit infernal. Au pire tu peux essayer de trouver des boules quies. C'est toujours bien de rendre heureux les gens même si c'est avec de petits sacrifices.{\i}":
            $ Fe += 1
            a "Je viens avec toi comme ça je te tiens un peu compagnie, je sais que tu aimes bien."
            show b happy
            b "Oh trop bien ! Je te laisse choisir ton lit !"
            hide b happy
            jump Fe_i

label Ne_Se:
    "{i}Vous rejoignez %(c)s, %(d)s et %(e)s qui sont déjà en train de déverrouiller la porte.{\i}"
    scene interieur_chalet:
        zoom 1.75
    play music "music_games.mp3"
    "{i}Vous entrez encombrés de vos affaires.{\i}"
    show b:
        xalign 0.0
        yalign 1.0
    show c:
        xalign 0.33
        yalign 1.0
    show d:
        xpos 700
        ypos 200
    show e:
        xpos 1250
        ypos 150 
    "{i}À tes côtés se trouvent tes 4 meilleurs amis %(b)s, %(c)s, %(d)s et %(e)s avec qui tu as prévu de passer le week-end.{\i}"
    "{i}Vous vous êtes tous globalement rencontrés pendant votre scolarité quelques années auparavant et vous vous voyez régulièrement depuis.{\i}"
    hide b
    hide c
    hide d
    hide e
    show b
    "{i}%(b)s, toujours pleine de nouvelles idées à essayer et parle beaucoup. Elle se fait facilement de nouveaux amis et adore discuter avec tout le monde.{\i}"
    show c
    hide b
    "{i}%(c)s on ne sait pas souvent ce qu'elle pense mais quand elle s'exprime c'est souvent pour prédire quelque chose que personne d'autre n'avait vu venir. Elle adore expliquer aux gens ses dernières lubies. Elle rafole des chats.{\i}"
    show d:
        xpos 500
        ypos 200
    hide c
    "{i}%(d)s adore apprendre, surtout des choses qu'il peut concrétiser. Il aime beaucoup le sport, les sensations fortes et sait apprécier la bonne nourriture.{\i}"
    show e:
        xpos 600
        ypos 150 
    hide d
    "{i}%(e)s sait mettre la bonne ambiance dans un groupe. Il est toujours là pour aider s'il y a un problème. Il se plie d'ailleurs un peu trop en quatre par moments.{\i}"
    hide e
    "{i}Vous dirigez vers les chambres pour tout déposer.{\i}"
    scene chambre:
        zoom 1.2
    "{i}Après avoir posé tes affaires, tu te rends dans la cuisine pour retrouver les 4 autres.{\i}"
    scene cuisine_chalet:
        zoom 0.75
    show b:
        xalign 0.0
        yalign 1.0
    show c:
        xalign 0.33
        yalign 1.0
    show d:
        xpos 700
        ypos 200
    show e:
        xpos 1250
        ypos 150 
    "{i}Une fois réunis, vous sortez les commissions des sacs que vous aviez laissés à la cuisine et vous rangez tout excepté les pizzas que vous mettez au four.{\i}"
    e "Bon, on avait pas vraiment décidé de ce qu'on allait faire cet après-midi, vous auriez une idée ou une envie particulière ?"
    d "Je vais aller me dégourdir un peu les jambes, il paraît qu'il y a une superbe vue à quelques minutes d'ici, je pensais prendre des photos. Ha et je pensais en profiter pour passer à l'expo d'art au centre-ville en même temps."
    e "Bonne idée, je viens avec toi."
    c "Je peux profiter de ce moment pour te montrer le powerpoint dont je t'avais parlé %(b)s. C'est une présentation sur certains principes de chimie et physique amusants que j'ai pu observer au cours de cette année, notamment dans les films que j'ai vu, si ça intéresse quelqu'un d'autre vous êtes les bienvenus."
    c "Je dois faire des retours à un de mes amis auquel j'avais déjà fait la présentation, ça pourrait être l'occasion de vous le présenter un de ces jours."
    menu Fe_dom_Se_dom :
        "{i}Que fais-tu de ton temps libre cet après-midi ?{\i}"
        "J'ai bien envie de me défouler un petit peu et voir la vue et l'expo, je vais avec %(d)s et %(e)s.":
            $ Se += 1
            jump Se_i
        "J'aime bien apprendre sur différents sujets aléatoires, en plus si cela permet de rencontrer l'ami de %(c)s un jour ça a l'air amusant.":
            $ Ne += 1
            jump Ne_i


label Te_i :
    "{i}Après avoir posé tes affaires, tu te rends dans la cuisine pour retrouver les 4 autres.{\i}"
    scene cuisine_chalet:
        zoom 0.75
    show b:
        xalign 0.0
        yalign 1.0
    show c:
        xalign 0.33
        yalign 1.0
    show d:
        xpos 700
        ypos 200
    show e:
        xpos 1250
        ypos 150 
    "{i}Une fois réunis, vous sortez les commissions des sacs que vous aviez laissés à la cuisine et vous rangez tout excepté les pizzas que vous mettez au four.{\i}"
    e "Bon, on avait dit qu'on faisait des jeux il me semble ? Tu as pensé à les prendre %(b)s ?"
    b "Mais bien sûr ! Pour qui tu me prends ?"
    hide b
    "{i}%(b)s part en direction des chambres.{\i}"
    c "Je lui ai envoyé un message hier soir pour lui rappeler de les mettre dans son sac, elle avait complétement oublié."
    show d laughing:
        xpos 700
        ypos 200
    d "ça m'étonne pas !"
    show d:
        xpos 700
        ypos 200
    show b:
        xalign 0.0
        yalign 1.0
    "{i}%(b)s revient, les bras chargés de jeux et nous nous rendons tous au salon.{\i}"
    scene salon_chalet:
        zoom 1.1
    show b:
        xalign 0.0
        yalign 1.0
    show c:
        xalign 0.33
        yalign 1.0
    show d:
        xpos 700
        ypos 200
    show e:
        xpos 1250
        ypos 150 
    "{i}Après un quart d'heure de débat, et la disposition des tranches de pizza fumantes sur le bord de la table du salon sur laquelle vous allez jouer,vous hésitez entre 2 jeux.{\i}"
    "{i}Le premier est un jeu auquel vous avez l'habitude de jouer lorsque vous faites des week-ends les 5 et qui vous a toujours fait passer de très bons moments.{\i}"
    "{i}Le second est un nouveau jeu que %(b)s s'est procuré et veut tester avec vous.{\i}"
    "{i}Vous avez le temps de faire les 2 à la suite, après faut-il encore avoir la motivation et l'énergie après avoir appris de nouvelles règles.{\i}"
    b "Allez, j'ai déjà lu le manuel ! Je peux tout vous expliquer, ce sera pas court mais pas interminable non plus ! ça a l'air super chouette !"
    c "ça me va de faire un nouveau jeu. On pourra faire l'autre après au pire."
    e "J'aurais quand même envie de jouer à l'autre moi perso, c'est un peu notre tradition ! Je pense pas que j'aurai la motivation de faire 2 gros jeux à la suite."
    d "Yeah, un jeu qu'on connaît déjà me tente plus."
    menu Te_Ni_Si :
        "{i}Tes 4 amis te regardent alors. Ils sont arrivés à une égalité, tu vas devoir trancher %(player_name)s.{\i}"
        "Go pour le nouveau jeu, j'aime bien découvrir de nouvelles choses.":
            $ Ni += 1
            jump Te_Ni
            b "Ha je vois, jamais facile les travaux de groupe."
        "Je préfère le jeu auquel on est habitués. On ne sait même pas si l'autre va nous plaire.":
            $ Si += 1
            jump Te_Si

label Fe_i :
    "{i}Après avoir posé tes affaires, tu te rends dans la cuisine pour retrouver les 4 autres.{\i}"
    scene cuisine_chalet:
        zoom 0.75
    show b:
        xalign 0.0
        yalign 1.0
    show c:
        xalign 0.33
        yalign 1.0
    show d:
        xpos 700
        ypos 200
    show e:
        xpos 1250
        ypos 150 
    "{i}Une fois réunis, vous sortez les commissions des sacs que vous aviez laissés à la cuisine et vous rangez tout excepté les pizzas que vous mettez au four.{\i}"
    e "Bon, on avait dit qu'on faisait des jeux il me semble ? Tu as pensé à les prendre %(b)s ?"
    b "Mais bien sûr ! Pour qui tu me prends ?"
    hide b
    "{i}%(b)s part en direction de votre chambre.{\i}"
    c "Je lui ai envoyé un message hier soir pour lui rappeler de les mettre dans son sac, elle avait complétement oublié."
    show d laughing:
        xpos 700
        ypos 200
    d "ça m'étonne pas !"
    show d:
        xpos 700
        ypos 200
    show b:
        xalign 0.0
        yalign 1.0
    "{i}%(b)s revient, les bras chargés de jeux et nous nous rendons tous au salon.{\i}"
    scene salon_chalet:
        zoom 1.1
    show b:
        xalign 0.0
        yalign 1.0
    show c:
        xalign 0.33
        yalign 1.0
    show d:
        xpos 700
        ypos 200
    show e:
        xpos 1250
        ypos 150 
    "{i}Après un quart d'heure de débat, et la disposition des tranches de pizza fumantes sur le bord de la table du salon sur laquelle vous allez jouer,vous hésitez entre 2 jeux.{\i}"
    "{i}Le premier est un jeu auquel vous avez l'habitude de jouer lorsque vous faites des week-ends les 5 et qui vous a toujours fait passer de très bons moments.{\i}"
    "{i}Le second est un nouveau jeu que %(b)s s'est procuré et veut tester avec vous.{\i}"
    "{i}Vous avez le temps de faire les 2 à la suite, après faut-il encore avoir la motivation et l'énergie après avoir appris de nouvelles règles.{\i}"
    b "Allez, j'ai déjà lu le manuel ! Je peux tout vous expliquer, ce sera pas court mais pas interminable non plus ! ça a l'air super chouette !"
    c "ça me va de faire un nouveau jeu. On pourra faire l'autre après au pire."
    e "J'aurais quand même envie de jouer à l'autre moi perso, c'est un peu notre tradition ! Je pense pas que j'aurai la motivation de faire 2 gros jeux à la suite."
    d "Yeah, un jeu qu'on connaît déjà me tente plus."
    menu Fe_Ni_Si :
        "{i}Tes 4 amis te regardent alors. Ils sont arrivés à une égalité, tu vas devoir trancher %(player_name)s.{\i}"
        "Go pour le nouveau jeu, j'aime bien découvrir de nouvelles choses.":
            $ Ni += 1
            jump Fe_Ni
            b "Ha je vois, jamais facile les travaux de groupe."
        "Je préfère le jeu auquel on est habitués. On ne sait même pas si l'autre va nous plaire.":
            $ Si += 1
            jump Fe_Si



label Te_Ni:
    show b happy:
        xalign 0.0
        yalign 1.0
    show c:
        xalign 0.33
        yalign 1.0
    show d:
        xpos 700
        ypos 200
    show e annoyed:
        xpos 1250
        ypos 150 
    b "Yeah trop bien !"
    "{i} %(b)s commence avec enthousiasme à expliquer les règles tout en mettant le matériel en place. Après une trentaine de minutes, nous sommes briefés sur les règles et les hostilités commencent.{\i}"
    show e happy:
        xpos 1250
        ypos 150 
    show c happy
    show d happy:
        xpos 700
        ypos 200
    "{i}%(e)s qui n'était pas favorable à ce choix de jeu se retrouve pourtant très investi et finit par remporter la partie.{\i}"
    b "Vous voyez que ce jeu valait la peine !"
    show b:
        xalign 0.0
        yalign 1.0
    show c:
        xalign 0.33
        yalign 1.0
    show d:
        xpos 700
        ypos 200
    show e:
        xpos 1250
        ypos 150 
    "{i}Nous nous affairons tous à ranger le jeu. Une fois cela fait, je regarde ma montre; il est 18h.{\i}"
    d "Je vais aller faire un petit peu de sport avant le repas moi. On se rejoint à 19h ?"
    e "Bonne idée, je vais venir avec toi ça va me faire du bien."
    c "Je peux profiter de ce moment pour te faire tester le nouveau test de personnalité que j'ai découvert."
    b "C'est parti ! On peut faire un peu en même temps et essayer de deviner ce qu'aurait mis l'autre !"
    menu Te_dom_Ni_dom :
        "{i}Que fais-tu de ton temps libre avant le repas ?{\i}"
        "J'ai bien envie de me défouler un petit peu, je viens avec vous %(d)s et %(e)s.":
            $ Te += 1
            jump fin
        "Je veux bien tester ton test de personnalité aussi %(c)s.":
            $ Ni += 1
            jump fin

label Fe_Ni:
    show b happy:
        xalign 0.0
        yalign 1.0
    show c:
        xalign 0.33
        yalign 1.0
    show d:
        xpos 700
        ypos 200
    show e annoyed:
        xpos 1250
        ypos 150 
    b "Yeah trop bien !"
    "{i} %(b)s commence avec enthousiasme à expliquer les règles tout en mettant le matériel en place. Après une trentaine de minutes, nous sommes briefés sur les règles et les hostilités commencent.{\i}"
    show e happy:
        xpos 1250
        ypos 150 
    show c happy
    show d happy:
        xpos 700
        ypos 200
    "{i}%(e)s qui n'était pas favorable à ce choix de jeu se retrouve pourtant très investi et finit par remporter la partie.{\i}"
    b "Vous voyez que ce jeu valait la peine !"
    show b:
        xalign 0.0
        yalign 1.0
    show c:
        xalign 0.33
        yalign 1.0
    show d:
        xpos 700
        ypos 200
    show e:
        xpos 1250
        ypos 150 
    "{i}Nous nous affairons tous à ranger le jeu. Une fois cela fait, je regarde ma montre; il est 18h.{\i}"
    d "Je vais aller faire un petit peu de sport avant le repas moi. On se rejoint à 19h ?"
    e "Bonne idée, je vais venir avec toi ça va me faire du bien."
    c "Je peux profiter de ce moment pour te montrer le powerpoint dont je t'avais parlé %(b)s. C'est une présentation sur certains principes de chimie et physique amusants que j'ai pu observer au cours de cette année, notamment dans les films que j'ai vu, si ça intéresse quelqu'un d'autre vous êtes les bienvenus."
    menu Fe_dom_Ni_dom :
        "{i}Que fais-tu de ton temps libre avant le repas ?{\i}"
        "J'ai bien envie de me défouler un petit peu, je viens avec vous %(d)s et %(e)s.":
            $ Fe += 1
            jump fin
        "Tout nouveau savoir est bon à prendre, je viens suivre ta présentation %(c)s.":
            $ Ni += 1
            jump fin

label Te_Si:
    show b annoyed:
        xalign 0.0
        yalign 1.0
    show c:
        xalign 0.33
        yalign 1.0
    show d:
        xpos 700
        ypos 200
    show e happy:
        xpos 1250
        ypos 150 
    b "Bon d'accord..."
    "{i}%(b)s râle mais déballe le jeu sur la table. Après quelques minutes, tout est en place et le jeu peut commencer.{\i}"
    show b happy
    show c happy
    show d happy:
        xpos 700
        ypos 200
    "{i}Tout le monde passe un très bon moment, ce qui n'est pas une surprise avec ce jeu.{\i}"
    "{i}Même %(b)s semble résignée sur le fait de tester son jeu un autre jour.{\i}"
    e "On s'en lasse définitivement pas !"
    d "Mouais, on aurait peut-être du jouer à l'autre jeu au final."
    show c laughing
    c "Tu dis ça juste parce que t'es dernier !"
    "{i}Ce ne fut effectivement pas %(d)s qui gagna la partie.{\i}"
    show b:
        xalign 0.0
        yalign 1.0
    show c:
        xalign 0.33
        yalign 1.0
    show d:
        xpos 700
        ypos 200
    show e:
        xpos 1250
        ypos 150 
    "{i}Nous nous affairons tous à ranger le jeu. Une fois cela fait, nous sortons quelques paquets de chips et des bières.{\i}"
    "{i}Il n'y a pas que le jeu auquel nous venons de jouer qui soit dans les habitudes de nos sorties au chalet.{\i}"
    "{i}Après une heure que nous passons à discuter et boire, nous lançons un jeu d'alcool.{\i}"
    "{i}Nous tirons à tour de rôle des cartes vérité que nous posons à notre voisin de gauche.{\i}"
    "{i}C'était au tour de %(e)s de répondre.{\i}"
    "{i}%(d)s avait posé une question sur à propos de qui dans la pièce il avait déjà fait un rêve érotique %(e)s avait refusé de répondre.{\i}"
    show e blush:
        xpos 1250
        ypos 150 
    "{i}%e(e)s but honteusement avant de tirer une carte pour me poser une question.{\i}"
    show e:
        xpos 1250
        ypos 150 
    menu Te_dom_Si_dom :
        e "Comment réagirais-tu si nous étions tous dans le même groupe pour un projet, voudrais-tu être le chef ?"
        "{i}Je serai probablement la personne la plus appropriée pour être le leader, je sais m'assurer que tout le monde fasse sa part et que tout soit rendu dans les temps.{\i}":
            $ Te += 1
            jump fin
        "{i}Si on me désigne, je veux bien en assumer la charge car je sais que j'en suis capable mais je ne me proposerai pas moi-même.Être bras droit et surveiller me va bien aussi.{\i}":
            $ Si += 1
            jump fin

label Fe_Si:
    show b annoyed:
        xalign 0.0
        yalign 1.0
    show c:
        xalign 0.33
        yalign 1.0
    show d:
        xpos 700
        ypos 200
    show e happy:
        xpos 1250
        ypos 150 
    b "Bon d'accord..."
    "{i}%(b)s râle mais déballe le jeu sur la table. Après quelques minutes, tout est en place et le jeu peut commencer.{\i}"
    show b happy
    show c happy
    show d happy:
        xpos 700
        ypos 200
    "{i}Tout le monde passe un très bon moment, ce qui n'est pas une surprise avec ce jeu.{\i}"
    "{i}Même %(b)s semble résignée sur le fait de tester son jeu un autre jour.{\i}"
    e "On s'en lasse définitivement pas !"
    d "Mouais, on aurait peut-être du jouer à l'autre jeu au final."
    show c laughing
    c "Tu dis ça juste parce que t'es dernier !"
    "{i}Ce ne fut effectivement pas %(d)s qui gagna la partie.{\i}"
    show b:
        xalign 0.0
        yalign 1.0
    show c:
        xalign 0.33
        yalign 1.0
    show d:
        xpos 700
        ypos 200
    show e:
        xpos 1250
        ypos 150 
    "{i}Nous nous affairons tous à ranger le jeu. Une fois cela fait, nous sortons quelques paquets de chips et des bières.{\i}"
    "{i}Il n'y a pas que le jeu auquel nous venons de jouer qui soit dans les habitudes de nos sorties au chalet.{\i}"
    "{i}Après une heure que nous passons à discuter et boire, nous lançons un jeu d'alcool.{\i}"
    "{i}Nous tirons à tour de rôle des cartes vérité que nous posons à notre voisin de gauche.{\i}"
    "{i}C'était au tour de %(e)s de répondre.{\i}"
    "{i}%(d)s avait posé une question sur à propos de qui dans la pièce il avait déjà fait un rêve érotique %(e)s avait refusé de répondre.{\i}"
    show e blush:
        xpos 1250
        ypos 150 
    "{i}%(e)s but honteusement avant de tirer une carte pour me poser une question.{\i}"
    show e:
        xpos 1250
        ypos 150 
    menu Fe_dom_Si_dom :
        e "Trouves-tu que tu es souvent la personne qui alimente les conversations lorsque tu fais des sorties avec des gens ?"
        "Je suis assez à l'aise pour trouver des sujets à aborder. Je peux parler avec n'importe qui s'il le faut. Cela ne m'empêche pas d'être là pour écouter aussi ce que les autres ont à dire.":
            $ Fe += 1
            jump fin
        "On me qualifie plutôt de personne à l'écoute. Je n'ai pas les rudiments pour faire du small talk efficacement et la conversation risque vite de mourir si on compte sur moi si je ne connais pas bien la personne.":
            $ Si += 1
            jump fin




    


label Ne_i:
    show b :
        xalign 0.0
        yalign 1.0
    show c:
        xalign 0.33
        yalign 1.0
    hide d
    hide e 
    "{i}%(d)s et %(e)s partent en direction des chambres pour se préparer pour le centre-ville.{\i}"
    "{i}%(c)s sort une clef USB de sa poche et la plante directement dans la TV du salon.{\i}"
    "{i}Le powerpoint semble intéressant et commence par une introduction à la physique dans Star Wars.{\i}"
    "{i}Ensuite, cela disgressa sur les films Aliens et autres films de science-fiction.{\i}" 
    "{i}La présentation était intéressante et tu as appris plein de nouveaux faits hasardeux.{\i}"
    "{i}Comme un nouveau sujet n'a pas été lancé, tu sens que tu peux orienter la suite comme tu le souhaites.{\i}"
    "{i}Tu hésites à demander un peu des nouvelles de la vie sentimentale de tes amies ou poser des questions sur certains principes qu'à expliquer %(c)s.{\i}"
    "{i}En effet, %(e)s intimide un peu %(b)s sur ce genre de sujet car ils ont une relation fut un temps.{\i}"
    "{i}D'un autre côté tu as plein de questions à poser et vous devez gentiment vous préparer car vous avez prévu d'aller voir un film au cinéma d'à côté.{\i}"
    menu Ne_Fi_Ti :
        "{i}Que préfères-tu demander ?{\i}"
        "Je préfère avoir les ragôts de la vie sentimentale de mes amis. Je reste une romantique dans l'âme.":
            $ Fi += 1
            jump Ne_Fi
        "Je veux pouvoir poser mes questions. C'est plus important d'étendre mes connaissances, en plus, les sentiments ça change bien vite.":
            $ Ti += 1
            jump Ne_Ti

label Se_i:
    scene chambre
    "{i}Vous partez en direction des chambres pour vous préparer pour le centre-ville.{\i}"
    "{i}Une fois les affaires que vous vouliez prises, vous vous mettez en route.{\i}"
    scene vue
    "{i}Vous vous rendez tout d'abord à un endroit offrant une vue dégagée de la plaine en contrebas, c'est magnifique.{\i}"
    "{i}Après avoir profité de la vue quelques instants, vous rejoignez le centre ville et atteignez l'expo d'art qui est dans un musée.{\i}"
    scene art :
        zoom 1.5
    "{i}Un homme connaisseur vous fait la visite en vous abreuvant de faits tous les plus intéressants les uns que les autres.{\i}"
    "{i}Une fois le tour terminé, il retourne derrière son guichet.{\i}"
    "{i}Comme un nouveau sujet n'a pas été lancé par tes compagnons, tu sens que tu peux orienter la suite comme tu le souhaites.{\i}"
    "{i}Tu hésites à demander un peu des nouvelles de la vie sentimentale de tes amis ou poser des questions sur certains principes qu'à expliquer le gardien du musée.{\i}"
    "{i}En effet, %(e)s a eu une relation avec %(b)s fut un temps et tu n'avais jamais trop pu lui poser des questions sur le sujet.{\i}"
    "{i}D'un autre côté tu as plein de questions à poser à celui qui gère le musée et vous devez gentiment partir car vous avez prévu d'aller voir un film au cinéma d'à côté avec le reste de l'équipe qui va vous rejoindre.{\i}"
    menu Se_Fi_Ti :
        "{i}Que préfères-tu demander ?{\i}"
        "Je préfère avoir les ragôts de la vie sentimentale de mes amis. Je reste une romantique dans l'âme.":
            $ Fi += 1
            jump Se_Fi
        "Je veux pouvoir poser mes questions. C'est plus important d'étendre mes connaissances, en plus, les sentiments ça change bien vite.":
            $ Ti += 1
            jump Se_Ti

label Ne_Fi:
    show b :
        xalign 0.0
        yalign 1.0
    show c:
        xalign 0.33
        yalign 1.0
    "{i}Après avoir papoté avec les filles, tu apprends que %(b)s a une relation secrète à distance avec une fille de son âge.{\i}"
    "{i}Elle te raconte les avantages et inconvénients, tu arrives bien à te projeter dans ce qu'elle te dit et pense que son avis pourrait être utile si tu te lances dans une relation du style un jour.{\i}"
    "{i}Vous vous préparez alors pour aller au cinéma et sortez en ville rejoindre le reste de la troupe.{\i}"
    scene cinema:
        zoom 1.5
    "{i}Vous retrouvez les autres à l'heure convenue et vous vous rendez dans la salle.{\i}"
    "{i}Une fois assis, vous piquez du popcorn chez votre voisine de droite %(c)s et réalisez qu'il s'agit de popcorn sucré.{\i}"
    "{i}Vous vous rappelez qu'elle avait spécifié qu'elle les voulait salé et vous savez qu'elle n'aime pas les sucrés.{\i}"
    "{i}%(c)s devine le fond de ta pensée.{\i}"
    c "Y a aucun soucis je t'assure, je peux vous en donner plus comme ça."
    menu Ne_dom_Fi_dom:
        "{i}Vous ne pouvez pas laisser passer ça, après vous savez que %(e)s n'a aucune gêne à aller réclamer des choses, surtout pour rendre service.{\i}"
        "{i}Moi non plus ça ne me dérange pas, je vais y aller de ce pas, pas besoin de demander à %(e)s.{\i}":
            $ Ne += 1
            jump fin
        "{i}Si %(e)s n'était pas là je serais aller moi mais comme il est là et que lui ça ne le dérange absolument pas, je vais lui demander.{\i}":
            $ Fi += 1
            jump fin
    

label Se_Fi:
    "{i}Après avoir papoté avec les garçons, tu apprends que %(e)s a toujours des sentiments pour %(b)s et espère bien la reconquérir.{\i}"
    "{i}Il te raconte un peu les stratagèmes qu'il emploie et tu lui demandes de te faire des retours sur leur efficacité.{\i}"
    "{i}Vous vous préparez alors pour aller au cinéma et sortez du musée pour rejoindre le reste de la troupe.{\i}"
    scene cinema:
        zoom 1.5
    "{i}Vous retrouvez les autres à l'heure convenue et vous vous rendez dans la salle.{\i}"
    "{i}Une fois assis, vous piquez du popcorn chez votre voisine de droite %(c)s et réalisez qu'il s'agit de popcorn sucré.{\i}"
    "{i}Vous vous rappelez qu'elle avait spécifié qu'elle les voulait salé et vous savez qu'elle n'aime pas les sucrés.{\i}"
    "{i}%(c)s devine le fond de ta pensée.{\i}"
    c "Y a aucun soucis je t'assure, je peux vous en donner plus comme ça."
    menu Se_dom_Fi_dom:
        "{i}Vous ne pouvez pas laisser passer ça, après vous savez que %(e)s n'a aucune gêne à aller réclamer des choses, surtout pour rendre service.{\i}"
        "{i}Moi non plus ça ne me dérange pas, je vais y aller de ce pas, pas besoin de demander à %(e)s.{\i}":
            $ Se += 1
            jump fin
        "{i}Si %(e)s n'était pas là je serais aller moi mais comme il est là et que lui ça ne le dérange absolument pas, je vais lui demander.{\i}":
            $ Fi += 1
            jump fin



label Ne_Ti:
    "{i}Vous posez toutes les questions qui vous trottent dans la tête à propos de la présentation que vous venez de suivre.{\i}"
    "{i}Vous vous y prenez si bien que vous parvenez même à obtenir le numéro de l'ami de %(c)s, qui est en fait chercheur, pour lui poser des questions approfondies en physique.{\i}"
    "{i}Vous vous préparez alors pour aller au cinéma et sortez du musée pour rejoindre le reste de la troupe.{\i}"
    scene cinema:
        zoom 1.5
    "{i}Vous retrouvez les autres à l'heure convenue et vous vous rendez dans la salle.{\i}"
    "{i}Une fois assis, vous piquez du popcorn chez votre voisine de droite %(c)s et réalisez qu'il s'agit de popcorn sucré.{\i}"
    "{i}Vous vous rappelez qu'elle avait spécifié qu'elle les voulait salé et vous savez qu'elle n'aime pas les sucrés.{\i}"
    "{i}%(c)s devine le fond de ta pensée.{\i}"
    c "Y a aucun soucis je t'assure, je peux vous en donner plus comme ça."
    menu Ne_dom_Ti_dom:
        "{i}Vous ne pouvez décemment pas laisser votre amie dans un tel embarras, après vous savez que %(e)s n'a aucune gêne à aller réclamer des choses, surtout pour rendre service.{\i}"
        "{i}Moi non plus ça ne me dérange pas, je vais y aller de ce pas, pas besoin de demander à %(e)s.{\i}":
            $ Ne += 1
            jump fin
        "{i}Si %(e)s n'était pas là je serais aller moi mais comme il est là et que lui ça ne le dérange absolument pas, je vais lui demander.{\i}":
            $ Ti += 1
            jump fin

label Se_Ti:
    "{i}Vous posez toutes les questions qui vous trottent dans la tête au gardien à propos du tour guidé que vous venez de suivre.{\i}"
    "{i}Vous vous y prenez si bien qu'il vous offre différents billets et réductions pour d'autres expositions dans la région. Entre passionnés on se comprend !{\i}"
    "{i}Vous vous préparez alors pour aller au cinéma et sortez du musée pour rejoindre le reste de la troupe.{\i}"
    scene cinema:
        zoom 1.5
    "{i}Vous retrouvez les autres à l'heure convenue et vous vous rendez dans la salle.{\i}"
    "{i}Une fois assis, vous piquez du popcorn chez votre voisine de droite %(c)s et réalisez qu'il s'agit de popcorn sucré.{\i}"
    "{i}Vous vous rappelez qu'elle avait spécifié qu'elle les voulait salé et vous savez qu'elle n'aime pas les sucrés.{\i}"
    "{i}%(c)s devine le fond de ta pensée.{\i}"
    c "Y a aucun soucis je t'assure, je peux vous en donner plus comme ça."
    menu Se_dom_Ti_dom:
        "{i}Vous ne pouvez décemment pas laisser votre amie dans un tel embarras, après vous savez que %(e)s n'a aucune gêne à aller réclamer des choses, surtout pour rendre service.{\i}"
        "{i}Moi non plus ça ne me dérange pas, je vais y aller de ce pas, pas besoin de demander à %(e)s.{\i}":
            $ Se += 1
            jump fin
        "{i}Si %(e)s n'était pas là je serais aller moi mais comme il est là et que lui ça ne le dérange absolument pas, je vais lui demander.{\i}":
            $ Ti += 1
            jump fin






label fin :
    scene noir
    "{i}Ta vision se trouble tout à coup, tu sens l'espace qui t'environnait comme se dissoudre.{\i}"
    g "3,2,1, réveille-toi."
    scene cabinet_psy
    show g
    "{i}Tu rouvres les yeux, tu es face au Dr. Ysp dans son cabinet.{\i}"
    "{i}Tu viens de te rappeler que tu avais accepté d'être le sujet test d'une nouvelle expérience de mise sous hypnose qui consiste en une sorte d'aventure permettant de découvrir ta typologie d'après Jung.{\i}"
    g "Comme nous vous l'avons spécifié avant le début de l'expérience, le fameux test des 16 personnalités qui circule en ligne attribue souvent aux gens un type qui n'est pas le leur."
    g "En effet, le test ne pose pas forcément les questions de manières adéquates ou est trop biaisé pour certaines questions."
    g "Nous espérons avec notre nouvelle méthode obtenir de meilleurs résultats."
    g "Votre participation a cette étude nous est très précieuse, je vous remercie de votre collaboration."
    g "Sans plus de cérémonie, passons à vos résultats voulez-vous ?"
    if Fe>Ne and Fe>Ni and Fe>Se and Fe>Si and Fe>Te and Fe>Ti and Fe>Fi:
        if Ni>Si :
            "Vous êtes Fe dominant avec comme auxiliaires Ni et Se. Plus communément appelé ENFJ."
        if Si>Ni :
            "Vous êtes Fe dominant avec comme auxiliaires Si et Ne. Plus communément appelé ESFJ."
    if Te>Ne and Te>Ni and Te>Se and Te>Si and Te>Fe and Te>Ti and Te>Fi:
        if Ni>Si :
            "Vous êtes Te dominant avec comme auxiliaires Ni et Se. Plus communément appelé ENTJ."
        if Si>Ni :
            "Vous êtes Te dominant avec comme auxiliaires Si et Ne. Plus communément appelé ESTJ."
    if Ne>Te and Ne>Ni and Ne>Se and Ne>Si and Ne>Fe and Ne>Ti and Ne>Fi:
        if Fi>Ti :
            "Vous êtes Ne dominant avec comme auxiliaires Fi et Te. Plus communément appelé ENFP."
        if Ti>Fi :
            "Vous êtes Ne dominant avec comme auxiliaires Ti et Fe. Plus communément appelé ENTP."
    if Se>Te and Se>Ni and Se>Ne and Se>Si and Se>Fe and Se>Ti and Se>Fi:
        if Fi>Ti :
            "Vous êtes Se dominant avec comme auxiliaires Fi et Te. Plus communément appelé ESFP."
        if Ti>Fi :
            "Vous êtes Se dominant avec comme auxiliaires Ti et Fe. Plus communément appelé ESTP."
    if Si>Te and Si>Ni and Si>Ne and Si>Se and Si>Fe and Si>Ti and Si>Fi:
        if Fe>Te :
            "Vous êtes Si dominant avec comme auxiliaires Fe et Ti. Plus communément appelé ISFJ."
        if Te>Fe :
            "Vous êtes Si dominant avec comme auxiliaires Te et Fi. Plus communément appelé ISTJ."
    if Ni>Te and Ni>Si and Ni>Ne and Ni>Se and Ni>Fe and Ni>Ti and Ni>Fi:
        if Fe>Te :
            "Vous êtes Ni dominant avec comme auxiliaires Fe et Ti. Plus communément appelé INFJ."
        if Te>Fe :
            "Vous êtes Ni dominant avec comme auxiliaires Te et Fi. Plus communément appelé INTJ."
    if Ti>Te and Ti>Ni and Ti>Ne and Ti>Se and Ti>Fe and Ti>Si and Ti>Fi:
        if Se>Ne :
            "Vous êtes Ti dominant avec comme auxiliaires Se et Ni. Plus communément appelé ISTP."
        if Ne>Se :
            "Vous êtes Ti dominant avec comme auxiliaires Ne et Si. Plus communément appelé INTP."
    if Fi>Te and Fi>Ni and Fi>Ne and Fi>Se and Fi>Fe and Fi>Si and Fi>Ti:
        if Se>Ne :
            "Vous êtes Fi dominant avec comme auxiliaires Se et Ni. Plus communément appelé ISFP."
        if Ne>Se :
            "Vous êtes Fi dominant avec comme auxiliaires Ne et Si. Plus communément appelé INFP."
    g "Malgré vos résultats ne prenez pas votre type pour acquis. N'hésitez pas à lire à propos des 4 fonctions cognitives et leurs aspects introvertis et extravertis."

    return
