import functools
import operator

class Solution(object):
    def xorQueries(self, arr, queries):
        """
        :type arr: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        prefix_xor = [0] * (len(arr) + 1)   
        for i in range(len(arr)):
            prefix_xor[i + 1] = prefix_xor[i] ^ arr[i]
        out = []

        for L, R in queries:
            if L == 0:
                out.append(prefix_xor[R + 1])
            else:
                out.append(prefix_xor[R + 1] ^ prefix_xor[L])

        return out
