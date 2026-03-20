class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        rarr = s.split(' ');count = 0
        for i in rarr:
            if i!='':
                count+=1
        return count