class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen = set()
        while n not in seen:
            seen.add(n)
            temp = 0
            while n!=0:
                digit = n%10
                n = n/10
                temp = temp + digit**2
            n = temp
            if n==1:
                return True
        return False
        