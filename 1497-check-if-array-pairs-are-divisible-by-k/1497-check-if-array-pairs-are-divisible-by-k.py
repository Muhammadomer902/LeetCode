class Solution(object):
    def canArrange(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: bool
        """
        remainder_count = [0] * k
        for num in arr:
            remainder = num % k
            if remainder < 0:
                remainder += k
            remainder_count[remainder] += 1
        
        if remainder_count[0] % 2 != 0:
            return False
        for i in range(1, k // 2 + 1):
            if remainder_count[i] != remainder_count[k - i]:
                return False
        
        return True

        