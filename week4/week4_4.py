def F( m, n):
    rows = []
    for i in range(n + 1):
        rows.append(0)

    rows[0] = 1

    for j in range(0,len(m)):
        for k in range(m[j], n+1):
            rows[k] += rows[k - m[j]]

    return rows[n]

# Driver program to test above function
m = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]
n = 7
print("mogelijkheden:", F(m,n))

