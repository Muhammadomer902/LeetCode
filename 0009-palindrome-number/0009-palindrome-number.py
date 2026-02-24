class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        arr = []
        if x<0:
            return False
        while x>0:
            digit=x%10
            x=x/10
            arr.insert(0,digit)
        left = 0;right = len(arr)-1
        while left<right:
            if arr[left]!=arr[right]:
                return False
            left+=1
            right-=1
        return True