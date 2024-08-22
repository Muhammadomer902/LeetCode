class Solution(object):
    def reverseWords(self, s):
        s = [s for s in s.split(' ') if s]
        s.reverse()
        return ' '.join(s)
        