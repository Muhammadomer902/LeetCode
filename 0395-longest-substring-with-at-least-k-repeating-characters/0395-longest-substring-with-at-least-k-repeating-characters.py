class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        size = len(s)
        flag = True
        while size>=k:
            count = 0
            while count+size<=len(s):
                subs = s[count:count+size]
                arr = [0] * 26 

                for i in range(0,len(subs)):
                    index = ord(subs[i]) - ord('a')
                    arr[index] += 1

                flag = True
                for freq in arr:
                    if freq == 0 or freq >= k:
                        flag = True
                    else:
                        flag = False
                        break

                count+=1
                
                if flag:
                    return size

            if flag:
                return size
            else:
                size-=1

        return 0