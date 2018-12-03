def voorkomen(file):
    dictVoorkomen = dict()
    with open(file, 'r') as infile:
        tekst = infile.read()
        for woord in tekst.split():
            if woord not in dictVoorkomen:
                dictVoorkomen[woord] = 1
            else:
                dictVoorkomen[woord] += 1
    return dictVoorkomen

def dictNaarFile(file, dictVoorkomen):
    with open(file, 'w') as outfile:
        for woord, aantal in sorted(dictVoorkomen.items()):
            outfile.write(woord + ',' + str(aantal) + '\n')


infile = 'tekst.txt'
outfile = 'dict.txt'
dictNaarFile(outfile, voorkomen(infile))


