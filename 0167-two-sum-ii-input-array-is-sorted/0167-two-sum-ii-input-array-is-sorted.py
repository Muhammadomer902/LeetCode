class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0; right = len(numbers) -1
        while left<right:
            if numbers[right]+numbers[left] < target:
                left+=1
            elif numbers[right]+numbers[left] > target:
                right-=1
            else:
                return [left+1,right+1]
        return []