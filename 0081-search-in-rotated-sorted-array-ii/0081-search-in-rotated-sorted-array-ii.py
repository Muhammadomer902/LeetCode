class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        size = len(nums)
        setnum = set(nums)
        if target not in setnum:
            return False
        return True
        # size = len(nums)
        # if size ==1 and nums[0]==target:
        #     return True
        # elif size ==1 and nums[0]!=target:
        #     return False
        # left=0;right = size-1;mid =-1
        # while left<=right and mid!=left and mid!=right:
        #     mid = int(left+(right-left)/2)

        #     if nums[mid] == target or nums[left]==target or nums[right]==target:
        #         return True
        #     elif (nums[mid]==nums[right]==nums[left]) or (nums[mid]<target and nums[right]<target and nums[left]<target) or (nums[mid]>target and nums[right]>target and nums[left]>target):
        #         right-=1
        #         left+=1
        #     elif (nums[mid]<target and nums[right]<target) or (nums[mid]>target and nums[left]<target):
        #         right = mid
        #         if mid==right:
        #             mid+=1
        #     elif (nums[mid]>target and nums[left]>target) or (nums[mid]<target and nums[right]>target):
        #         left = mid
        #         if mid==left:
        #             mid+=1

        # if nums[mid] == target or nums[left]==target or nums[right]==target:
        #     return True
        # return False
            
                