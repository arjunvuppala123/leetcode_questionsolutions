# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = l1
        p2 = l2
        num1 = []
        num2 = []
        
        while p1:
            num1.append(p1.val)
            p1 = p1.next
        while p2:
            num2.append(p2.val)
            p2 = p2.next
            
        num1 = num1[::-1]
        num2 = num2[::-1]
        m = len(num1)
        n = len(num2)
        n1 = 0
        n2 = 0
        
        for i in range(0,m):
            n1 += num1[i]*(10**(i))
        for i in range(0,n):
            n2 += num2[i]*(10**(i))
            
        res = n1+n2
        res = [int(x) for x in str(res)]
        
        result = ListNode(0)
        tot_link = result
        for i in res:
            tot_link.next = ListNode(i)
            tot_link = tot_link.next   
            
        return result.next
    
     
        