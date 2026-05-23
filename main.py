from Player import Player
#Poser ornitho tour 1 obligatoire pour pas crever
#Checker où les gens ont déplacé leurs trucs pour prédire attaques
densites = ""

player = Player("SuperCrazyLazy")

game=True
while(game):
    if(player.play()):
        print(f"Go tour {player.tour}")
        #Recalculer rentabilité cases
        #Eventuellement stocker etat plateau
        if(player.tour==1):
            densites = player.infos_densite()
            #Choisir lieu pour foreuse
            #Poser foreuse
            player.ajouter_orni()
            #Recup info orni
                #Bouger si besoin
            

