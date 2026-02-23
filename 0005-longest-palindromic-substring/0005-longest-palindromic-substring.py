class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        size = len(s)
        maxLength = 0;start = 0
        
        if not s:
            return ""

        def expandForPalindrome(left, right):
            while left>=0 and right<size and s[left]==s[right]:
                left-=1
                right+=1
            return right-left-1
        
        for i in range(0,size):
            len1 = expandForPalindrome(i, i)
            len2 = expandForPalindrome(i, i+1)

            curMax = max(len1,len2)

            if curMax > maxLength:
                maxLength = curMax
                start = i - (curMax-1)//2
            
        return s[start:start + maxLength]