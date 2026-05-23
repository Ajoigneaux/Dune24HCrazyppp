import socket

HOST = '127.0.0.1'
PORT = 1234


class Player():
    def __init__(self, name):
        self.name=name
        self.client=self.connectePlayer(self.name)
        self.tour=1

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
    
    


