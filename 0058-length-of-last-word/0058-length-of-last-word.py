class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        splitS = s.split(" ")
        last = len(splitS)-1
        while splitS[last]=='':
            last-=1
        return len(splitS[last])