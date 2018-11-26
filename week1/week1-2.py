zin = 'een123zin45 6met-632meerdere+7777getallen1'


""" description

Parameters
 ---------
s : string
    giving the function a sentence to check for integers

Return
-----
list2: int
    returning list with integers
"""

def getNumbers(zin):
    integerList = []
    tmpZin = ''
    for char in zin:
        if(char.isdigit()):
            tmpZin += char
        elif  tmpZin != '' :
            integerList.append(int(tmpZin))
            tmpZin = ''

    if tmpZin != '':
        integerList.append(int(tmpZin))

    return(integerList)

print(getNumbers(zin))