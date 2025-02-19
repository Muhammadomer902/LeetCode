class Solution(object):
    def getHappyString(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        def backtrack(current):
            if len(current) == n:
                happy_strings.append(current)
                return
            for ch in "abc":
                if not current or current[-1] != ch:
                    backtrack(current + ch)
        
        happy_strings = []
        backtrack("")
        
        return happy_strings[k - 1] if k <= len(happy_strings) else ""
