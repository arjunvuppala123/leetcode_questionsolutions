class Solution:
    def largestInteger(self, num: int) -> int:
        odd = []
        even = []
        num = str(num)
        for n in num:
            if int(n)%2 == 0:
                even.append(n)
            else:
                odd.append(n)
        even.sort()
        odd.sort()
        num = list(num)
        for i in range(len(num)):
            if int(num[i])%2 == 0:
                num[i] = even.pop()
            else:
                num[i] = odd.pop()
        return int("".join(num))