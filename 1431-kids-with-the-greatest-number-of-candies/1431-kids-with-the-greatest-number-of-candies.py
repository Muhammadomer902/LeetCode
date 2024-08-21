class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        size = len(candies)
        arr = [False]*size
        for i in range(size):
            if candies[i]+extraCandies>=max(candies):
                arr[i]=True
        return arr