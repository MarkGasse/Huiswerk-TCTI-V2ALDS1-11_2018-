

def swap(a,i,j):
    a[i],a[j] = a[j],a[i]

import random

counter = 0
def qsort(a,low=0,high=-1):
    global counter
    counter += 1
    if high == -1:
        high = len(a) -1
    if low < high:
        swap(a,low, random.randint(low, high))
        m = low
        for j in range(low+1,high+1):
            if a[j] < a[low]:
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

def worst_case_qsort(a,low=0,high=-1):
    global counter
    counter += 1
    if high == -1:
        high = len(a) -1
    if low < high:
        swap(a,low,high)
        m = low
        for j in range(low+1,high+1):
            if a[j] < a[low]:
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


list = []
random.seed(None)
for i in range(10000):
    list.append(random.randint(1,10000))

qsort(list)
print(counter)

counter = 0
worst_case_qsort(list)
print(counter)