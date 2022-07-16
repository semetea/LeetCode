from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = None
        while head:
            n = head.next
            head.next, p, head = p, head, n
        return p


head = ListNode([1, 2, 3, 4, 5])
print(head.next)
print(Solution().reverseList(head))
