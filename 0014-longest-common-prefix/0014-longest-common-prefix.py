class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        word = "";index = -1;length = 1000
        for i,s in enumerate(strs):
            if len(s)<length:
                word = s
                index = i
                length = len(s)
        print(word, index)

        for i in range(0,len(strs)):
            if word and i != index:
                for j in range(0,length):
                    if strs[i][j]!=word[j]:
                        word = word[:j]
                        length = len(word)
                        break

        return word
            