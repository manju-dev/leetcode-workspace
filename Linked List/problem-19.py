# 19. Remove Nth Node From End of List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    
    def __str__(self):
        foo = []
        current = self
        while current != None:
            foo.append(current.val)
            current = current.next
        return str(foo)

class Solution:
    def removeNthFromEnd1(self, head, n):
        foo = []
        node = head
        while node != None:
            foo.append(node)
            node = node.next 
        idx = len(foo) - n
        bar = foo[idx]
        if idx == 0:
            return foo[idx].next
        else:
            foo[idx - 1].next = bar.next
        return head
    
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy
        for i in range(n+1):
            first = first.next
        while first != None:
            first = first.next
            second = second.next
        second.next = second.next.next
        return dummy.next

# Test
solution = Solution()
# Expected: [1, 2, 3, 5]
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
print(solution.removeNthFromEnd(head, 2))