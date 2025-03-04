class Solution(object):
    def checkPowersOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n > 0:
            if n % 3 == 2:  # If there's a '2' in the base-3 representation, return False
                return False
            n //= 3  # Reduce n by dividing by 3
        return True