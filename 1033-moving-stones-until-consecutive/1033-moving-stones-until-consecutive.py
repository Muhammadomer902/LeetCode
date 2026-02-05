class Solution(object):
    def numMovesStones(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        while a>b or b>c:
            if a>b and a>c:
                a,c=c,a
            elif a>b and a<c:
                a,b=b,a
            elif a<b and a>c:
                a,c=c,a
                b,c=c,b
            elif b>c:
                b,c=c,b

        if a+1==b and b+1==c:
            return [0,0]
        elif a+1==b:
            return [1,c-b-1]
        elif a+2==b:
            return [1,b-a-1+c-b-1]
        elif b+1==c:
            return [1, b-a-1]
        elif b+2==c:
            return [1,b-a-1+c-b-1]
        else:
            return[2, b-a-1+c-b-1]