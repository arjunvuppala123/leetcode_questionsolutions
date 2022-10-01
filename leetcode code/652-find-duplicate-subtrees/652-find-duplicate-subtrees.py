# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        my_dict = defaultdict(lambda: 0)
        res = set()
        
        def traverse(root,my_dict,res):
            if root:
                left = traverse(root.left,my_dict,res)
                right = traverse(root.right,my_dict,res)
                subtree = (root.val,left,right)
                my_dict[subtree] = my_dict[subtree] + 1
                if my_dict[subtree] == 2:
                    res.add(root)
                return subtree
            return None
        
        traverse(root,my_dict,res)
        return list(res)