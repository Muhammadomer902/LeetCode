class Solution(object):
    def closestPrimes(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        def sieve(n):
            is_prime = [True] * (n + 1)
            is_prime[0] = is_prime[1] = False
            for i in range(2, int(n**0.5) + 1):
                if is_prime[i]:
                    for j in range(i * i, n + 1, i):
                        is_prime[j] = False
            return is_prime
        
        primes = sieve(right)
        prime_list = [i for i in range(left, right + 1) if primes[i]]
        
        if len(prime_list) < 2:
            return [-1, -1]
        
        min_gap = float('inf')
        ans = [-1, -1]
        
        for i in range(len(prime_list) - 1):
            gap = prime_list[i + 1] - prime_list[i]
            if gap < min_gap:
                min_gap = gap
                ans = [prime_list[i], prime_list[i + 1]]
        
        return ans