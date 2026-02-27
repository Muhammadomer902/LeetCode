class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        stringToCheck = "";sign = 1; start = False;Leading = True
        setNum = ("0","1","2","3","4","5","6","7","8","9")
        for i in s:
            if i == "-" and not start:
                sign = -1
                start = True
            elif i == "-" and start:
                break
            elif i == "+" and not start:
                sign = 1
                start = True
            elif i == "+" and start:
                break
            elif start and i not in setNum and (i != " " or i == " "):
                break
            elif i in setNum:
                start = True
                if i!="0" or not Leading:
                    stringToCheck+=i
                    Leading = False
            elif i not in setNum and i != " ":
                break
        if stringToCheck == "":
            return 0
        else:
            num = int(stringToCheck)*sign
            if num>(2**31)-1:
                return (2**31)-1
            elif num<-(2**31):
                return -(2**31)
            return num