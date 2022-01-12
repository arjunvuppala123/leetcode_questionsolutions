class Solution:
    def calculate(self, s: str) -> int:
        n = len(s)
        op = '+'
        curr = 0;
        k = 0
        stack = []
        for i in s:
            if i.isdigit():
                curr = (curr*10)+ int(i)
            if i.isdigit()==0 and i.isspace()==0 or k == n - 1:
                if op=='+':
                    stack.append(curr)
                elif op=='-':
                    stack.append(-curr)
                elif op=='*':
                    stack.append(stack.pop()*curr)
                elif op=='/':
                    stack.append(int(stack.pop()/curr))
                op = i
                curr = 0
            k += 1
        res = 0
        while stack:
            res += stack.pop()
        return res
                