class Solution(object):
    def maximumSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import defaultdict
        
        def sum_of_digits(n):
            return sum(int(digit) for digit in str(n))
        
        digit_sum_map = defaultdict(list)
        max_sum = -1
        
        # Group numbers by their sum of digits
        for num in nums:
            digit_sum = sum_of_digits(num)
            digit_sum_map[digit_sum].append(num)
        
        # Find the maximum sum of pairs
        for key in digit_sum_map:
            if len(digit_sum_map[key]) > 1:
                digit_sum_map[key].sort(reverse=True)
                max_sum = max(max_sum, digit_sum_map[key][0] + digit_sum_map[key][1])
        
        return max_sum
