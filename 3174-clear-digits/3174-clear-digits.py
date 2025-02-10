class Solution(object):
    def clearDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        
        for char in s:
            if char.isdigit():
                # Remove the closest non-digit character to its left
                if stack:
                    stack.pop()
            else:
                stack.append(char)
        
        return "".join(stack)
        