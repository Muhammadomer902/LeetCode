class Solution(object):
    def largestAltitude(self, gain):
        max = 0;sum = 0
        for i in gain:
            sum+=i
            if sum>max:
                max = sum
        return max
        