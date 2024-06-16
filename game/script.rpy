
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
image h = im.Scale("musee.png", 500, 800)
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
image c shy = im.Scale("Eve_Shy.png", 500, 800)
image e blush= im.Scale("Male_Blush.png", 750, 1250)
image cabinet_psy = Transform("cabinet.jpg", zoom=3, xoffset=-200)
image ex = Transform("cabinet_ex.jpg", zoom=3, xoffset=-200)
image ex2 = Transform("cabinet_ex2.jpg", zoom=3, xoffset=-200)
image ex3 = Transform("cabinet_ex3.jpg", zoom=3, xoffset=-200)
image ex4 = Transform("cabinet_ex4.jpg", zoom=3, xoffset=-200)
image ex5 = Transform("cabinet_ex5.jpg", zoom=3, xoffset=-200)
image ex6 = Transform("cabinet_ex6.jpg", zoom=3, xoffset=-200)
image d petit = im.Scale("Sprite Male Dark Hair Neu01.png", 600, 900)
image e petit = im.Scale("Male_Neutral.png", 500, 900)


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
    text "Pour vivre pleinement cette expérience, nous vous conseillons de sélectionner les réponses qui corresponderaient le plus à votre manière d'agir/de penser si vous étiez confrontés à des situations similaires." size 100 color "#000000" xalign 0.5 yalign 0.5

screen debut_message2():
    text "Commençons" size 100 color "#FFFFFF" xalign 0.5 yalign 0.5


label start:
    show screen debut_message1
    show start_background
    $ renpy.pause()
    hide screen debut_message1
    hide start_background
    show screen debut_message2
    $ renpy.pause()
    hide screen debut_message2
    jump debut
    

