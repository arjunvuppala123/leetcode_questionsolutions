class Solution:
    def bfs(self, root: TreeNode) -> int:
        if root == None:
            return []
        result = []
        
        queue = deque()
        queue.append(root)
        
        while queue:
            levelSize = len(queue)
            currentLevel = []
            for _ in range(levelSize):
                currNode = queue.popleft()
                currentLevel.append(currNode.val)
                if currNode.left:
                    queue.append(currNode.left)
                if currNode.right:
                    queue.append(currNode.right)
            result.append(sum(currentLevel)/levelSize)
        return result
    
    def averageOfLevels(self, root: TreeNode) -> int:
        return self.bfs(root)