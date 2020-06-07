class node:
    def __init__(self,data=None):
        self.data = data
        self.next =None

class linkedl:
    def __init__(self):
        self.head = node()

    def append(self,data):
        newnode = node(data)
        cur = self.head
        while cur.next!=None:
            cur=cur.next
        cur.next = newnode

    def lengthoflist(self):
        cur =self.head
        total = 0
        while cur.next!=None:
            total+=1
            cur=cur.next
        return total

    def popnode(self,targetnodedata):
        curnode = self.head


    def addupnodevales(self):


    def reverselist(self):


