class Solution(object):
    def construct2DArray(self, original, m, n):
        """
        :type original: List[int]
        :type m: int
        :type n: int
        :rtype: List[List[int]]
        """
        if len(original)!=m*n:
            return[]
        D2 = [];c=0
        for i in range(m):
            row =[]
            for j in range(n):
                row.append(original[c])
                c+=1
            D2.append(row)
        return D2

        