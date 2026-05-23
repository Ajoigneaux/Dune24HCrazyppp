import socket

HOST = '127.0.0.1'
PORT = 1234

class Player():

    time_to_play=False
    name=""
    tour=0

    def __init__(self, name):
        self.name=name
        self.connectePlayer(self.name)

    def getResponse(self):
        rep = self.client.recv(1024).decode().rstrip()
        if "DEBUT_TOUR" in rep:
            self.tour=rep.split('|')[-1]
            print(self.time_to_play)
            self.time_to_play=True
            print(self.time_to_play)
        print(self.name,":",rep)
        return rep
    
    def play(self):
        return self.time_to_play
    
    def connectePlayer(self, name):
        self.client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.client.connect((HOST, PORT))
        response = self.getResponse()
        if(response=="NOM_EQUIPE"):
            self.client.sendall((name+'\n').encode())
            self.numJoueur=int(self.client.recv(1024).decode().rstrip()[-1])
        else:
            print("Connection error")
        self.getResponse()
    
    def ajouter_recolteuse(self, numligne, numcolonne):
        self.client.sendall(("AJOUTERRECOLTEUSE|{}|{}".format(numligne,numcolonne)+'\n').encode())
        self.getResponse()
    
    def ajouter_usine(self, numligne,numcolonne):
        self.client.sendall(("AJOUTERUSINE|{}|{}".format(numligne,numcolonne)+'\n').encode())
        self.getResponse()

    def deplacer(self, numlignedep,numcolonnedep,numlignearr,numcolonnearr):
        self.client.sendall(("DEPLACER|{}|{}|{}|{}".format(numlignedep,numcolonnedep,numlignearr,numcolonnearr)+'\n').encode())
        self.getResponse()

    def ajouter_orni(self,secteur):
        self.client.sendall(("AJOUTERORNI|{}".format(secteur)+'\n').encode())
        self.getResponse()

    def saboter(self,secteur):
        self.client.sendall(("SABOTER|{}".format(secteur)+'\n').encode())
        self.getResponse()

    def fin_tour(self):
        self.time_to_play=False
        self.client.sendall(("FINDETOUR"+'\n').encode())
        self.getResponse()

    def infos_densite(self):
        self.client.sendall(("DENSITE"+'\n').encode())
        self.getResponse()
        
    def infos_elements(self):
        self.client.sendall(("ELEMENTS"+'\n').encode())
        self.getResponse()
    
    def infos_warning(self):
        self.client.sendall(("WARNING"+'\n').encode()) 
        self.getResponse()
        
    def infos_scores(self):
        self.client.sendall(("SCORES"+'\n').encode())
        self.getResponse()
    

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


