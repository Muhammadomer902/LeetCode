class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g = sorted(g)
        s = sorted(s)
        count = 0;j =0;i = 0
        while j<len(s) and i<len(g):
            if s[j] >= g[i]:
                count+=1
                i+=1
            j+=1
        return count
