import socket

HOST = '127.0.0.1'
PORT = 1234


class Player():
    def __init__(self, name):
        self.name=name
        self.client=self.connectePlayer(self.name)
        self.tour=1
        self.epice_necessaire={"recolteuse":3000,
                          "usine":5000,
                          "orni":400,
                          "saboter":600}

    def getResponse(self):
        rep = self.client.recv(1024).decode()
        print(self.name,":",rep)
        return rep
    
    def connectePlayer(self, name):
        client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        client.connect((HOST, PORT))
        print(name, ":", client.recv(1024).decode())
        client.sendall((name+'\n').encode())
        self.numJoueur=int(client.recv(1024).decode().rstrip()[-1])
        return client
    def ajouter_recolteuse(self, numligne, numcolonne):
        self.client.sendall(("AJOUTERRECOLTEUSE|{}|{}".format(numligne,numcolonne)+'\n').encode())
    
    def ajouter_usine(self, numligne,numcolonne):
        """
        """
        self.client.sendall(("AJOUTERUSINE|{}|{}".format(numligne,numcolonne)+'\n').encode())

    def deplacer(self, numlignedep,numcolonnedep,numlignearr,numcolonnearr):
        self.client.sendall(("DEPLACER|{}|{}|{}|{}".format(numlignedep,numcolonnedep,numlignearr,numcolonnearr)+'\n').encode())
        

    def ajouter_orni(self,secteur):
        self.client.sendall(("AJOUTERORNI|{}".format(secteur)+'\n').encode())

    def saboter(self,secteur):
        self.client.sendall(("SABOTER|{}".format(secteur)+'\n').encode())


    def fin_tour(self):
        self.client.sendall(("FINDETOUR"+'\n').encode())

    def infos_densite(self):
        self.client.sendall(("DENSITE"+'\n').encode())  
        
    def infos_elements(self):
        self.client.sendall(("ELEMENTS"+'\n').encode()) 
    
    def infos_warning(self):
        self.client.sendall(("WARINIG"+'\n').encode()) 
        
        
    def infos_scores(self):
        self.client.sendall(("SCORES"+'\n').encode()) 
    

    def is_adjacent(numligne1,numcolonne1,numligne2,numcolonne2):
        if((numligne1 in (0,15)) and (numligne2 in (0,15)) and (numcolonne1 in (0,18)) and (numcolonne2 in (0,18))):
            if (numligne1+1==numligne2) and (numcolonne1+1==numcolonne2):
                return True
            elif(numligne1==numligne2) and (numcolonne1+1==numcolonne2):
                return True
            elif(numligne1+1==numligne2) and (numcolonne1==numcolonne2):
                return True
            elif(numligne1==numligne2) and (numcolonne1-1==numcolonne2):
                return True
            elif(numligne1-1==numligne2) and (numcolonne1==numcolonne2):
                return True
            elif(numligne1-1==numligne2) and (numcolonne1+1==numcolonne2):
                return True
            else:
                return False

    def assez_ressources(self, type_element, quantite) -> bool:
        """
        Vérifie si le joueur a suffisamment de ressources pour réaliser une action.
        True si c'est bon 
        False si c'est pas bon
        """
        return self.epice_necessaire[type_element]<=quantite