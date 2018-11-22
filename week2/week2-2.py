class mystack(list):
    def push(self,item):
        list.append(item)

    def pop(self,index):
        list.remove(list[index])

    def peek(self):
        if(len(list) != 0 ):
            return list[0]
        else:
            return None

    def isEmpty(self):
        if(len(list) == 0):
            return None
        else:
            return "Not empty"


list = [1,2]
m = mystack(list)
m.push(3)
print(list)
m.pop(0)
m.pop(0)
print(list)
print(m.peek())
print(list)
print(m.isEmpty())