import random

""" description

Return
-----
aantalgevonden: int
    returns the quantity of list with a double integer
"""

def kans():
    verjaardagen = []
    aantalGevonden = 0
    for lijsten in range(100):
        random.seed(None)
        for personen in range(23):
            verjaardagen.append(random.randint(1,366))
        #print(list4)
        for datum in verjaardagen:
            verjaardagen.remove(datum)
            for datum2 in verjaardagen:
                if(datum == datum2):
                    aantalGevonden += 1
                    break

        verjaardagen = []

    return(aantalGevonden)

print(kans()/100)