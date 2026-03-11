class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        unique = set(candyType); num = len(candyType)/2
        if num<len(unique):
            return num
        else:
            return len(unique)