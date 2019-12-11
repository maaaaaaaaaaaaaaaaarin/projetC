
aEcrire = []

with open("serveur.c", 'r') as fileRead:
    line = fileRead.readline()
    cnt = 1
    while line:
        # Process la ligne du pdf de merde
        nouvelleLigne = line.split(' ', 1)
        if len(nouvelleLigne) > 1 and len(nouvelleLigne[0]) <= 2:
            howMany = len(nouvelleLigne)-1
            nouvelleLigne = nouvelleLigne[1:]
            print()
            nouvelleLigne = ' '.join(nouvelleLigne)
        else:
            nouvelleLigne = line
        if len(nouvelleLigne) <= 3:
            line = fileRead.readline()
            continue
        aEcrire.append(nouvelleLigne)
        line = fileRead.readline()
        cnt += 1
    print("Nombre de ligne du pdf de merde: %s" % (cnt))

with open("serveur.c", 'w+') as fileWrite:
    for ligne in aEcrire:
        fileWrite.write(ligne)
