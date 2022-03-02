class Solution:
    def reverseBits(self, n: int) -> int:
        orig_num = '{0:032b}'.format(n)
        rev_num = orig_num[::-1]
        return int(rev_num,2)