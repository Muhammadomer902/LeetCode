from collections import defaultdict

class Solution(object):
    def countBadPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_pairs = len(nums) * (len(nums) - 1) // 2
        count_map = defaultdict(int)
        good_pairs = 0
        
        for i, num in enumerate(nums):
            key = num - i  # Compute nums[j] - j should be equal to nums[i] - i
            good_pairs += count_map[key]  # Count valid good pairs
            count_map[key] += 1  # Store occurrences
        
        return total_pairs - good_pairs