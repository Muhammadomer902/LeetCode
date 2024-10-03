class Solution:
    def minSubarray(self, nums, p):
        total_sum = sum(nums)
        target_remainder = total_sum % p
        if target_remainder == 0:
            return 0 
        prefix_sum = 0
        prefix_mod_map = {0: -1} 
        min_len = len(nums)
        found = False
        for i, num in enumerate(nums):
            prefix_sum += num
            current_mod = prefix_sum % p
            desired_mod = (current_mod - target_remainder) % p
            if desired_mod in prefix_mod_map:
                found = True
                min_len = min(min_len, i - prefix_mod_map[desired_mod])
            prefix_mod_map[current_mod] = i
        
        return min_len if found and min_len < len(nums) else -1
