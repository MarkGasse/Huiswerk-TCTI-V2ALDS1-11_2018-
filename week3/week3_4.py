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


class TrieNode:
    def __init__(self, n = 0, data = None):
        if data == None:
            data = dict()
        self.n = n
        self.data = data

    def __repr__(self):
        return str([self.data, self.n])

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.end = ' '
		
    def __repr__(self):
        return str(self.root)

    def insert(self, woord):
        current = self.root
        if woord not in current.data.keys():
            current.data[woord] = TrieNode()
        current = current.data[woord]
        if self.end not in current.data.keys():
            current.data[self.end] = TrieNode()
        current.data[self.end].n += 1

    def find(self, woord):
        current = self.root
        if woord in current.data.keys():
            current = current.data[woord]
        else:
            return False
        return self.end in current.data.keys()

def readFile(file):
    myTrie = Trie()
    with open(file, 'r') as infile:
        tekst = infile.read()
        for woord in tekst.split():
            myTrie.insert(woord)
    return myTrie

print(readFile(infile))



