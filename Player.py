import socket

HOST = '127.0.0.1'
PORT = 1234

class Player():

    time_to_play=False
    name=""
    tour=0
    position_joueur=0 #Position du joueur dans le tour actuel
    requests_remaining=15
    numjoueur=0

    def __init__(self, name):
        self.name=name
        self.connectePlayer(self.name)
        self.epice_necessaire={"recolteuse":3000,
                          "usine":5000,
                          "orni":400,
                          "saboter":600}
    def applyRequest(self):
        if(self.requests_remaining<=1):
            self.fin_tour()
        self.requests_remaining-=1
        return self.getResponse()

    def getResponse(self):
        rep = self.client.recv(1024).decode().rstrip()
        # print(self.name,":",rep)
        if "DEBUT_TOUR" in rep:
            self.tour=rep.split('|')[-1]
            self.time_to_play=True
            self.position_joueur=(self.position_joueur+1)%4#A verifier
        return rep
    
    def play(self):
        return self.time_to_play
    
    def connectePlayer(self, name):
        self.client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.client.connect((HOST, PORT))
        response = self.getResponse()
        if(response=="NOM_EQUIPE"):
            self.client.sendall((name+'\n').encode())
            self.position_joueur=int(self.client.recv(1024).decode().rstrip()[-1])
            self.numjoueur=self.position_joueur
        else:
            print("Connection error")
        self.getResponse()
    
    def ajouter_recolteuse(self, numligne, numcolonne):
        self.client.sendall(("AJOUTERRECOLTEUSE|{}|{}".format(numligne,numcolonne)+'\n').encode())
        self.applyRequest()
    
    def ajouter_usine(self, numligne,numcolonne):
        self.client.sendall(("AJOUTERUSINE|{}|{}".format(numligne,numcolonne)+'\n').encode())
        self.applyRequest()

    def deplacer(self, numlignedep,numcolonnedep,numlignearr,numcolonnearr):
        self.client.sendall(("DEPLACER|{}|{}|{}|{}".format(numlignedep,numcolonnedep,numlignearr,numcolonnearr)+'\n').encode())
        self.applyRequest()

    def ajouter_orni(self,secteur):
        self.client.sendall(("AJOUTERORNI|{}".format(secteur)+'\n').encode())
        self.applyRequest()

    def saboter(self,secteur):
        self.client.sendall(("SABOTER|{}".format(secteur)+'\n').encode())
        self.applyRequest()

    def fin_tour(self):
        self.time_to_play=False
        self.client.sendall(("FINDETOUR"+'\n').encode())
        self.requests_remaining=15
        self.getResponse()
        self.getResponse()

    def infos_densite(self):
        self.client.sendall(("DENSITE"+'\n').encode())
        ans = self.applyRequest()
        if not ans:
            print(self.name, ": DENSITE: aucune réponse du serveur")
            return None
        ans = ans.rstrip()
        densite_liste = []
        for i in range(0, len(ans), 18):
            densite_liste.append([int(char) for char in ans[i:i+18]])
        return densite_liste
        
    def infos_elements(self):
        self.client.sendall(("ELEMENTS"+'\n').encode())
        ans = self.applyRequest()
        if not ans:
            print(self.name, ": ELEMENTS: aucune réponse du serveur")
            return None
        ans = ans.rstrip()
        densite_liste = []
        for i in range(0, len(ans), 18):
            densite_liste.append(list(ans[i:i+18]))
        return densite_liste
    
    def infos_warning(self):
        self.client.sendall(("WARNING"+'\n').encode()) 
        orni = self.applyRequest()
        return orni.split("|")
        
    def infos_scores(self):
        self.client.sendall(("SCORES"+'\n').encode()) 
        return self.applyRequest()
    
def assez_ressources(self, type_element, quantite) -> bool:
        """
        Vérifie si le joueur a suffisamment de ressources pour réaliser une action.
        True si c'est bon 
        False si c'est pas bon
        """
        return self.epice_necessaire[type_element]<=quantite
