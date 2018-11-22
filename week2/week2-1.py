def machtv3(a,n):
    assert n > 0

    m = 1
    while n > 0:
        if n%2 == 0:
            a *= a
            n /= 2
            m += 1
        else:
            n -= 1
    return m

print(machtv3(2,10000))