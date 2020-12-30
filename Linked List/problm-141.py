# 141. Linked List Cycle
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
    def hasCycle1(self, head):
        pos = -1
        foo = {}
        curr = head
        while curr != None:
            foo[curr] = curr.val
            if curr.next in foo:
                # pos = list(foo.keys()).index(curr.next)
                return True
            curr = curr.next
        return pos >= 0
    
    def hasCycle(self, head):
        if not head or not head.next:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
        return True

# Test
solution = Solution()
# Expected: True
head = ListNode(3)
head.next = ListNode(2)
head.next.next = ListNode(0)
head.next.next.next = ListNode(-4)
head.next.next.next.next = head.next
print(solution.hasCycle(head))