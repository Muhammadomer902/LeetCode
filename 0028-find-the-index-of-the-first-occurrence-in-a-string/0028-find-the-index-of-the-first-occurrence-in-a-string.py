class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(haystack)<len(needle):
            return -1
        
        i = 0;sizeN = len(needle)

        while i+sizeN<=len(haystack):
            window = haystack[i:i+sizeN]
            if window==needle:
                return i
            i+=1
        
        return -1