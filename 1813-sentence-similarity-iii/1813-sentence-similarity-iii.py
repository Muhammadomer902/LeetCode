class Solution(object):
    def areSentencesSimilar(self, sentence1, sentence2):
        """
        :type sentence1: str
        :type sentence2: str
        :rtype: bool
        """
        words1 = sentence1.split()
        words2 = sentence2.split()
        i = 0
        while i < min(len(words1), len(words2)) and words1[i] == words2[i]:
            i += 1
        j = 0
        while j < min(len(words1), len(words2)) and words1[-1 - j] == words2[-1 - j]:
            j += 1
        return i + j >= min(len(words1), len(words2))