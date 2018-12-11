
class hashNode:
    def __init__(self):
        self.hashSet = set()

    def __repr__(self):
        format = ''
        for key in self.hashSet:
            format += str(key) + ' '
        return format

    def insert(self, e):
        self.hashSet.add(e)

    def delete(self, e):
        for key in self.hashSet:
            if key == e:
                self.hashSet.remove(e)
                return True
        return False

    def rehash(self, new_len):
        return len(self.hashSet)

class separate_chaining_hashing:
    def __init__(self):
        self.hashTable = dict()

    def __repr__(self):
        s = ''
        print( self.hashTable)
        return s

    def search(self, e):
        i = e % 10
        for key in self.hashTable:
            if key == i:
                return 'number ' + str(e) + ' found.'
        return 'number ' + str(e) + ' not found.'

    def insert(self, e):
        i = e % 10
        for key in self.hashTable:
            if key == i:
                self.hashTable[key].insert(e)
        newHash = hashNode()
        newHash.insert(e)
        self.hashTable[i] = newHash



    def delete(self, e):
        i = e % 10
        for key in self.hashTable:
            if key == i:
                self.hashTable[key].delete(e)

    def rehash(self, new_len):
        total = 0
        for key in self.hashTable:
             total += self.hashTable[key].rehash(new_len)
        fill = total / len(self.hashTable)
        if fill > 0.75:
            new_len = len(self.hashTable) * 2
        return new_len



s = separate_chaining_hashing()
s.insert(1)
s.insert(3)
s.insert(7)
print(s)
print(s.search(3))
print(s.search(6))
s.delete(5)
s.delete(7)
print(s)
print(s.rehash(1))

