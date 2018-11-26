class mystack():
    def __init__(self):
        self.stackList = []
        self.index = -1

    def push(self,item):
        self.stackList.append(item)
        self.index += 1

    def pop(self):
        if self.isEmpty():
           return None
        else:
            self.poppedItem = self.stackList[self.index]
            self.stackList.remove(self.poppedItem)
            self.index -= 1
            return self.poppedItem

    def peek(self):
        return self.stackList[self.index]

    def isEmpty(self):
        if self.index == -1:
            return True
        else:
            return False

#m = mystack()
#m.push(1)
#m.push(2)
#m.push(3)
#print(m.pop())
#print(m.peek())
#print(m.isEmpty())
