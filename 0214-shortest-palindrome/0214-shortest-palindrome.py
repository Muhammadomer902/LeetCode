class Solution(object):
    @staticmethod
    def isPalindrome(s):
        return s == s[::-1]

    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        rev_s = s[::-1]
        combined = s + "#" + rev_s 
        prefix_len = self.computeKMP(combined)

        non_palindrome_suffix = s[prefix_len:]

        return non_palindrome_suffix[::-1] + s

    def computeKMP(self, s):
        """
        Compute the KMP table (partial match table) for string `s`.
        This helps in finding the longest prefix of the string that is a palindrome.
        """
        n = len(s)
        lps = [0] * n

        length = 0
        i = 1
        while i < n:
            if s[i] == s[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps[-1]
