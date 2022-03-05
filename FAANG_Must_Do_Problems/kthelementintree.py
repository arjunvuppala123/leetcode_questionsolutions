# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self,root,res):
        if root:
            self.inorder(root.left,res)
            res.append(root.val)
            self.inorder(root.right,res)
        return res
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []
        self.inorder(root,arr)
        arr.sort()
        return arr[k-1]
        