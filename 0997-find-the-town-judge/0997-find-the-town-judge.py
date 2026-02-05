class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        arr = [1]*n;arr1 = [0]*n
        size = len(trust);count = n
        for i in range(0,size):
            if arr[trust[i][0]-1]==1:
                count-=1
            arr[trust[i][0]-1]=0
            arr1[trust[i][1]-1]+=1
        if count==0:
            return -1
        else:
            for i in range(0,n):
                if arr[i] and arr1[i]==n-1:
                    return i+1
        return -1