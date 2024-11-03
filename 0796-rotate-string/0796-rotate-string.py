class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        # Check if the lengths are equal
        if len(s) != len(goal):
            return False
        # Check if goal is a substring of s + s
        return goal in (s + s)

        