class ListNode:
    def __init__(self,data,next_node):
        self.data = data
        self.next = next_node

    def __repr__(self):
       return str(self.data)


class MyCircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __repr__(self):
        s = ''
        current = self.head
        if current != None:
            s = s + str(current)
            current = current.next
        while current != self.head:
            s = s + " -> " + str(current)
            current = current.next
        if s == '':
            s = 'empty list'
        return s

    def addLast(self, e):
        if self.head == None:
            n = ListNode(e, None)
            self.tail = n
            self.head = n
            self.tail.next = self.head
        else:
            n = ListNode(e, self.head)
            self.tail.next = n
            self.tail = n
            self.tail.next = self.head

    def delete(self,e):
        if self.head != None:
            if self.tail.data == e:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.tail.next = self.head
        else:
            current = self.head
            while current.next != None and current.next.data != e:
                current = current.next
            if current.next != None:
                current.next = current.next.next
            if current.next == None:
                self.tail = current

mylist =  MyCircularLinkedList()
print(mylist)
mylist.addLast(1)
mylist.addLast(2)
mylist.addLast(3)
print(mylist)
mylist.delete(2)
print(mylist)
mylist.delete(1)
print(mylist)
mylist.addLast(4)
mylist.addLast(5)
print(mylist)
mylist.delete(4)
print(mylist)
