class Solution(object):
    def findKthBit(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        def find_kth_bit(n, k):
            if n == 1:
                return '0'
            length = (1 << n) - 1  
            mid = (length // 2) + 1  
            if k == mid:
                return '1' 
            elif k < mid:
                return find_kth_bit(n - 1, k)
            else:
                mirrored_k = mid - (k - mid)
                return '1' if find_kth_bit(n - 1, mirrored_k) == '0' else '0'
        
        return find_kth_bit(n, k)
