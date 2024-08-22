class Solution(object):
    def compress(self, chars):
        size = 0 
        i = 0  
        while size < len(chars):
            char = chars[size]
            count = 0
            while size < len(chars) and chars[size] == char:
                size += 1
                count += 1
            chars[i] = char
            i += 1
            if count > 1:
                for c in str(count):
                    chars[i] = c
                    i += 1
        return i 

        