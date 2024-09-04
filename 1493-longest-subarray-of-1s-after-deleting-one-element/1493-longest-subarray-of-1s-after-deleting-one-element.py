class Solution(object):
    def longestSubarray(self, nums):
        max1 =0;left_z = 0;right_z=0;z_count = 0
        for right_z in range(len(nums)):
            if nums[right_z]==0:
                z_count+=1
            
            while z_count>1:
                if nums[left_z]==0:
                    z_count-=1
                left_z+=1

            max1 = max(max1, right_z-left_z) 
        return max1
        
        

        