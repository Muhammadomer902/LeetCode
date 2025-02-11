class Solution(object):
    def removeOccurrences(self, s, part):
        """
        :type s: str
        :type part: str
        :rtype: str
        """
        while part in s:  # Keep removing until 'part' no longer exists in 's'
            s = s.replace(part, "", 1)  # Remove only the first occurrence per iteration
        return s
