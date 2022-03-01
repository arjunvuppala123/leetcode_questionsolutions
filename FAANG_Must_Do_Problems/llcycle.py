# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        ptr1 = head
        while ptr1 and ptr1.next:
            ptr1 = ptr1.next.next
            head = head.next
            if head==ptr1:
                return True
        return False