def B(n, k):
    if k in (0, n):
        return 1
    return B(n - 1, k - 1) + B(n - 1, k)

print(B(6,3))
#print(B(30,10))