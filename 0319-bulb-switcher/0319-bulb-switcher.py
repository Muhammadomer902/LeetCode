class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int(n ** 0.5)
        # x = [1]*n
        # count=n
        # for i in range(1,n):
        #     for j in range(i,n,i+1):
        #         if x[j]==0:
        #             x[j] = 1
        #             count+=1
        #         else:
        #             x[j] = 0
        #             count-=1
        # return count