from queues import push, pop, length, queues

class BST:
    def __init__(self, data):
        self.data=data
        self.left = None
        self.right = None

    def insert(self, data):
        if self.data == None:
            self.data = data
        else:
            if data < self.data:
                if self.left == None:
                    self.left = BST(data)
                else:
                    self.left.insert(data)
            else:
                if self.right == None:
                    self.right = BST(data)
                else:
                    self.right.insert(data)

    def inorder(self,head):
        # if head is None:
        #     return
        #
        if head.left:
            self.inorder(head.left)
        print(head.data, end=' ')
        if head.right:
            self.inorder(head.right)

    def preOrder(self,head):
        # if head is None:
        #     return
        #
        print(head.data, end=' ')
        if head.left:
            self.preOrder(head.left)

        if head.right:
            self.preOrder(head.right)

    def postOrder(self, head):
        if head is None:
            return
        if head.left:
            self.postOrder(head.left)
        if head.right:
            self.postOrder(head.right)
        print(head.data, end=' ')



    def searchnode(self,data, head):
        print("current head data::", head.data)
        if head.data == data:
            print("current head data2::", head.data)
            print("current head ::", head)
            return head
        if data < head.data:
            print("current head 3 ::", head)
            head=self.searchnode(data, head.left)
        else:
            head=self.searchnode(data, head.right)
        return head

    def max(self, head):
        if head.right:
            self.max(head.right)
        else:
            print("max ::", head.data)
            return head

    def deleteNode(self, data, head):
        print(" deleteNode data head data and head::", data, head.data, head)
        current = self.searchnode(data, head)
        print(" deleteNode current current.data data ::", current, current.data, data)
        if not current.left and not current.right:
            print("deleteNode current.data current  None::", current.data, current )
            current.data = None
            print("deleteNode current.data current None::", current)
        elif current.left and not current.right:
            current = current.left
        elif current.right and not current.left:
            current = current.right
        else:
            temp = current.right
            while temp.left:
                temp = temp.left
            print("deleteNode current.data1 current::", current.data, current)
            current.data = temp.data
            print("deleteNode current.data2 current::", current.data, current)
            self.deleteNode(current.data, current.right)
        print("deleteNode finish current.data current::", current.data, current)
        return current


    def levelOrder(self, head):
        current = head
        if head is None:
            return
        else:
            print("length 1::", length())
            push(current)
            #print("queue element 1::", queues()[0].data)
            count = length()
            #print("length 2::", count)
            while length() != 0:
                element = pop()
                push(element.left)
                push(element.right)
                # print(element.data)
                count2 = length()
                que = queues()
                #print("lenght 2:", count2)
                print(element.data, end=' ')




if __name__ == '__main__':
    head = BST(5)
    # head.insert(7)
    # head.insert(3)
    # head.insert(4)
    # head.insert(9)
    # head.insert(8)
    # head.insert(2)
    # head.insert(0)
    # head.insert(10)
    # head.insert(1)
    # head.insert(6)

    head.insert(3)
    head.insert(2)
    head.insert(4)
    head.insert(8)
    head.insert(7)
    head.insert(6)
    head.insert(10)
    head.insert(9)


print("preOrder:: ")
head.preOrder(head)
print("\n")
print("inorder:: ")
head.inorder(head)
print("\n")
print("postOrder:: ")
head.postOrder(head)
#head.searchnode(8,head)
#head.max(head)
#head.searchnode(7, head)
#head.deleteNode(7, head)
#head.inorder(head)
print("\n")
head.levelOrder(head)





