ROWS = 16
COLS = 18

def inside(numligne, numcolonne, rows=ROWS, cols=COLS):
    return 0 <= numligne < rows and 0 <= numcolonne < cols

def adjacence(numligne, numcolonne):
    if not inside(numligne, numcolonne):
        return []
    if numligne % 2 == 1:
        candidates = [
            (numligne + 1, numcolonne + 1),
            (numligne, numcolonne + 1),
            (numligne + 1, numcolonne),
            (numligne, numcolonne - 1),
            (numligne - 1, numcolonne),
            (numligne - 1, numcolonne + 1),
        ]
    else:
        candidates = [
            (numligne - 1, numcolonne - 1),
            (numligne - 1, numcolonne),
            (numligne, numcolonne + 1),
            (numligne, numcolonne - 1),
            (numligne + 1, numcolonne - 1),
            (numligne + 1, numcolonne),
        ]
    return [(r, c) for r, c in candidates if inside(r, c)]

# def is_adjacent(numligne1, numcolonne1, numligne2, numcolonne2):
#     if not inside(numligne1, numcolonne1) or not inside(numligne2, numcolonne2):
#         return False
#     return (numligne2, numcolonne2) in adjacence(numligne1, numcolonne1)

def adjacence_niveau_2(numligne, numcolonne):
    voisins_niveau_2=[]
    voisins = adjacence(numligne, numcolonne)
    for voisin in voisins:
        voisins_niveau_2.extend(adjacence(voisin[0], voisin[1]))
    voisins_niveau_2=list(set(voisins_niveau_2))
    return voisins_niveau_2

def matrice_usine(elements):
    matrice = [[0 for _ in range(18)] for _ in range(16)]
    for i in range(16):
        for j in range(18):
            if elements[i][j] == "U":
                voisins_niveau_2=adjacence_niveau_2(i,j)
                for voisin in voisins_niveau_2:
                    matrice[voisin[0]][voisin[1]]=1
    return matrice

    

def recalc_densite(densite, elements):
    new_densite=[[0 for _ in range(18)] for _ in range(16)]
    usine=matrice_usine(elements)
    for i in range(16):
        for j in range(18):
            new_densite[i][j]=densite[i][j]+usine[i][j]
    return new_densite

def parse_densite(densite):
    densite_liste = []
    for i in range(0, len(densite), 18):
        densite_liste.append([int(char) for char in densite[i:i+18]])
    return densite_liste

element = [[0 for _ in range(18)] for _ in range(16)]
element[1][1]="U"
element[10][10]="U"
element[1][2]="U"

densite_string = "111131211111112234112242311111212333111234421111133332233233211111233232123322221111144121112211121111332111322121233221221211323233322111121111333433434312321122333433432312221322232443322323222132424344443334221232324344323443421132333243112322211111232221112322111111112111111222111111"
densite=parse_densite(densite_string)

print(recalc_densite(densite, element))