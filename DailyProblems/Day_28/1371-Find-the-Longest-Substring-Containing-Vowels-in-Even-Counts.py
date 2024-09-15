class Solution(object):
    def findTheLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        vowel_to_bit = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}
        bitmask = 0
        first_occurrence = {0: -1}
        max_length = 0
        for i, char in enumerate(s):
            if char in vowel_to_bit:
                bitmask ^= (1 << vowel_to_bit[char])
            if bitmask in first_occurrence:
                max_length = max(max_length, i - first_occurrence[bitmask])
            else:
                first_occurrence[bitmask] = i

        return max_length
        