class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        pointer = 0
        s = s.split()
        for char in s:
            if(char.isdigit()):
                if(pointer<int(char)):
                    pointer=int(char)
                else:
                    return False
        return True