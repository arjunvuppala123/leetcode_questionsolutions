# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self,root,res):
        if not root:
            res.append(None)
        if root:
            res.append(root.val)
            self.helper(root.left,res)
            self.helper(root.right,res)
        
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        res1 = []
        self.helper(p,res1)
        res2 = []
        self.helper(q,res2)
        return res1 == res2