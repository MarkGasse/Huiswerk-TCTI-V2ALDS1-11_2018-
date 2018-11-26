def mybin(number):

    assert number >= 0

    if number == 0:
        return "0b"

    return ( mybin(number // 2) + str(number % 2) )

print(mybin(100))