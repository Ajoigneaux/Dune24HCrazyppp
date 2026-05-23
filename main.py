# from Player import Player
# #Poser ornitho tour 1 obligatoire pour pas crever
# #Checker où les gens ont déplacé leurs trucs pour prédire attaques
# densites = ""

# player = Player("SuperCrazyLazy")

# game=True
# while(game):
#     if(player.play()):
#         print(f"Go tour {player.tour}")
#         #Recalculer rentabilité cases
#         #Eventuellement stocker etat plateau
#         # if(player.tour==1):
#             # densites = player.infos_densite()
#             #Choisir lieu pour foreuse
#             #Poser foreuse
#             # player.ajouter_orni()
#             #Recup info orni
#                 #Bouger si besoin
#         player.infos_densite()
#         player.fin_tour()
            

from Player import Player
import tools


secteur_0 = [[0,7], [0,8]]
secteur_1 = [[0,7], [9,17]]
secteur_2 = [[8,15], [0,8]]
secteur_3 = [[8,15], [9,17]]
compteurs_orni = [0, 0, 0, 0]
secteurs = [secteur_0, secteur_1, secteur_2, secteur_3]
player = Player("SuperCrazyLazy")
densitee_initiale = player.infos_densite()
game=True
while(game):
    if(player.play()):

        for i in range(4):
            if compteurs_orni[i] != 0 :
                compteurs_orni[i]-=1


        forreuses_deplacee = []
        money = int(player.infos_scores().split("|")[player.numjoueur])
        tableau_element = player.infos_elements()
        tableau_densitee = tools.recalc_densite(densitee_initiale, tableau_element)
        tableau_orni = player.infos_warning()
        nb_forreuse = 0

        for ligne in range(16) :
                for colone in range(18) :
                    if (tableau_element[ligne][colone] == str(player.numjoueur)) :
                        nb_forreuse+=1


        for ligne in range(0,16) :
            for colone in range(0,18) :
                if tableau_element[ligne][colone] == str(player.numjoueur) and compteurs_orni[tools.quelle_region(ligne, colone)] <= 1 and int(money) >= 400 :
                    player.ajouter_orni(tools.quelle_region(ligne, colone))
                    compteurs_orni[tools.quelle_region(ligne, colone)] = 5
                    money-=400

        for i in range(0,4) :
            if tableau_orni[i] == "DANGER" :
                for ligne in range(secteurs[i][0][0], secteurs[i][0][1]):
                    for colone in range(secteurs[i][1][0], secteurs[i][1][1]):
                        if(tableau_element[ligne][colone] == str(player.numjoueur)):
                            cible=[0,0]
                            densitee_cible=0
                            if(player.requests_remaining > 0):
                                for nouvelle_ligne in range(16) :
                                    for nouvelle_colone in range(18) :
                                        if [nouvelle_ligne, nouvelle_colone] not in forreuses_deplacee :
                                            zone = tools.adjacence(nouvelle_ligne, nouvelle_colone)
                                            densitee_tot = int(tableau_densitee[nouvelle_ligne][nouvelle_colone])
                                            for voisin in zone:
                                                if (tableau_element[voisin[0]][voisin[1]] != "X"):
                                                    densitee_tot += int(tableau_densitee[voisin[0]][voisin[1]])#//2
                                                else :
                                                    densitee_tot += int(tableau_densitee[voisin[0]][voisin[1]])
                                                
                                                if (densitee_tot > densitee_cible and tableau_element[nouvelle_ligne][nouvelle_colone] == "X" and tableau_orni[tools.quelle_region(nouvelle_ligne, nouvelle_colone)] != "DANGER"):
                                                    cible = [nouvelle_ligne, nouvelle_colone]
                                                    densitee_cible = densitee_tot
                                player.deplacer(ligne,colone,cible[0],cible[1])
                                forreuses_deplacee.append([cible[0], cible[1]])



        if(int(money) >= 3000 and nb_forreuse <= 10 and int(player.tour) <= 190) :
            cible=[0,0]
            densitee_cible=0
            for ligne in range(16) :
                for colone in range(18) :
                    zone = tools.adjacence(ligne, colone)
                    densitee_tot = int(tableau_densitee[ligne][colone])
                    for voisin in zone:
                        if (tableau_element[voisin[0]][voisin[1]] != "X"):
                            densitee_tot += int(tableau_densitee[voisin[0]][voisin[1]])#//2
                        else :
                            densitee_tot += int(tableau_densitee[voisin[0]][voisin[1]])
                        
                        if (densitee_tot > densitee_cible and tableau_element[ligne][colone] == "X"):
                            cible = [ligne, colone]
                            densitee_cible = densitee_tot
            player.ajouter_recolteuse(cible[0], cible[1])
        
        player.fin_tour()