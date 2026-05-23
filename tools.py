def is_adjacent(numligne1,numcolonne1,numligne2,numcolonne2):
    if((numligne1 in (0,15)) and (numligne2 in (0,15)) and (numcolonne1 in (0,18)) and (numcolonne2 in (0,18))):
        if(numligne1%2==0):
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
        else:
            if (numligne1-1==numligne2) and (numcolonne1-1==numcolonne2):
                return True
            elif(numligne1-1==numligne2) and (numcolonne1==numcolonne2):
                return True
            elif(numligne1==numligne2) and (numcolonne1+1==numcolonne2):
                return True
            elif(numligne1==numligne2) and (numcolonne1-1==numcolonne2):
                return True
            elif(numligne1+1==numligne2) and (numcolonne1-1==numcolonne2):
                return True
            elif(numligne1+1==numligne2) and (numcolonne1==numcolonne2):
                return True
            else:
                return False
def ajdacence(numligne,numcolonne):
    if numligne%2==0:
        return [[numligne+1,numcolonne+1],[numligne,numcolonne+1],[numligne+1,numcolonne],[numligne,numcolonne-1],[numligne-1,numcolonne],[numligne-1,numcolonne+1]]
    else:
        return [[numligne-1,numcolonne-1],[numligne-1,numcolonne],[numligne,numcolonne+1],[numligne,numcolonne-1],[numligne+1,numcolonne-1],[numligne+1,numcolonne]]
        