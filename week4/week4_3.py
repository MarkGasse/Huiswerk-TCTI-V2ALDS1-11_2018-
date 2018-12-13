def B(n, k):
    result = 1
    if k > n - k:
        k = n - k
    for i in range(k):
        result /= (i + 1)
        result *= (n - i)
    return int(result)

print(B(6,3))
print(B(100,50))
