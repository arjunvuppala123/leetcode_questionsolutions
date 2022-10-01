class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        my_dict,res = {},[]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                sum = i+j
                if sum in my_dict:
                    my_dict[sum].append(mat[i][j])
                else:
                    my_dict[sum] = [mat[i][j]]
        i = 0
        for key in my_dict:
            if i%2 == 0:
                res.append(my_dict[key][::-1])
            else:
                res.append(my_dict[key])
            i += 1
            
        res = list(itertools.chain.from_iterable(res))
        return res