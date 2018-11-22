string = "((<>))"

def check_expressions(string):
    stack = []
    found = 0
    blockState = 0
    LGstate = 0
    for char in string:
        if char == "(":
            stack.append(char)

        elif char == ")":
            if blockState == 1 or LGstate == 1:
                return "niet geldig"
            for hook in stack:
                if hook == "(":
                    stack.pop(stack.index(hook))
                    found = 1
                    break
            if found != 1:
                return "niet geldig"
            else:
                found = 0


        elif char == "<":
            stack.append(char)
            LGstate = 1

        elif char == ">":
            for arrow in stack:
                if arrow == "<":
                    LGstate = 0
                    stack.pop(stack.index(arrow))
                    found = 1
                    break
            if found != 1:
                return "niet geldig"
            else:
                found = 0

        elif char == "[":
            stack.append(char)
            blockState = 1

        elif char == "]":
            for block in stack:
                if block == "[":
                    blockState = 0
                    stack.pop(stack.index(block))
                    found = 1
                    break
            if found != 1:
                return "niet geldig"
            else:
                found = 0

    if len(stack) == 0:
        return "geldig"
    else:
        return "niet geldig"


print(check_expressions(string))