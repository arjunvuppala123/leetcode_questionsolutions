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

    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        res = []
        self.inorder(root,res)
        res.sort()
        memo = {}
        for i in range(len(res)):
            checked = k - res[i]
            if checked in memo:
                return True
            memo[res[i]] = i
        return False