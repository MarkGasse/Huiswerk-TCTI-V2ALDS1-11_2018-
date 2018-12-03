def check(a,i):  # ga na of i aan a toegevoegd kan worden
    n = len(a)
    return not (i in a or
                # niet in dezelfde kolom
                i+n in [a[j]+j for j in range(n)] or
                # niet op dezelfde diagonaal
                i-n in [a[j]-j for j in range(n)])
                # niet op dezelfde diagonaal

def printQueens(a):
    global b
    n = len(a)
    for i in range(n):
        for j in range(n):
            if a[i] == j:
                print("X",end= " ")
            else:
                print("*",end= " ")
        print()
    print()

def rsearch(N):
    for i in range(N):
        if check(a,i):
            a.append(i)
            if len(a) == N:
                b.append(a.copy())
            rsearch(N)
            del a[-1]

a = []
b = []
rsearch(8)
print(b)
#printQueens(a)
print("Aantal oplossingen = " + str(len(b)))