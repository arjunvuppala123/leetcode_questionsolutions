class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        ruleDict = {"type":0,"color":1,"name":2}
        ind = ruleDict[ruleKey]
        ctr = 0
        for rec in items:
            if rec[ind] == ruleValue:
                ctr += 1
        return ctr