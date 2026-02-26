class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        rnum = 0;flag = False
        if x<0:
            flag = True
            x = x*-1
        while x:
            digit = x%10
            x = x/10
            rnum = rnum*10 + digit
            if rnum>2147483647 or rnum<-2147483648:
                return 0
        if flag:
            return -1*rnum
        else:
            return rnum