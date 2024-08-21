class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        if len(flowerbed)==1 and flowerbed[0]==0 and n<=1:
            return True
        elif len(flowerbed)==1 and flowerbed[0]==1 and n>1:
            return False
        for i in range(len(flowerbed)):
            if i==0 and flowerbed[i]==0 and flowerbed[i+1]==0:
                n-=1
                flowerbed[i]=1
            elif i>0 and i<len(flowerbed)-1 and flowerbed[i-1]==0 and flowerbed[i]==0 and flowerbed[i+1]==0:
                n-=1
                flowerbed[i]=1
            elif i==len(flowerbed)-1 and flowerbed[i-1]==0 and flowerbed[i]==0:
                n-=1
                flowerbed[i]=1

        if n<=0:
            return True
        return False
        