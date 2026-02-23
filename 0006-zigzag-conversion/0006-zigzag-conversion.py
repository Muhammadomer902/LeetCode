class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        zigzag = [[] for _ in range(numRows)]
        flag = True; curIndex = 0; result =""
        for i in range(len(s)):
            if flag:
                zigzag[curIndex].append(s[i])
                curIndex+=1
            else:
                zigzag[curIndex].append(s[i])
                curIndex-=1
            if flag and curIndex%numRows==0:
                flag = False
                curIndex-=2
            elif not flag and curIndex<0:
                flag = True
                curIndex+=2

        for row in zigzag:
            result += "".join(row)

        return result