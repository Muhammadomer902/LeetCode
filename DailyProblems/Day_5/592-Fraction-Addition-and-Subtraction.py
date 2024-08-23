from fractions import Fraction

class Solution(object):
    def fractionAddition(self, expression):
        explist=expression.replace('-','+-').split('+')
        num = 0
        for i in explist:
            if i:
                templist = i.split('/')
                num = num + Fraction(int(templist[0]),int(templist[1]))
        if num%1==0:
            return str(num)+\/1\
        return str(num)
        
        