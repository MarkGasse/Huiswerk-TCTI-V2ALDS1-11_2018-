integerList = [1 , 2, 3, 5, 7, 3, 1]
#list = [1 , 'H', 3, 5, 7, 3, 1]

""" description

Parameters
 ---------
list : int
    for checking highest number in list

Return
-----
max: int
    returns max integer in list or returns error if element is not of type int or double
"""
def mymax(integerList):
    max = 0
    if(len(integerList) == 0):
        return(-1)


    for item in integerList:
        assert type(item) is int, "fail"
        if(max < item):

            max = item
    return(max)

print(mymax(integerList))