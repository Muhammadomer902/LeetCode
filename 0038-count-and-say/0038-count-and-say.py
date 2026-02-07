class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        rstring = "1";count = 0;cnum=rstring[0];news=""
        if n==1:
            return rstring
        for i in range(1,n):
            for j in range(0,len(rstring)):
                if cnum == rstring[j]:
                    count+=1
                else:
                    news+= str(count) + cnum
                    cnum = rstring[j]
                    count = 1
            news+= str(count) + cnum
            count = 0
            rstring = news
            cnum=rstring[0]
            news = ""
        return rstring