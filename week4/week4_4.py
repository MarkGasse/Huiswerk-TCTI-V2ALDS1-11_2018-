def F(n):
    A = []
    for i in range(len(A)):
        A[i,0] = 1
        for j in range(len(A[i])):
            A[0,j] = 1
            if j >= m[i]:
                A[i,j] = A[i-1,j] + A[i,j-m[i]]
            elif j < m[i]:
                A[i,j] = A[i-1,j]
    return A

n = 7
m = [1,2,5,10,20,50,100,200,500,1000,2000,5000,10000]

print(F(n))
