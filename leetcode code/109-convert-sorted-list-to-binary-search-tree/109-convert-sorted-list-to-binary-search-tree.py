# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        temp2 = head
        l1 = []
        
        while temp2:
            l1.append(temp2.val)
            temp2 = temp2.next
        
        def convertToBinaryTree(nums):
            length = len(nums)
            if not length:
                return None
            mid = length//2
            return TreeNode(nums[mid],convertToBinaryTree(nums[:mid]),convertToBinaryTree(nums[mid+1:]))
        
        return convertToBinaryTree(l1)