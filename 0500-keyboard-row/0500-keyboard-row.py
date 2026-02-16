class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        row1 = ['q','w','e','r','t','y','u','i','o','p']
        row2 = ['a','s','d','f','g','h','j','k','l']
        row3 = ['z','x','c','v','b','n','m']
        rarr = []
        for i in words:
            r1c=0;r2c=0;r3c=0
            for j in i:
                j = lower(j)
                if j in row1:
                    r1c+=1
                elif j in row2:
                    r2c+=1
                else:
                    r3c+=1
            if r2c==0 and r3c==0:
                rarr.append(i)
            elif r1c==0 and r3c==0:
                rarr.append(i)
            elif r2c==0 and r1c==0:
                rarr.append(i)
        return rarr