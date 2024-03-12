

class LinkedList:
    def __init__(self, data):
        self.data=data
        self.address = None

    def addToList(self, data):
        if self.data == None:
            self.data=data
        else:
            if self.address==None:
                self.address = LinkedList(data)
            else:
                self.address.addToList(data)


    def traverse(self, head):
        #print(head.data)
        while(head.address):
            #print("head ::", head)
            #print("head address ::", head.address)
            print(head.data)
            head = head.address
        print(head.data)

    def traverseTill(self, head, count):
        while(count>1):
            #print("head ::", head)
            #print("head address ::", head.address)
            print(head.data)
            head = head.address
            count = count -1
        print(head.data)

    def reverseAtK(self,head, k):
        if k < 1 or k > 5000:
            return False
        if head == None:
            return head
        prev = None
        curr = None
        nex = None
        curr = head
        # Reverse first k nodes of the linked list
        while (curr is not None and k>0):
            nex = curr.address
            curr.address = prev
            prev = curr
            curr = nex
            k = k-1
        self.traverse(prev)
        if curr:
            print("previous next ::", prev.data)
            print("current next ::", curr.data)
            head.address = self.reverseAtK(curr, 4)
        return prev
# 4-3-2-1-8-7-6-5-10-9
    def reverse(self, head):
        if(head==None):
            return head
        h1=head
        h2=None
        h3=None

        while(h1!= None):
            h3 = h1.address
            h1.address = h2
            h2 = h1
            h1 = h3

            #print("head ::")
        head = h2
        linkedlist.traverse(head)
        return head





linkedlist = LinkedList(1)
linkedlist.addToList(2)
linkedlist.addToList(3)
linkedlist.addToList(4)
linkedlist.addToList(5)
linkedlist.addToList(6)
linkedlist.addToList(7)
linkedlist.addToList(8)
linkedlist.addToList(9)
linkedlist.addToList(10)

linkedlist.traverse(linkedlist)
#linkedlist.reverse(linkedlist)

head = linkedlist.reverseAtK(linkedlist, 4)
linkedlist.traverse(head)
#linkedlist.traverseTill(linkedlist, 5)
#linkedlist.traverse(linkedlist)