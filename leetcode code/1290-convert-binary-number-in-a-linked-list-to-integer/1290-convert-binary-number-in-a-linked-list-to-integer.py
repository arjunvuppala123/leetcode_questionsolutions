# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        num = 0
        temp = head
        temp2 = head
        length = -1
        
        while temp:
            length += 1
            temp = temp.next
        
        while temp2:
            num += temp2.val*(2**length)
            length -= 1
            temp2 = temp2.next
        
        return num