class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        count = 0
        for i in words:
            flag = True
            for j in i:
                if j not in allowed:
                    flag = False
                    break
            if flag:
                count+=1
        return count
        