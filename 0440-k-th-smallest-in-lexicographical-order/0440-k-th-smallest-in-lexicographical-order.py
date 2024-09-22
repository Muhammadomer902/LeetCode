class Solution(object):
    def findKthNumber(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        def count_steps(prefix, n):
            """ Count the steps between prefix and the next lexicographical number """
            steps = 0
            current = prefix
            next_prefix = prefix + 1
            while current <= n:
                steps += min(n + 1, next_prefix) - current
                current *= 10
                next_prefix *= 10
            return steps
        
        current = 1
        k -= 1  
        
        while k > 0:
            steps = count_steps(current, n)
            if steps <= k:
                current += 1
                k -= steps
            else:
                current *= 10
                k -= 1
        
        return current
