import random

""" description

Return
-----
aantalgevonden: int
    returns the quantity of list with a double integer
"""

def kans():
    list4 = []
    aantalGevonden = 0
    for lists in range(100):
        random.seed(None)
        for personen in range(23):
            list4.append(random.randint(1,366))
        #print(list4)
        for datum in list4:
            list4.remove(datum)
            for datum2 in list4:
                if(datum == datum2):
                    aantalGevonden += 1
                    break

        list4 = []

    return(aantalGevonden)

print(kans()/100)