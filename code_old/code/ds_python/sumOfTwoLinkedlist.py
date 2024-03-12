# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    head = None

    def traverse(self, head):
        while (head.next):
            print(head.val)
            head = head.next
        print(head.val)

    def insert(self, data):
        current = self.head
        if self.head == None:
            self.head = ListNode(data)
            current = self.head
            return current
        while current.next:
            current = current.next
        current.next = ListNode(data)
        return current

    def addTwoNumbers(self, l1, l2):
        count = 0
        list3 = None

        carry = 0

        while l1 or l2:

            if l1 and l2:
                sum = l1.val + l2.val
                l1 = l1.next
                l2 = l2.next
            elif l2 == None:
                sum = l1.val
                l1 = l1.next
            elif l1 == None:
                sum = l2.val
                l2 = l2.next

            if sum >= 10 and carry == 0:
                carry = 1
                sum = sum % 10
            elif sum > 10 and carry == 1:
                carry = 1
                sum = (sum % 10) + carry
            else:
                sum = sum + carry
                if sum < 10:
                    carry = 0
                else:
                    carry = 1
                sum = sum % 10

            list3 = self.insert(sum)
        if carry == 1:
            list3 = self.insert(1)
        return self.head


"""
('sum 1 ::', 18)
('sum 2 ::', 8)
('sum 1 ::', 18)
('sum 3 ::', 9)
('sum 1 ::', 18)
('sum 3 ::', 9)
('sum 1 ::', 18)
('sum 3 ::', 9)
('sum 1 ::', 9)
('sum 5 ::', 0)
('sum 1 ::', 9)
('sum 5 ::', 0)
('sum 1 ::', 9)
('sum 5 ::', 0)
8
9
9
9
0
0
0
"""
