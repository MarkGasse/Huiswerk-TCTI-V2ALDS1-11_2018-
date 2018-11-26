from week2_2 import *

def check_expressions(stringHaakjes):
    stack = mystack()
    startChars = ['(','[','<']
    endChars = [')',']','>']

    for char in stringHaakjes:
        if char in startChars:
            stack.push(char)
        elif char in endChars:
            prevChar = stack.pop()

            if(char == ')' and prevChar != '('):
                return False
            elif (char == ']' and prevChar != '['):
                return False
            elif (char == '>' and prevChar != '<'):
                return False
            elif prevChar == None:
                return False

    if stack.isEmpty():
        return True
    else:
        return False


print(" Should be True:")
stringHaakjes1 = "((<>)())"
print(check_expressions(stringHaakjes1))

stringHaakjes2 = "[(<>)]()(()()) "
print(check_expressions(stringHaakjes2))

stringHaakjes3 = "((<>))"
print(check_expressions(stringHaakjes3))

print(" Should be False:")
stringHaakjes4 = "([)]"
print(check_expressions(stringHaakjes4))

stringHaakjes5 = "(((<)>))"
print(check_expressions(stringHaakjes5))

stringHaakjes6 = "(((<>))"
print(check_expressions(stringHaakjes6))

stringHaakjes7 = ")((<>))"
print(check_expressions(stringHaakjes7))

stringHaakjes8 = "(())("
print(check_expressions(stringHaakjes8))
