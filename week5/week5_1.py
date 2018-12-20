class myqueue(list):
    def __init__(self, a=[]):
        list.__init__(self, a)

    def dequeue(self):
        return self.pop(0)

    def enqueue(self, x):
        self.append(x)


class Vertex:
    def __init__(self, data):
        self.data = data

    def __repr__(self):  # voor afdrukken
        return str(self.data)

    def __lt__(self, other):  # voor sorteren
        return self.data < other.data


import math

INFINITY = math.inf  # float("inf")


def vertices(G):
    return sorted(G)


def edges(G):
    return [(u, v) for u in vertices(G) for v in G[u]]


v = [Vertex(i) for i in range(8)]

G = {v[0]: [v[4], v[5]],
     v[1]: [v[4], v[5], v[6]],
     v[2]: [v[4], v[5], v[6]],
     v[3]: [v[7]],
     v[4]: [v[0], v[1], v[5]],
     v[5]: [v[1], v[2], v[4]],
     v[6]: [v[2], v[1]],
     v[7]: [v[3]]}

G2 = {v[0]: [v[4], v[5]],
     v[1]: [v[4], v[5], v[6]],
     v[2]: [v[4], v[5], v[6]],
     v[4]: [v[0], v[1], v[5]],
     v[5]: [v[1], v[2], v[4]],
     v[6]: [v[2], v[1]]}

G3 = {v[0]: [v[4], v[5]],
     v[1]: [v[4], v[6]],
     v[2]: [ v[5]],
     v[3]: [v[7]],
     v[4]: [v[0], v[1]],
     v[5]: [v[0], v[2]],
     v[6]: [v[1]],
     v[7]: [v[3]]}

G4 = {v[0]: [v[1], v[3]],
     v[1]: [v[0], v[2]],
     v[2]: [ v[1], v[3], v[4]],
     v[3]: [v[0], v[2]],
     v[4]: [v[2], v[5], v[6]],
     v[5]: [v[4], v[6]],
     v[6]: [v[4] , v[5], v[7]],
     v[7]: [v[6]]}

G5 = {v[0]: [v[1], v[2]],
     v[1]: [v[0], v[3]],
     v[2]: [ v[0], v[3]],
     v[3]: [v[1], v[2], v[4], v[6]],
     v[4]: [v[3], v[5], v[6], v[7]],
     v[5]: [v[4], v[6]],
     v[6]: [v[3], v[4] , v[5], v[7]],
     v[7]: [v[4], v[6]]}

G6 = {v[0]: [v[2]],
     v[2]: [v[1], v[4]],
     v[4]: [v[2], v[6]],
     v[6]: [v[4]]}

print("vertices(G):", vertices(G))
print("edges(G):", edges(G))


def clear(G):
    for v in vertices(G):
        k = [e for e in vars(v) if e != 'data']
        for e in k:
            delattr(v, e)


def BFS(G, s):
    V = vertices(G)
    s.predecessor = None
    s.distance = 0
    for v in V:
        if v != s:
            v.distance = INFINITY  # v krijgt het attribuut 'distance'
    q = myqueue()
    q.enqueue(s)
    #    print("q:", q)
    while q:
        u = q.dequeue()
        for v in G[u]:
            if v.distance == INFINITY:  # v is nog niet bezocht
                v.distance = u.distance + 1
                v.predecessor = u  # v krijgt het attribuut 'predecessor'
                q.enqueue(v)


# print("q:", q)
BFS(G, v[1])


def show_tree_info(G):
    print('tree:', end=' ')
    for v in vertices(G):
        print('(' + str(v), end='')
        if hasattr(v, 'distance'):
            print(',d:' + str(v.distance), end='')
        if hasattr(v, 'predecessor'):
            print(',p:' + str(v.predecessor), end='')
        print(')', end=' ')
    print()


show_tree_info(G)


def show_sorted_tree_info(G):
    print('sorted tree:')
    V = vertices(G)
    #    V = [v for v in V if hasattr(v,'distance') and hasattr(v,'predecessor')]
    V.sort(key=lambda x: (x.distance, x.predecessor))
    d = 0
    for v in V:
        if v.distance > d:
            print()
            d += 1
        print('(' + str(v) + ',d:' + str(v.distance) + ',p:'
              + str(v.predecessor), end='')
        print(')', end=' ')
    print()


#show_sorted_tree_info(G)

def path_BFS(G, u, v):
    BFS(G, u)
    a = []
    if hasattr(v, 'predecessor'):
        current = v
        while current:
            a.append(current)
            current = current.predecessor
        a.reverse()
    return a


print("path_BFS(G,v[1],v[7]):", path_BFS(G, v[1], v[7]))

clear(G)

print("\n------Opdracht week5_1------\n")

def is_connected(G):
    notes = vertices(G)
    for pos in notes:
        check = path_BFS(G,v[0],pos)
        if check == []:
            return False
    return True

print("Should be False: " , is_connected(G))
print("Should be True: " , is_connected(G2))

print("\n----------------------------")

print("\n------Opdracht week5_2------\n")

def no_cycles(G):
    seen = []
    parent = -1

    for i in vertices(G):
        for pos in edges(G):
            if pos[0] == i:
                if pos[1] in seen and parent is pos[1]:
                    return False
                else:
                    seen.append(pos[1])
        parent = i
    return True



print("should be True: ",no_cycles(G3))
print("should be False: ",no_cycles(G))


print("\n----------------------------")

print("\n------Opdracht week5_3------\n")

def get_bridges(G):
    bridges = []

    if not is_connected(G):
        return False
    
    for pos in edges(G):

        G[pos[0]].remove(pos[1])
        G[pos[1]].remove(pos[0])

        if not is_connected(G):
            bridges.append(pos)

        G[pos[0]].append(pos[1])
        G[pos[1]].append(pos[0])

    return bridges

#print("bridges: [(2,4),(4,2),(6,7),(7,6)] == ", get_bridges(G4))

print("\n----------------------------")

print("\n------Opdracht week5_4------\n")

def is_strongly_connected(G):
    reverse = {}
    if not is_connected(G):
        return False

    for pos in vertices(G):
        reverse[pos] = []
    for pos in vertices(G):
        for value in G[pos]:
            reverse[value].append(pos)

    if not is_connected(reverse):
        return False
    return True

print("should be False: ", is_strongly_connected(G))
print("should be True: ", is_strongly_connected(G2))

print("\n----------------------------")

print("\n------Opdracht week5_5------\n")

def is_Euler_graph(G):
    notes = vertices(G).copy()
    for i in notes:
        if int(str(i)) % 2 is not 0:
           return False
    return True

print("Should be False: ", is_Euler_graph(G))
print("Should be True: ", is_Euler_graph(G6))


def get_Euler_circuit(G,s): # nog afmaken
    circuit = []
    current = s
    circuit.append(current)
    while edges(G) is not []:
        for next in G[vertices(G)[current]]:
            if (current,next) is not get_bridges(G) and next != current:
                prev = current
                current = next
        circuit.append(current)
        G[current].remove(prev)
        G[prev].remove(current)

    return circuit

#print(get_Euler_circuit(G5,0))


print("\n----------------------------")