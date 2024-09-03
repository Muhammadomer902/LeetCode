class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        st = ['a','e','i','o','u']
        vowels = 0;max =0
        for i in range(k):
            if s[i] in st:
                max+=1
        vowels = max
        for i in range(k,len(s)):
            if s[i] in st:
                vowels+=1
            if s[i-k] in st:
                vowels-=1
            if vowels>max:
                max = vowels
        return max            