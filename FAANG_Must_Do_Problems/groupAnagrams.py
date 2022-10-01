class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for word in strs:
            sortedWord = "".join(sorted(word))
            if sortedWord not in res:
                res[sortedWord] = [word]
            else:
                res[sortedWord].append(word)
        final = []
        for key in res:
            final.append(res[key])
        return final
        