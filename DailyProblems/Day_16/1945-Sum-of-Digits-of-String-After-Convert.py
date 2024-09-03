class Solution(object):
    def getLucky(self, s, k):
        st =""
        for i in range(len(s)):
            st+= str(ord(s[i])-96)
        sum = 0;j = 0
        while j<k:
            sum = 0
            for i in range(len(st)):
                sum +=int(st[i])
            j+=1
            st = str(sum)
        return int(st)
            

        