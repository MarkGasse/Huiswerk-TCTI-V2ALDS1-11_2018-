def swap(a,i,j):
    a[i],a[j] = a[j],a[i]

import random

def qsort(a,low=0,high=-1):
    checks = 0
    if high == -1:
        high = len(a) -1
    if low < high:
        swap(a,low, random.randint(low,high))
        m = low
        for j in range(low+1,high+1):
            if a[j] < a[low]:
                checks += 1
                m += 1
                swap(a,m,j)
                    # low < i <= m : a[i] < a[low]
                    #  i > m        : a[i] >= a[low]
                swap(a,low,m)
                    #  low <= i < m : a[i] < a[m]
                    #  i > m        : a[i] >= a[m]
                if m > 0:
                    qsort(a,low,m-1)
                qsort(a,m+1,high)
    print(checks)

list = []

for i in range(0,10):
    list.append(i)

qsort(list)