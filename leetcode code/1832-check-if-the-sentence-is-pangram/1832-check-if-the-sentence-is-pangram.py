class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        sentences = set(sentence)
        return len(sentences) == 26