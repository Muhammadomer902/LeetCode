class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        max = 0
        size = len(candies)
        arr = [False]*size
        for i in candies:
            if i>max:
                max = i
        for i in range(size):
            if candies[i]+extraCandies>=max:
                arr[i]=True
        return arr