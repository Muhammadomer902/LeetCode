class Solution(object):
    def isCircularSentence(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        # Split the sentence into words
        words = sentence.split()
        
        # Check if each word ends with the same character that the next word starts with
        for i in range(len(words)):
            # Current word's last character
            last_char = words[i][-1]
            # Next word's first character (wrap around to the first word for the last word)
            next_first_char = words[(i + 1) % len(words)][0]
            
            # If they do not match, the sentence is not circular
            if last_char != next_first_char:
                return False
        
        return True
