class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        size=len(s)

        for i in range(size//2,0,-1):
            if size%i==0 and i!=0:
                j=i+i
                flag = True
                arr1 = s[:i]
                arr2 = s[i:i+i]
                while j<=size:
                    print(arr1)
                    print(arr2)
                    if arr1!=arr2:
                        flag = False
                        break
                    arr1 = arr2
                    arr2 = s[j:j+i]
                    j+=i
                if flag:
                    return True
        
        return False