label debut:
    $ Fe = 0
    $ Fi = 0
    $ Ne = 0
    $ Ni = 0
    $ Se = 0
    $ Si = 0
    $ Te = 0
    $ Ti = 0
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
            b "Ha je vois, jamais facile les travaux de groupe."
            jump Fe_Te
        "Je n'arrive pas à me motiver à faire les choses à l'avance et j'ai du rush pour finir à temps.":
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
    "{i}%(e)s but honteusement avant de tirer une carte pour me poser une question.{\i}"
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
    scene chambre:
        zoom 1.2
    "{i}Vous partez en direction des chambres pour vous préparer pour le centre-ville.{\i}"
    "{i}Une fois les affaires que vous vouliez prises, vous vous mettez en route.{\i}"
    scene vue
    "{i}Vous vous rendez tout d'abord à un endroit offrant une vue dégagée de la plaine en contrebas, c'est magnifique.{\i}"
    "{i}Après avoir profité de la vue quelques instants, vous rejoignez le centre ville et atteignez l'expo d'art qui est dans un musée.{\i}"
    scene art :
        zoom 1.5
    show h:
        xalign 0.2
        yalign 1.0
    show d petit:
        xpos 1100
        ypos 250
    show e petit:
        xpos 1450
        ypos 200 
    "{i}Un homme connaisseur vous fait la visite en vous abreuvant de faits tous les plus intéressants les uns que les autres.{\i}"
    "{i}Il vous raconte de nombreuses anecdotes que vous savez que vous allez pouvoir ressortir pour épater la galerie.{\i}"
    hide h
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
    "{i}Tu te sens revigorée après cette échange et te sens plus proche encore qu'avant de tes amies.{\i}"
    "{i}Vous vous préparez alors pour aller au cinéma et sortez en ville rejoindre le reste de la troupe.{\i}"
    scene cinema:
        zoom 1.5
    "{i}Vous retrouvez les autres à l'heure convenue et vous vous rendez dans la salle.{\i}"
    show c:
        xalign 0.66
        yalign 1.0
    "{i}Une fois assis, vous piquez du popcorn chez votre voisine de droite %(c)s et réalisez qu'il s'agit de popcorn sucré.{\i}"
    "{i}Vous vous rappelez qu'elle avait spécifié qu'elle les voulait salé et vous savez qu'elle n'aime pas les sucrés.{\i}"
    "{i}%(c)s devine le fond de ta pensée.{\i}"
    show c shy:
        xalign 0.66
        yalign 1.0
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
    "{i}Il te raconte un peu les stratagèmes qu'il emploie et tu commences à douter de ses compétences en la matière.{\i}"
    "{i}Néanmoins, tu lui demandes quand même de te faire des retours sur leur efficacité.{\i}"
    "{i}Vous vous préparez alors pour aller au cinéma et sortez du musée pour rejoindre le reste de la troupe.{\i}"
    scene cinema:
        zoom 1.5
    "{i}Vous retrouvez les autres à l'heure convenue et vous vous rendez dans la salle.{\i}"
    show c:
        xalign 0.66
        yalign 1.0
    "{i}Une fois assis, vous piquez du popcorn chez votre voisine de droite %(c)s et réalisez qu'il s'agit de popcorn sucré.{\i}"
    "{i}Vous vous rappelez qu'elle avait spécifié qu'elle les voulait salé et vous savez qu'elle n'aime pas les sucrés.{\i}"
    "{i}%(c)s devine le fond de ta pensée.{\i}"
    show c shy:
        xalign 0.66
        yalign 1.0
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
    show c:
        xalign 0.66
        yalign 1.0
    "{i}Une fois assis, vous piquez du popcorn chez votre voisine de droite %(c)s et réalisez qu'il s'agit de popcorn sucré.{\i}"
    "{i}Vous vous rappelez qu'elle avait spécifié qu'elle les voulait salé et vous savez qu'elle n'aime pas les sucrés.{\i}"
    "{i}%(c)s devine le fond de ta pensée.{\i}"
    show c shy:
        xalign 0.66
        yalign 1.0
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
    show h:
        xalign 0.2
        yalign 1.0
    "{i}Vous posez toutes les questions qui vous trottent dans la tête au gardien à propos du tour guidé que vous venez de suivre.{\i}"
    "{i}Vous vous y prenez si bien qu'il vous offre différents billets et réductions pour d'autres expositions dans la région. Entre passionnés on se comprend !{\i}"
    hide h
    "{i}Vous vous préparez alors pour aller au cinéma et sortez du musée pour rejoindre le reste de la troupe.{\i}"
    scene cinema:
        zoom 1.5
    "{i}Vous retrouvez les autres à l'heure convenue et vous vous rendez dans la salle.{\i}"
    show c:
        xalign 0.66
        yalign 1.0
    "{i}Une fois assis, vous piquez du popcorn chez votre voisine de droite %(c)s et réalisez qu'il s'agit de popcorn sucré.{\i}"
    "{i}Vous vous rappelez qu'elle avait spécifié qu'elle les voulait salé et vous savez qu'elle n'aime pas les sucrés.{\i}"
    "{i}%(c)s devine le fond de ta pensée.{\i}"
    show c shy:
        xalign 0.66
        yalign 1.0
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
    stop music fadeout 2.0
    with Dissolve(2.0) 
    "{i}Ta vision se trouble tout à coup, tu sens l'espace qui t'environnait comme se dissoudre.{\i}"
    play music "psy.mp3" fadein 2.0
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
            g "Vous êtes Fe dominant avec comme auxiliaires Ni et Se. Plus communément appelé ENFJ."
            g "Votre fonction dominante Fe, Feelings extravertis ou sentiments extravertis, indiquent que vous faites beaucoup attention aux autres."
            g "Vous êtes généralement la personne prête à vous sacrifier pour les autres ou à donner un coup de main."
            g "Vous aimez créer la bonne humeur et le confort chez autruis quitte à vous sacrifier au passage."
            g "Votre fonction auxiliaire est l'intuition introvertie, cette fonction est probablement la plus mystique."
            g "Vous utilisez votre intuition pour imaginer des scénarios dans le futur."
            g "Comme vous vous projetez loin, soit vous devinez des événements et surprenez tout le monde autour de vous, soit vous passez pour un idiot ou un fou."
        if Si>Ni :
            g "Vous êtes Fe dominant avec comme auxiliaires Si et Ne. Plus communément appelé ESFJ."
            g "Votre fonction dominante Fe, Feelings extravertis ou sentiments extravertis, indiquent que vous faites beaucoup attention aux autres."
            g "Vous êtes généralement la personne prête à vous sacrifier pour les autres ou à donner un coup de main."
            g "Vous aimez créer la bonne humeur et le confort chez autruis quitte à vous sacrifier au passage."
            g "Votre fonction auxiliaire est la sensation introvertie, vous utilisez cette fonction pour ressasser intérieurement des sensations vécues par le passé."
            g "En d'autres termes, vous aimez bien ce que vous connaissez déjà et aimez bien créer une routine si possible car vous vous sentez plus confortable ainsi."
            g "Cette fonction vous rend peu prompt à tester de nouvelles choses par vous-mêmes mais vous savez qu'avec de l'habitude vous pouvez tout aimer."
    if Te>Ne and Te>Ni and Te>Se and Te>Si and Te>Fe and Te>Ti and Te>Fi:
        if Ni>Si :
            g "Vous êtes Te dominant avec comme auxiliaires Ni et Se. Plus communément appelé ENTJ."
            g "Avec Te, Thinking extraverti ou pensée extraverti, en fonction dominante, vous cherchez à être efficace."
            g "Vous abattez le travail comme personne s'il y en a et cette fonction peut vous pousser à vouloir être leader de groupe."
            g "Vous avez tendance à aimer organiser les choses et penser que cela ne peut pas être mieux fait que par vous."
            g "Vous n'êtes pas réputé pour prendre des pincettes avec les gens, même si vous avez peut-être appris avec le temps."
            g "Votre fonction auxiliaire est l'intuition introvertie, cette fonction est probablement la plus mystique."
            g "Vous utilisez votre intuition pour imaginer des scénarios dans le futur."
            g "Comme vous vous projetez loin, soit vous devinez des événements et surprenez tout le monde autour de vous, soit vous passez pour un idiot ou un fou."
        if Si>Ni :
            g "Vous êtes Te dominant avec comme auxiliaires Si et Ne. Plus communément appelé ESTJ."
            g "Avec Te, Thinking extraverti ou pensée extraverti, en fonction dominante, vous cherchez à être efficace."
            g "Vous abattez le travail comme personne s'il y en a et cette fonction peut vous pousser à vouloir être leader de groupe."
            g "Vous avez tendance à aimer organiser les choses et penser que cela ne peut pas être mieux fait que par vous."
            g "Votre fonction auxiliaire est la sensation introvertie, vous utilisez cette fonction pour ressasser intérieurement des sensations vécues par le passé."
            g "En d'autres termes, vous aimez bien ce que vous connaissez déjà et aimez bien créer une routine si possible car vous vous sentez plus confortable ainsi."
            g "Cette fonction vous rend peu prompt à tester de nouvelles choses par vous-mêmes mais vous savez qu'avec de l'habitude vous pouvez tout aimer."
    if Ne>Te and Ne>Ni and Ne>Se and Ne>Si and Ne>Fe and Ne>Ti and Ne>Fi:
        if Fi>Ti :
            g "Vous êtes Ne dominant avec comme auxiliaires Fi et Te. Plus communément appelé ENFP."
            g "Utilisant principalement l'iNtuition extravertie, vous regorgez d'idées et êtes un parfait membre pour les brainstormings."
            g "Vous tendez néanmoins à vous disperser dans tous les sens et abandonner des projets en cours ou pas encore commencé."
            g "Vous détestez la routine et dites oui à tout ce qui pourrait être nouveau et surprenant."
            g "Votre fonction auxiliaire est Fi ou sentiments introvertis, vous avez de fortes valeurs internes et tout un code moral."
            g "Vous restez à l'écoute de vos sentiments dans l'espoir de comprendre vraiement qui \'vous\' êtes au fond de vous."
            g "Si quelqu'un va à l'encontre des valeurs que vous arborez vous serez grandement affectés."
        if Ti>Fi :
            g "Vous êtes Ne dominant avec comme auxiliaires Ti et Fe. Plus communément appelé ENTP."
            g "Utilisant principalement l'iNtuition extravertie, vous regorgez d'idées et êtes un parfait membre pour les brainstormings."
            g "Vous tendez néanmoins à vous disperser dans tous les sens et abandonner des projets en cours ou pas encore commencé."
            g "Vous détestez la routine et dites oui à tout ce qui pourrait être nouveau et surprenant."
            g "Votre fonction auxiliaire, Thinking introverti ou pensée introvertie, vous pousse à chercher la connaissance."
            g "Vous avez besoin de savoir comment cela fonctionne, pas seulement si cela fonctionne."
            g "Vous êtes à l'affut des règles qui régissent le monde et cherchez non seulement à les découvrir mais à les comprendre."
            g "Cette fonction vous fait tendre à être rationnel et logique ce qui peut mener à négliger les valeurs et sentiments d'autruis."
    if Se>Te and Se>Ni and Se>Ne and Se>Si and Se>Fe and Se>Ti and Se>Fi:
        if Fi>Ti :
            g "Vous êtes Se dominant avec comme auxiliaires Fi et Te. Plus communément appelé ESFP."
            g "Votre fonction dominante est la Sensation extravertie ou Se, vous êtes avides d'expériences."
            g "Plus particulièrement d'expériences qui ravissent vos sens, que ce soit voir un beau paysage, manger un plat succulent ou alors mettre vos sens dans tout leur état avec des sports extrêmes."
            g "Vous êtes très observateurs et repérez les petits détails que les autres n'ont pas vu; un nouveau parfum, un nouveau pull, etc."
            g "Votre fonction auxiliaire est Fi ou sentiments introvertis, vous avez de fortes valeurs internes et tout un code moral."
            g "Vous restez à l'écoute de vos sentiments dans l'espoir de comprendre vraiement qui \'vous\' êtes au fond de vous."
            g "Si quelqu'un va à l'encontre des valeurs que vous arborez vous serez grandement affectés."
        if Ti>Fi :
            g "Vous êtes Se dominant avec comme auxiliaires Ti et Fe. Plus communément appelé ESTP."
            g "Votre fonction dominante est la Sensation extravertie ou Se, vous êtes avides d'expériences."
            g "Plus particulièrement d'expériences qui ravissent vos sens, que ce soit voir un beau paysage, manger un plat succulent ou alors mettre vos sens dans tout leur état avec des sports extrêmes."
            g "Vous êtes très observateurs et repérez les petits détails que les autres n'ont pas vu; un nouveau parfum, un nouveau pull, etc."
            g "Votre fonction auxiliaire, Thinking introverti ou pensée introvertie, vous pousse à chercher la connaissance."
            g "Vous avez besoin de savoir comment cela fonctionne, pas seulement si cela fonctionne."
            g "Vous êtes à l'affut des règles qui régissent le monde et cherchez non seulement à les découvrir mais à les comprendre."
            g "Cette fonction vous fait tendre à être rationnel et logique ce qui peut mener à négliger les valeurs et sentiments d'autruis."
    if Si>Te and Si>Ni and Si>Ne and Si>Se and Si>Fe and Si>Ti and Si>Fi:
        if Fe>Te :
            g "Vous êtes Si dominant avec comme auxiliaires Fe et Ti. Plus communément appelé ISFJ."
            g "Votre fonction dominante est la sensation introvertie, vous utilisez cette fonction pour ressasser intérieurement des sensations vécues par le passé."
            g "En d'autres termes, vous aimez bien ce que vous connaissez déjà et aimez bien créer une routine si possible car vous vous sentez plus confortable ainsi."
            g "Cette fonction vous rend peu prompt à tester de nouvelles choses par vous-mêmes mais vous savez qu'avec de l'habitude vous pouvez tout aimer."
            g "Votre fonction auxiliaire Fe, Feelings extravertis ou sentiments extravertis, indiquent que vous faites beaucoup attention aux autres."
            g "Vous êtes généralement la personne prête à vous sacrifier pour les autres ou à donner un coup de main."
            g "Vous aimez créer la bonne humeur et le confort chez autruis quitte à vous sacrifier au passage."
        if Te>Fe :
            g "Vous êtes Si dominant avec comme auxiliaires Te et Fi. Plus communément appelé ISTJ."
            g "Votre fonction dominante est la sensation introvertie, vous utilisez cette fonction pour ressasser intérieurement des sensations vécues par le passé."
            g "En d'autres termes, vous aimez bien ce que vous connaissez déjà et aimez bien créer une routine si possible car vous vous sentez plus confortable ainsi."
            g "Cette fonction vous rend peu prompt à tester de nouvelles choses par vous-mêmes mais vous savez qu'avec de l'habitude vous pouvez tout aimer."
            g "Avec Te, Thinking extraverti ou pensée extraverti, en fonction auxiliaire, vous cherchez à être efficace."
            g "Vous abattez le travail comme personne s'il y en a et cette fonction peut vous pousser à vouloir être leader de groupe."
            g "Vous avez tendance à aimer organiser les choses et penser que cela ne peut pas être mieux fait que par vous."
    if Ni>Te and Ni>Si and Ni>Ne and Ni>Se and Ni>Fe and Ni>Ti and Ni>Fi:
        if Fe>Te :
            g "Vous êtes Ni dominant avec comme auxiliaires Fe et Ti. Plus communément appelé INFJ."
            g "Votre fonction dominante est l'intuition introvertie, cette fonction est probablement la plus mystique."
            g "Vous utilisez votre intuition pour imaginer des scénarios dans le futur."
            g "Comme vous vous projetez loin, soit vous devinez des événements et surprenez tout le monde autour de vous, soit vous passez pour un idiot ou un fou."
            g "Votre fonction auxiliaire Fe, Feelings extravertis ou sentiments extravertis, indiquent que vous faites beaucoup attention aux autres."
            g "Vous êtes généralement la personne prête à vous sacrifier pour les autres ou à donner un coup de main."
            g "Vous aimez créer la bonne humeur et le confort chez autruis quitte à vous sacrifier au passage."
        if Te>Fe :
            g "Vous êtes Ni dominant avec comme auxiliaires Te et Fi. Plus communément appelé INTJ."
            g "Votre fonction dominante est l'intuition introvertie, cette fonction est probablement la plus mystique."
            g "Vous utilisez votre intuition pour imaginer des scénarios dans le futur."
            g "Comme vous vous projetez loin, soit vous devinez des événements et surprenez tout le monde autour de vous, soit vous passez pour un idiot ou un fou."
            g "Avec Te, Thinking extraverti ou pensée extraverti, en fonction auxiliaire, vous cherchez à être efficace."
            g "Vous abattez le travail comme personne s'il y en a et cette fonction peut vous pousser à vouloir être leader de groupe."
            g "Vous avez tendance à aimer organiser les choses et penser que cela ne peut pas être mieux fait que par vous."
    if Ti>Te and Ti>Ni and Ti>Ne and Ti>Se and Ti>Fe and Ti>Si and Ti>Fi:
        if Se>Ne :
            g "Vous êtes Ti dominant avec comme auxiliaires Se et Ni. Plus communément appelé ISTP."
            g "Votre fonction dominante, Thinking introverti ou pensée introvertie, vous pousse à chercher la connaissance."
            g "Vous avez besoin de savoir comment cela fonctionne, pas seulement si cela fonctionne."
            g "Vous êtes à l'affut des règles qui régissent le monde et cherchez non seulement à les découvrir mais à les comprendre."
            g "Cette fonction vous fait tendre à être rationnel et logique ce qui peut mener à négliger les valeurs et sentiments d'autruis."
            g "Votre fonction dominante est la Sensation extravertie ou Se, vous êtes avides d'expériences."
            g "Plus particulièrement d'expériences qui ravissent vos sens, que ce soit voir un beau paysage, manger un plat succulent ou alors mettre vos sens dans tout leur état avec des sports extrêmes."
            g "Vous êtes très observateurs et repérez les petits détails que les autres n'ont pas vu; un nouveau parfum, un nouveau pull, etc."
        if Ne>Se :
            g "Vous êtes Ti dominant avec comme auxiliaires Ne et Si. Plus communément appelé INTP."
            g "Votre fonction dominante, Thinking introverti ou pensée introvertie, vous pousse à chercher la connaissance."
            g "Vous avez besoin de savoir comment cela fonctionne, pas seulement si cela fonctionne."
            g "Vous êtes à l'affut des règles qui régissent le monde et cherchez non seulement à les découvrir mais à les comprendre."
            g "Cette fonction vous fait tendre à être rationnel et logique ce qui peut mener à négliger les valeurs et sentiments d'autruis."
            g "Utilisant l'iNtuition extravertie en fonction auxiliaire, vous regorgez d'idées et êtes un parfait membre pour les brainstormings."
            g "Vous tendez néanmoins à vous disperser dans tous les sens et abandonner des projets en cours ou pas encore commencé."
            g "Vous détestez la routine et dites oui à tout ce qui pourrait être nouveau et surprenant."
    if Fi>Te and Fi>Ni and Fi>Ne and Fi>Se and Fi>Fe and Fi>Si and Fi>Ti:
        if Se>Ne :
            g "Vous êtes Fi dominant avec comme auxiliaires Se et Ni. Plus communément appelé ISFP."
            g "Votre fonction cominante est Fi ou sentiments introvertis, vous avez de fortes valeurs internes et tout un code moral."
            g "Vous restez à l'écoute de vos sentiments dans l'espoir de comprendre vraiement qui \'vous\' êtes au fond de vous."
            g "Si quelqu'un va à l'encontre des valeurs que vous arborez vous serez grandement affectés."
            g "Votre fonction auxiliaire est la Sensation extravertie ou Se, vous êtes avides d'expériences."
            g "Plus particulièrement d'expériences qui ravissent vos sens, que ce soit voir un beau paysage, manger un plat succulent ou alors mettre vos sens dans tout leur état avec des sports extrêmes."
            g "Vous êtes très observateurs et repérez les petits détails que les autres n'ont pas vu; un nouveau parfum, un nouveau pull, etc."
        if Ne>Se :
            g "Vous êtes Fi dominant avec comme auxiliaires Ne et Si. Plus communément appelé INFP."
            g "Votre fonction cominante est Fi ou sentiments introvertis, vous avez de fortes valeurs internes et tout un code moral."
            g "Vous restez à l'écoute de vos sentiments dans l'espoir de comprendre vraiement qui \'vous\' êtes au fond de vous."
            g "Si quelqu'un va à l'encontre des valeurs que vous arborez vous serez grandement affectés."
            g "Utilisant l'iNtuition extravertie en fonction auxiliaire, vous regorgez d'idées et êtes un parfait membre pour les brainstormings."
            g "Vous tendez néanmoins à vous disperser dans tous les sens et abandonner des projets en cours ou pas encore commencé."
            g "Vous détestez la routine et dites oui à tout ce qui pourrait être nouveau et surprenant."
    g "Malgré vos résultats ne prenez pas votre type pour acquis. N'hésitez pas à lire à propos des 4 fonctions cognitives et leurs aspects introvertis et extravertis."
    g "Les tests, même celui-ci, ne sont jamais 100 pourcents fiables et il n'est pas rare de se considérer comme appartenant au mauvais type."
    g "Renseignez-vous et essayez de trouver quels schémas de pensée vous utilisez par vous-mêmes !"
