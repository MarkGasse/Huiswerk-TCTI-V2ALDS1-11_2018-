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
    listBool = []
    listNumbers = []

    for i in range(2,max):
        listNumbers.append(i)
        listBool.append(True)

    for item in listNumbers:
        m = item * item
        while m < max:
            m += item
            listBool[m-item-item] = False

    for index in range (len(listBool)):
        if(listBool[index] == False):
            listNumbers.remove(index)
    print(len(listNumbers))
    return(listNumbers)

print(priem(1000))
