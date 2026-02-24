class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        reversedhalf = 0
        
        while x > reversedhalf:
            reversedhalf = reversedhalf * 10 + x % 10
            x //= 10
        
        return x == reversedhalf or x == reversedhalf // 10