label fin2:
    menu explication:
        "Je veux plus d'explications sur comment fonctionnent les fonctions cognitives en général.":
            g "La typologie établie par Jung était surtout destinée à déterminer comment un individu recueille et traite les informations autour de lui."
            g "Il y a donc 2 sortes de fonctions."
            g "Nous avons les fonctions qui recueillent l'information qui sont dites des fonctions de perception."
            g "Nous pouvons receuillir l'information soit par l'intuition, \'N\', soit par la sensation \'S\'."
            g "Et nous avons les fonctions qui traitent cette information qui sont dites des fonctions de jugement."
            g "Nous traitons l'information soit avec nos sentiments ou valeurs, \'F\', soit avec notre pensée ou logique, \'T\'."
            g "Chacune de ses fonctions peuvent être introverties ou extravertie, par exemple : Si et Se, sensation introvertie et sensation extravertie."
            g "Une fonction extravertie signifie que l'individu va se tourner vers l'extêrieur pour percevoir l'information, dans le cas de Se et Ne, ou la traiter, dans le cas de Fe et Te."
            g "Une fonction introvertie au contraire signifiera que l'individu se tournera plutôt à l'intérieur de lui-même."
            g "Par exemple, une personne avec un fort Fe traitera l'information en jugeant l'effet qu'elle produit sur son entourage, elle se préoccupera des sentiments des autres."
            g "Tandis qu'une personne dotée d'un fort Fi traitera l'information en jugeant si elle est conforme à ses valeurs et ses sentiments propres."
            g "Jung établissait que nous avions tous une fonction dominante qui soit de perception ou de jugement."
            g "Nous avions ensuite une fonction auxiliaire qui vient compléter la fonction dominante."
            g "Cette fonction auxiliaire sera une fonction de perception si la fonction dominante était de jugement et une fonction de jugement si la fonction dominante était une fonction de perception."
            g "Il en va de même pour l'introversion et l'extraversion; la fonction auxiliaire sera de la sorte que la fonction dominante n'était pas."
            g "Par exemple, une personne avec une fonction dominante Ti, soit une fonction de jugement introverti, aura une fonction de perception extravertie comme fonction auxiliaire, donc Se ou Ne."
            g "Ces 2 fonctions, la fonction dominante et la fonction auxiliaire, sont celles que nous utilisons majoritairement."
            g "Mais nous utilisons tous les 4 fonctions psychologiques que sont l'intuition, la sensation, les sentiments et la pensée."
            g "Ainsi entrent en jeu la 3ème et 4ème fonction; la fonction tertiaire et la fonction inférieure."
            g "Ces fonctions seront utilisées proportionnellement à l'utilisation que nous faisons de nos 2 premières fonctions."
            g "Par exemple, disons que nous avons une fonction dominante Te, une fonction de jugement. Cette fonction aura un impact sur l'utilisation de notre autre fonction de jugement."
            g "En effet, si nous jugeons beaucoup avec notre Te, nous jugerons très peu avec notre Fi qui est la fonction inférieure d'une personne à la fonction dominante Te."
            g "Fi dans ce cas-là sera la fonction inférieure, soit la 4ème fonction, car ce sera la fonction la moins utilisée."
            g "La fonction dominante et la fonction inférieure sont toujours de la même sorte; des fonctions de perception ou des fonctions de jugement."
            g "Il en va de même pour la fonction auxiliaire et la fonction tertiaire."
            g "La typologie de Jung cherchait donc à déterminer les processus de pensées que les individus utilisaient de préférence, sachant qu'ils les utilisaient de toute façon tous à une certain degré."
            g "En ce qu'il s'agit de la notation de ces types, par exemple ENFJ, la première lettre désigne si la fonction est extravertie."
            g "La dernière lettres permet de savoir que c'est la fonction F qui sera extravertie, il s'agit juste d'appris par coeur pour cette notion."
            g "En effet, les types EXXJ auront leur 3ème lettre en fonction dominante extravertie et les EXXP, ce sera leur 2ème lettre."
            g "Quant aux IXXJ, ils auront leur 2ème lettre en fonction dominante introvertie et les IXXP, ce sera la 3ème lettre."
            g "La lettre restante indiquera alors la fonction auxiliaire, sachant que les lettres d'extrémité ne sont présentes que pour indiquer la position et introversion ou extraversion de la fonction dominante."
            menu exemple:
                g "Avez-vous besoin d'un exemple pour clarifier les choses ?"
                "Non, j'ai tout compris, merci !":
                    g "Parfait, vous devriez avoir les bases avec tout cela !"
                    jump fin2
                "Volontiers, ça fait beaucoup d'un coup.":
                    g "Je comprends tout à fait."
                    hide g
                    show ex
                    show g:
                        xalign 0.1
                        yalign 1.0
                    g "Prenons par exemple une personne INTP."
                    g "La première lettre indique que sa fonction dominante sera introvertie."
                    g "Les fonctions de type IXXP ont toujours la 3ème lettre en fonction dominante, donc T qui sera introverti, soit Ti ou logique introvertie."
                    hide g
                    show ex2
                    show g:
                        xalign 0.1
                        yalign 1.0
                    g "Sa fonction auxiliaire sera la lettre restante, donc la 2ème. Cela donnera une fonction auxiliaire d'intuition extravertie ou Ne."
                    hide g
                    show ex3
                    show g:
                        xalign 0.1
                        yalign 1.0
                    g "Nous pouvons alors facilement trouver les fonctions tertiaires et inférieure."
                    g "La fonction auxiliaire est Ne, une fonction de perception extravertie. Pour compenser, il faudra une fonction de perception introvertie et celle que nous n'utilisons pas encore est la sensation, donc cela donnera Si."
                    hide g
                    show ex4
                    show g:
                        xalign 0.1
                        yalign 1.0
                    g "La fonction dominante est Ti, une fonction de jugement introvertie. De même, il faudra une fonction de jugement extraverti que nous n'utilisons pas, soit les valeurs extraverties ou Fe."
                    hide g
                    show ex5
                    show g:
                        xalign 0.1
                        yalign 1.0
                    g "Comme nous l'avions expliqué précédemment, la fonction dominante, ici Ti, est surutilisée, ainsi, l'autre fonction de jugement sera très peu utilisée."
                    hide g
                    show ex6
                    show g:
                        xalign 0.1
                        yalign 1.0
                    g "Si nous devions tracé des flèches quant à l'utilisation des fonctions cognitives chez un INTP cela donnerait donc ceci."
                    g "J'espère que cet exemple vous aura aider à clarifier les choses !"
                    hide g
                    hide ex
                    hide ex2
                    hide ex3
                    hide ex4
                    hide ex5
                    hide ex6
                    show g 
                    jump fin2
        "Je veux essayer une nouvelle voie.":
            g "D'accord. Installe-toi confortablement et ferme les yeux."
            scene noir 
            with Dissolve(2.0) 
            stop music fadeout 2.0
            g "Concentre-toi uniquement sur ma voix et ta respiration."
            play sound "breathing.mp3" volume 1.5
            g "Respire profondément. C'est très bien."
            play sound "snap.mp3"
            g "Endors-toi maintenant."
            ""
            jump debut
        "Je veux quitter le jeu.":
            $ renpy.quit()

    return
