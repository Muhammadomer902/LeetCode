class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen = {};seenI = {};rIndex = 100000000000000
        for i in range(0,len(s)):
            if s[i] not in seen:
                seen[s[i]] = 1
                seenI[s[i]] = i
            else:
                seen[s[i]]+=1
        for i in set(s):
            if seen[i]==1 and seenI[i]<rIndex:
                rIndex = seenI[i]
        if rIndex!=100000000000000:
            return rIndex
        return -1
                
        