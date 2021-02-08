""" --- MASTERMIND --- """

""" --- Naam : Hussin Almoustafa 
     --- Date 08-02-2021"""
import random



"""
Feedback 08/02/2021
Comments:
Het commenten van elke def is duidelijk.
Taal:
Geef er zelf niet super veel om, maar je wisselt een hoop tussen engels en nederlands, als je nederlands gebruikt is opzich handig want dan zie je meteen wat jouwn functie
is en welke onderdelen code taal zijn.
Bijv lijst en list.
Leesbaarheid:
Goed leesbaar, kan met 1 keer doorlezen precies zien wat elke def doet.
Error(s) vangen:
Goed gedaan, gecontroleerd op geldige invoer ja/nee.

Conclusie:
Nog een beetje je taal afwisseling verbeteren, het helpt namelijk wel met de leesbaarheid (ook voor jezelf denk ik)
Verder gaat het goed!
"""
kleuren = ["A", "B", "C", "D", "E", "F"]


def knowledge_maker(gok, feedback):
    """ Een functie die alle  feedack's & gokken analyseert  """
    return



def aantal_moelijkhede():
    """ Een functie die alle kleuren combinatie in een list stopt """

    keys = "ABCDEF"
    arr = keys #Is niet perse nodig, kan ook keys[x] doen.
    aantal_mogelijkheden = []
    for i in range(6):
        for j in range(6):
            for k in range(6):
                for m in range(6):
                    antwoord = arr[i] + arr[j] + arr[k] + arr[m]
                    aantal_mogelijkheden.append(antwoord)

    print(aantal_mogelijkheden)
    return aantal_mogelijkheden




def feedback_analyze(speler_gok , kleur_code ):
    """ Een functie die de evaluatie weergeeft.
     De evaluatie is als volgt:

    Als je een pin op de juiste plaats en in de juiste kleur hebt, dan krijg je een zwarte pin >> [1]
    Als je een pin op de verkeerde plaats hebt maar de juiste kleur, dan krijg je een witte pin >> [0]
     Anders krijg je >> [-1]"""

    feedback = [-1, -1, -1, -1] #Handig.

    for i in range(len(kleur_code)):
        if  speler_gok[i] == kleur_code[i]:
            feedback[i] = 1
        elif speler_gok.count(kleur_code[i]) == 1:
            feedback[i] = 0
        else:
            feedback[i] = -1 #Deze is niet nodig, want je feedback lijst is al -1, je kan dus ook gewoon skippen en niets doen.
    print(feedback)

    return feedback



def Een_rondom_code(kleur_code):
    """
     Een Functie die rondom combinatie geeft
    """
    move = []
    available_choices = ["A", "B", "C", "D", "E", "F"] 


    for x in range(0, len(kleur_code)):
        val = random.choice(available_choices)
        move.append(val)
        available_choices.remove(val)
    print(move)

    return move

def Een_consequent_gok(gok, feedback):
    """ Een functie die een consequent gok geeft op basis van de feedback """
    niewue_gok = [] #nieuwe ipv niewue.
    feedback = feedback_analyze(gok, kleur_code)
    for i in range(0, len(gok)):
        if feedback[i] == 1 :
            niewue_gok.append(gok[i])

        elif feedback[i] == 0:
            gok.split()
            print(gok.split("(?!^)"))
            gok[i] = gok.index()
            niewue_gok.append(gok[i])

    print(niewue_gok)
    return gok



# Handelt op dit moment wel erg veel direct zelf, probeer wat van zijn handelingen te vertalen naar functies. Makelijker te porten naar andere media's + je kan dan later
# voor andere opdrachten je eigen functies jatten, scheelt weer plagiaat!
def Game():
    print(" --- MASTERMIND --- \n")
    print("Raad de geheime kleurcode in zo min mogelijk pogingen.\n")
    print("Voer uw kleurcode in. \n U kunt rood (A), groen (B), blauw (C), geel (D), wit (E) en roze (F) gebruiken")


    pogingen = 0
    spelen = True
    global kleur_code

    kleur_code = random.sample(kleuren, 4)
    print(kleur_code)
     
    while spelen:
        juiste_kleur = ""
        geraden_kleur = ""

        speler_gok = input().upper()
        pogingen += 1

        if len(speler_gok) != len(kleur_code):
            print(
                "\nDe geheime code heeft precies vier kleuren. Ik weet het, je kunt tot vier tellen. Probeer het nog eens!")
            continue #Niet elke keer nodig, haal er eens een paar weg en kijk of het dan nog werkt. Leuke bron: https://www.programiz.com/python-programming/break-continue
        for i in range(4):
            if speler_gok[i] not in kleuren:
                print("\nZoek op welke kleuren je in dit spel kunt gebruiken !!!!")
                continue
     
        if juiste_kleur != "****":
            for i in range(0, len(speler_gok)):
                if speler_gok[i] == kleur_code[i]:
                    juiste_kleur += "*"
                elif speler_gok[i] != kleur_code[i] and speler_gok[i] in kleur_code :
                    geraden_kleur += "."

            feedback = (juiste_kleur + geraden_kleur +"\n")
            print(feedback)

        if juiste_kleur == "****":
            if pogingen == 1:
                print("Wauw! Je raadt het al bij de eerste poging!")
                print("Gefsltieerd!!!! U heeft gewonen!") #Gefeliciteerd! U is verder heel net nederlands, U gebruik je vooral voor leraren en ouderen. Meestal is je goed hoor ;)
            else:
                print("Goed gedaan... Binnen " + str(pogingen) + " Keer je raadt het al.")
                print("Gefsltieerd!!!! U heeft gewonen!")
            spelen = False

        if pogingen >= 1 and pogingen < 8 and juiste_kleur != "***":
            print("Volgende poging: ")
        elif pogingen >= 8:
            print("Je raadde het niet! De geheime kleurcode was: " + str(kleur_code))

        while spelen == False:
            finish_game = input("\nWil je nog een keer spelen (J / N)?").upper()
            pogingen = 0
            if finish_game == "N":
                print("Bedankt voor het spel! Tot ziens!")
                break
            elif finish_game == "J":
                spelen = True
                print("Dus laten we opnieuw spelen ... Raad de geheime code:")



Game()
