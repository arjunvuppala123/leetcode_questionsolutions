class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        
        for c in s:
            if stack and stack[-1][0] == c:
                top = stack.pop()
                if top[1] < k - 1:
                    stack.append((c, top[1] + 1))
            else:
                stack.append((c, 1))
                    
        return "".join([i[0]*i[1] for i in stack])