class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = 0
        for i in digits:
            num = num*10 + i
        
        num+=1; digitR = []

        while num>0:
            d = num%10
            num = num/10
            digitR.insert(0,d)

        return digitR
