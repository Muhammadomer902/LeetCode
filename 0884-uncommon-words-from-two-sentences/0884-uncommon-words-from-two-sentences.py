class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        s1  = s1.split(" ");s2 = s2.split(" ");out=[]
        for i in range(len(s1)):
            if s1[i] not in s2:
                if s1[i] not in s1[:i] and s1[i] not in s1[i+1:]:
                    out.append(s1[i])
        for i in range(len(s2)):
            if s2[i] not in s1:
                if s2[i] not in s2[:i] and s2[i] not in s2[i+1:]:
                    out.append(s2[i])
        return out