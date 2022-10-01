class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        
        for word in path.split("/"):
            if word == '..':
                if stack:
                    stack.pop()
            elif word == '.' or not word:
                continue
            else:
                stack.append(word)
                    
        final_str = "/" + "/".join(stack)
        return final_str