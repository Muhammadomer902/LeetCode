class Solution(object):
    def smallestNumber(self, pattern):
        """
        :type pattern: str
        :rtype: str
        """
        stack = [] 
        result = "" 
        num = 1 
        
        for ch in pattern + 'I':  
            stack.append(str(num))  
            num += 1  
            
            if ch == 'I': 
                while stack:
                    result += stack.pop()
        
        return result