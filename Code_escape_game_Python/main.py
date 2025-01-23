def commencer():

    print(r'''
                                                                    
      ____       __  __              ``     ____                _     _             _                     
     / ___|___  / _|/ _|_ __ ___    __ _   / ___|___  _ __ ___ | |__ (_)_ __   __ _(_)___  ___  _ __  ___ 
    | |   / _ \| |_| |_| '__/ _ \  / _` | | |   / _ \| '_ ` _ \| '_ \| | '_ \ / _` | / __|/ _ \| '_ \/ __|
    | |__| (_) |  _|  _| | |  __/ | (_| | | |__| (_) | | | | | | |_) | | | | | (_| | \__ \ (_) | | | \__ \
     \____\___/|_| |_| |_|  \___|  \__,_|  \____\___/|_| |_| |_|_.__/|_|_| |_|\__,_|_|___/\___/|_| |_|___/
                                                                                                       
                                                                                                
                                                                                                
        

                     |                   |                  |                     |
            _________|________________.=""_;=.______________|_____________________|_______
            |                   |  ,-"_,=""     `"=.|                  |
            |___________________|__"=._o`"-._        `"=.______________|___________________
                      |                `"=._o`"=._      _`"=._                     |
             _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
            |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
            |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
                      |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
             _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
            |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
            |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
            ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
            /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
            ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
            /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
            ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
            /______/______/______/______/______/______/______/______/______/______/_____ /
            
    ''')
    
    import time    

    phrase1 = "En inspectant le coffre, Léo découvre une suite de chiffres"
    for char in phrase1:
        print(char, end='', flush=True)
        time.sleep(0.03)
    print()  
    time.sleep(0.8)

    phrase2 = "Il essuie la poussière avec sa main et retranscrit sur un papier cette suite de chiffres"
    for char in phrase2:
        print(char, end='', flush=True)
        time.sleep(0.03)
    print()
    time.sleep(0.8) 

    phrase3 = "Léo écrit 🖊️📖 ...."
    for char in phrase3:
        print(char, end='', flush=True)
        time.sleep(0.02)
    print()
    time.sleep(0.5)

    phrase4 = "1111011 - 1111010"
    for char in phrase4:
        print(char, end='', flush=True)
        time.sleep(0.04)
    print()
    time.sleep(0.8)

    phrase5 = "Aidez Léo à convertir ces deux codes binaires, puis soustrayez-les."
    for char in phrase5:
        print(char, end='', flush=True)
        time.sleep(0.03)
    print()
    time.sleep(0.8)

    bonnereponse1 = 2
    erreurs=0


    phrase5 = None  
    while phrase5 != bonnereponse1:
        phrase5 = int(input("Entrez votre réponse : "))  
        if phrase5 == bonnereponse1:
            phrase6 = "Félicitation, vous avez trouvé la bonne réponse !"
            for char in phrase6:
                print(char, end='', flush=True)
                time.sleep(0.03)
            print()
        else:
            erreurs += 1
            print("Mauvaise réponse. Veuillez réessayer.")
            print("(Indice: Relisez bien les parchemins qui ont été mis à votre disposition !)")
    totalerreurs1=erreurs
    print("----------------------------------------------------------------------")
    print("----------------------------------------------------------------------")
    time.sleep(0.8)
    phrase7 = "En cherchant un nouvelle indice, Léo soulève le coffre."
    for char in phrase7:
        print(char, end='', flush=True)
        time.sleep(0.03)
    print()
    time.sleep(0.8)

    phrase8 = "Il y découvre une carte d'identité abîmée."
    for char in phrase8:
        print(char, end='', flush=True)
        time.sleep(0.03)
    print()
    time.sleep(0.8)

    print(r'''
        +----------------------------------------+
        |           CARTE D'IDENTITÉ             |
        +----------------------------------------+
        | Nom               : *u**ng             |
        | Prénom            : *l**               |
        | Date de naissance : 23/0*/1912         |
        | Sexe              : Masculin           |
        | Lieu de naissance : W*lms**w           |
        +----------------------------------------+      
''')
    
    phrase9= "(Indice : Déchiffreur de la machine Enigma )"
    for char in phrase9:
        print(char, end='', flush=True)
        time.sleep(0.03)
    print()
    time.sleep(0.8)

    phrase10 = "Retrouvez le chiffre manquant de sa date de naissance"
    for char in phrase10:
        print(char, end='', flush=True)
        time.sleep(0.03)
    print()
    time.sleep(0.8)


    bonnereponse2 = 6
    erreurs=0

    phrase11 = None  
    while phrase11 != bonnereponse2:
        phrase11 = int(input("Entrez votre réponse : "))  
        if phrase11 == bonnereponse2:
            phrase12 = "Félicitation, vous avez trouvé la bonne réponse !"
            for char in phrase12:
                print(char, end='', flush=True)
                time.sleep(0.03)
            print()
        else:
            erreurs += 1
            print("Mauvaise réponse. Veuillez réessayer.")
    totalerreurs2=erreurs
    print("----------------------------------------------------------------------")
    print("----------------------------------------------------------------------")
    time.sleep(0.8)
    
    phrase13= "En retrouvant l'identité d'Alan Turing"
    for char in phrase13:
        print(char, end='', flush=True)
        time.sleep(0.03)
    print()
    time.sleep(0.8)

    phrase14= "Léo se rappelle d'un livre dans lequel Alan Turing est mentionné"
    for char in phrase14:
        print(char, end='', flush=True)
        time.sleep(0.03)
    print()
    time.sleep(0.8)

    
    phrase15= "Voici la page :"
    for char in phrase15:
        print(char, end='', flush=True)
        time.sleep(0.03)
    print()
    time.sleep(0.8)

    print(r'''
            ╔══════════════════════════════╗
            ║          Alan Turing         ║
            ║                              ║
            ║ ~~ ~~~~~~ ~~~~~~~~~~~ ~~~~~  ║
            ║ ~~~~~ ~~~ ~~~~~ ~~ ~~~~~~~~  ║
            ║ ~~~~~~~~ ~~~~~~~~  ~~~~~     ║
            ║                              ║
            ║ ~~ ~~~~~~ ~~~~~~~~~~~ ~~~~~  ║
            ║ ~~~ http://localhost:3000 ~~ ║
            ║ ~~~~~ ~~~ ~~~~~ ~~ ~~~~~~~~  ║
            ║                              ║
            ║ ~~~~~ ~~~ ~~~~~ ~~ ~~~~~~~~  ║
            ║ ~~~~~~~~ ~~~~~~~~  ~~~~~     ║
            ║                              ║
            ║            Page 8            ║
            ╚══════════════════════════════╝
''')
    

    phrase16= "On y voit un liens menant vers une page internet"
    for char in phrase16:
        print(char, end='', flush=True)
        time.sleep(0.02)
    print()
    time.sleep(0.5)


    phrase17= "Aidez Léo à trouver l'indice qui est caché dans cette page"
    for char in phrase17:
        print(char, end='', flush=True)
        time.sleep(0.02)
    print()
    time.sleep(0.5)

   

    bonnereponse3 = 9
    phrase18 = None
    erreurs = 0  

    while phrase18 != bonnereponse3:
        try:
            phrase18 = int(input("Entrez votre réponse : "))
        except ValueError:
            print("Veuillez entrer un nombre valide.")
            continue

        if phrase18 == bonnereponse3:
            phrase19 = "Félicitations, vous avez trouvé la bonne réponse !"
            for char in phrase19:
                print(char, end='', flush=True)
                time.sleep(0.03)
            print()  
        else:
            erreurs += 1
            print("Mauvaise réponse. Veuillez réessayer.")
            if erreurs == 1:
                print("(Indice: Relisez bien le parchemin sur la biographie de Alan Turning)")
            elif erreurs == 2:
                print("(Deuxième indice: Inspecter l'élément)")
    totalerreurs3=erreurs

    print("----------------------------------------------------------------------")
    print("----------------------------------------------------------------------")
    time.sleep(0.8)

    phrase20= "En continuant à chercher d'autre indice pendant des heures,"
    for char in phrase20:
        print(char, end='', flush=True)
        time.sleep(0.03)
    print()
    time.sleep(0.8)

    phrase21= "Léo et ses amis décident de prendre une pose et de s'asseoir."
    for char in phrase21:
        print(char, end='', flush=True)
        time.sleep(0.03)
    print()
    time.sleep(0.8)

    phrase22= "En voulant s'asseoir l'un de ses amis fait accidentelement tomber la bibliothèque "
    for char in phrase22:
        print(char, end='', flush=True)
        time.sleep(0.03)
    print()
    time.sleep(0.8)

    phrase23= "En se relevant, il découvre une inscription sur le mur"
    for char in phrase23:
        print(char, end='', flush=True)
        time.sleep(0.03)
    print()
    time.sleep(0.8)

    phrase24= "Ceci est le dernière indice qui les mèneront à trouver le code"
    for char in phrase24:
        print(char, end='', flush=True)
        time.sleep(0.03)
    print()
    time.sleep(0.8)

    phrase25= "Voici ce qui est inscrit sur le mur :"
    for char in phrase25:
        print(char, end='', flush=True)
        time.sleep(0.03)
    print()
    time.sleep(0.8)

    print(r'''

        ░▒▓█▓▒░▒▓███████▓▒░       ░▒▓██████████████▓▒░ ░▒▓██████▓▒░░▒▓███████▓▒░        ░▒▓██████▓▒░  
     ░▒▓████▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
        ░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
        ░▒▓█▓▒░░▒▓██████▓▒░       ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░       ░▒▓███████▓▒░ 
        ░▒▓█▓▒░▒▓█▓▒░             ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░             ░▒▓█▓▒░ 
        ░▒▓█▓▒░▒▓█▓▒░             ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░             ░▒▓█▓▒░ 
        ░▒▓█▓▒░▒▓████████▓▒░      ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░░▒▓███████▓▒░        ░▒▓██████▓▒░  
                                                                                                 
                                                                                                 
    ''')
    

    bonnereponse4 = 3
    phrase26 = None
    erreurs = 0  

    while phrase26 != bonnereponse4:
        try:
            phrase26 = int(input("Entrez votre réponse : "))
        except ValueError:
            print("Veuillez entrer un nombre valide.")
            continue

        if phrase26 == bonnereponse4:
            phrase27 = "Félicitations, vous avez trouvé la bonne réponse !"
            for char in phrase27:
                print(char, end='', flush=True)
                time.sleep(0.03)
            print()
        else:
            erreurs += 1
            print("Mauvaise réponse. Veuillez réessayer.")
            if erreurs == 1:
                print("(Indice: Relisez bien les parchemins qui ont été mis à votre disposition !)")
            elif erreurs == 2:
                print("(Deuxième indice: L'information ce trouve dans le parchemins des types d'opérations !)")
    totalerreurs4=erreurs
    print("----------------------------------------------------------------------")
    print("----------------------------------------------------------------------")
    time.sleep(0.8)


    bonne_reponses = 2693

    phrase28 = None  
    while phrase28 != bonne_reponses:
        phrase28 = int(input("Entrez dans l'ordre tous les chiffres que vous avez trouvés grâce aux indices : ")) 

        if phrase28 == bonne_reponses:
            phrase29 = "Maintenant que nous avons récupéré les 4 chiffres,"
            for char in phrase29:
                print(char, end='', flush=True)
                time.sleep(0.03)
            print()
        else:
            print("Mauvaise réponse. Veuillez réessayer.")
    time.sleep(0.8)


    phrase30= "Nous allons tester toutes les combinaisons possible pour déverouiller le cadenas."
    for char in phrase30:
        print(char, end='', flush=True)
        time.sleep(0.03)
    print()
    time.sleep(0.8)

    

    from itertools import permutations
    import random

    while True:
        reponses = input("Êtes-vous prêts ? (oui/non) : ").strip().lower()
        if reponses == "oui":
            password = [6, 2, 3, 9]
            break
        elif reponses == "non":
            print("D'accord, prenez votre temps !")
        else:
            print("Veuillez répondre par 'oui' ou 'non'.")

    attempted_combinations = []
    found = False

    possible_combinations = list(permutations(password))
    random.shuffle(possible_combinations) 

    print("Début de la recherche du mot de passe...\n")

    for combination in possible_combinations:
        attempted_combinations.append(combination)
        print(f"Combinaison testée: {combination}")
        time.sleep(0.2)
        
        if list(combination) == password:
            print(f"\nMot de passe trouvé ! : {combination}")
            found = True
            break

    print(f"\nNombre total des combinaisons testées : {len(attempted_combinations)}")

    
    print("----------------------------------------------------------------------")
    totalerreurs = totalerreurs1 + totalerreurs2 + totalerreurs3 + totalerreurs4
    time.sleep(0.8)
    phrase31= "Léo dévérouille le coffre.."
    for char in phrase31:
        print(char, end='', flush=True)
        time.sleep(0.03)
    print()
    time.sleep(0.8)

    phrase32= "Des jetons d'une valeur inestimable émanent du coffre"
    for char in phrase32:
        print(char, end='', flush=True)
        time.sleep(0.03)
    print()
    time.sleep(0.8)

    phrase33= "Il décide de vous remercier en vous passant des jetons"
    for char in phrase33:
        print(char, end='', flush=True)
        time.sleep(0.03)
    print()
    time.sleep(0.8)

    phrase33= "Le nombre de jetons est donné en fonction du nombre de fautes que vous avez faites"
    for char in phrase33:
        print(char, end='', flush=True)
        time.sleep(0.03)
    print()
    time.sleep(0.8)

    jetons = (6 - (totalerreurs*1))

    print(f"Vous avez obtenu {jetons} jetons !")
    if jetons <= 0 :
        print ("Pour votre participation, nous vous donnons quand même 1 jeton de 10 !")
    print("Merci d'avoir aidé avec Léo et ses amis.")








while True:
    reponse = input("Voulez-vous commencer ? (oui/non) : ").strip().lower()
    if reponse == "oui":
        commencer()
    elif reponse == "non":
        print("Le programme ne commence pas.")
    else:
        print("Veuillez répondre par 'oui' ou 'non'.")
    


