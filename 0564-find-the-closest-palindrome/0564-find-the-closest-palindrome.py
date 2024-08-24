class Solution(object):
    @staticmethod
    def is_palindrome(s):
        return s == s[::-1]

    def nearestPalindromic(self,n):
        length = len(n)
        num = int(n)
        if num <= 10 or set(n) == {'0', '1'} and n[0] == '1' and n[-1] == '0':
            return str(num - 1)
        candidates = []
        prefix = int(n[:(length + 1) // 2])
        for diff in (-1, 0, 1):
            candidate = str(prefix + diff)
            if length % 2 == 0:
                candidates.append(candidate + candidate[::-1])
            else:
                candidates.append(candidate + candidate[-2::-1])
        candidates.append('9' * (length - 1)) 
        candidates.append('1' + '0' * (length - 1) + '1')
        candidates = [c for c in candidates if c != n]
        closest = min(candidates, key=lambda x: (abs(int(x) - num), int(x)))
        return closest
