# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def checkCycle(self,head):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True,slow
        return False,slow
        
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        flag,fast = self.checkCycle(head)
        if flag:
            while head != fast:
                head = head.next
                fast = fast.next
            return fast
        return None