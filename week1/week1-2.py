string = 'een123zin45 6met-632meerdere+7777getallen'


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

def getNumbers(s):
    list2 = []
    tmpStr = ''
    for item in s:
        if(item.isdigit()):
            tmpStr += item
        elif(tmpStr != ''):
            list2.append(tmpStr)
            tmpStr = ''

    return(list2)

print(getNumbers(string))