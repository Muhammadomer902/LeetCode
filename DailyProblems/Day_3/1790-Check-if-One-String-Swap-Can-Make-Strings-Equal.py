class Solution(object):
    def areAlmostEqual(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if s1 == s2:
            return True
        
        # Find the indices where the two strings differ
        diff = [(a, b) for a, b in zip(s1, s2) if a != b]
        
        # There must be exactly two differences, and swapping them should make the strings equal
        return len(diff) == 2 and diff[0] == diff[1][::-1]
