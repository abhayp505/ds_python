'''Longest Univalue Path'''

from queues import push, pop, queues

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:

    head = None
    current = None
    def insert(self, data):


        if self.head == None:
            self.head = Node(data)
            self.current = self.head
            push(self.head)
            push(self.head)

        else:
            current = pop()
            print("current ::", current.data)
            #print("queue ::", queues())
            if current.left == None:
                current.left = Node(data)
                push(current.left)
                push(current.left)

            elif current.right == None:
                current.right = Node(data)
                push(current.right)
                push(current.right)


    def inorder(self, head):

        if head.left:
            self.inorder(head.left)
        print(head.data, end=' ')
        if head.right:
            self.inorder(head.right)

    def preorder(self, head):

        print(head.data, end=' ')
        if head.left:
            self.preorder(head.left)
        if head.right:
            self.preorder(head.right)

    def postOrder(self, head):
        if head is None:
            return
        if head.left:
            self.postOrder(head.left)
        if head.right:
            self.postOrder(head.right)
        print(head.data, end=' ')

    # Definition for a binary tree node.
    # class TreeNode:
    #     def __init__(self, val=0, left=None, right=None):
    #         self.val = val
    #         self.left = left
    #         self.right = right
    class Solution:

        queue = []

        def inorder(self, root):

            if root.left:
                self.inorder(root.left)
            # element = self.push(root.val)
            self.queue.append(root.val)
            print(root.val)
            if root.right:
                self.inorder(root.right)

        def longestUnivaluePath(self, root) -> int:
            if root == None:
                return 0
            if root.left == None and root.right == None:
                return 0

            self.queue.clear()
            self.inorder(root)
            flag = True
            element = None
            longestSum = 0
            count = 0
            print("queue ::", self.queue)

            for value in self.queue:
                if value == element:
                    count = count + 1
                else:
                    element = value
                    if count > longestSum:
                        longestSum = count
                    count = 0
                print("loop 2 ::", value, " ", element, " ", count, " ", flag)
            if count > longestSum:
                longestSum = count
            print("longestSum ::", longestSum)
            return longestSum

    """
    loop :: 1   None   0   True
    loop 2 :: 1   1   0   True
    loop :: 4   1   0   True
    loop 2 :: 4   4   0   True
    loop :: 1   4   0   True
    loop 2 :: 1   1   0   True
    loop :: 5   1   0   True
    loop 2 :: 5   5   0   True
    loop :: 5   5   0   True
    loop 2 :: 5   5   1   True
    loop :: 5   5   1   True
    loop 2 :: 5   5   2   True
    """

    # def push(data):
    #     if data is None:
    #         return
    #     else:
    #         self.queue.append(data)

    # def pop():
    #     element = queue[0]
    #     self.queue.pop(0)
    #     return element

    # def length(self):
    #     size = len(self.queue)
    #     return size

    # def queues():
    #     return self.queue

    def mains(self):
        list = [5,4,5,1,1,6,5]

        for element in list:
            print("element ::", element)
            self.insert(element)

        self.inorder(self.head)
        print('\n')
        self.preorder(self.head)
        print('\n')
        self.postOrder(self.head)

bt = BinaryTree()
bt.mains()