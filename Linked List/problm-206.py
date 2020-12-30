# 206. Reverse Linked List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        outStr = ''
        current = self
        while current != None:
            outStr += str(current.val) + "->"
            current = current.next
        return outStr[:-2]

class Solution:
    def reverseList1(self, head):
        if not head:
            return None
        current = head.next
        previous = ListNode(head.val)
        previous.next = None
        while current != None:
            temp = current.next
            current.next = previous
            previous = current
            current = temp
        return previous
    
    def reverseList(self, head):
        if not head or not head.next:
            return head
        foo = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return foo

# Test
solution = Solution()
# Expected: 5->4->3->2->1
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
print(solution.reverseList(head))