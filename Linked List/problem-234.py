# 234. Palindrome Linked List
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
    def isPalindrome1(self, head):
        if not head:
            return True
        foo = []
        curr = head
        while curr != None:
            foo.append(curr.val)
            curr = curr.next
        return foo == foo[::-1]
        
    def isPalindrome(self, head):
        fast = slow = head
        # find the mid node
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # reverse the second half
        node = None
        while slow:
            nxt = slow.next
            slow.next = node
            node = slow
            slow = nxt
        # compare the first and second half nodes
        while node: # while node and head:
            if node.val != head.val:
                return False
            node = node.next
            head = head.next
        return True

# Test
solution = Solution()
# Expected: True
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(2)
head.next.next.next.next = ListNode(1)
print(solution.isPalindrome(head))