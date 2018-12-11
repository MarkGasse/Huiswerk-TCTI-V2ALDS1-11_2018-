hashValues = dict()
for number in range(1,100000000):
    x = number/100000000
    newHash = hash(x) % (2**32)

    if  newHash in hashValues:
        print("----------------")
        print(repr(x))
        print(repr(newHash))
        print(repr(hashValues[newHash]))
        print("----------------")
    else:
        hashValues[newHash] = x



