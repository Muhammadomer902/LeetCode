class Solution(object):
    def countMaxOrSubsets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_or = 0
        for num in nums:
            max_or |= num 
        self.count = 0
        def backtrack(i, current_or):
            if i == len(nums):
                if current_or == max_or:
                    self.count += 1
                return
            backtrack(i + 1, current_or | nums[i])
            backtrack(i + 1, current_or)
        backtrack(0, 0)
        return self.count

        