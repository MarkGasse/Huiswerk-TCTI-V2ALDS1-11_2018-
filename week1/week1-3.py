""" description

Parameters
 ---------
max : int
    for putting integers in a list until the max number is reached

Return
-----
list3: int
    list of all prime numbers
"""


def priem(max):
    listbool = []
    list3 = []

    for i in range(2,max):
        list3.append(i)
        listbool.append(True)

    for item in list3:
        m = item * item
        while m < max:
            m += item
            listbool[m-item-item] = False

    for index in range (len(listbool)):
        if(listbool[index] == False):
            list3.remove(index)

    return(list3)

print(priem(1000))