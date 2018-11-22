

def mybin(n,list=None):
    if list == None:
        list = []

    if n >= 0:
        n /= 2
        rem = n % 2
        list.append(rem)
        return mybin(n,list)
    else:
        string = ""
        while len(list) != 0:
            string += str(list.pop())

        return string;




print(mybin(100))