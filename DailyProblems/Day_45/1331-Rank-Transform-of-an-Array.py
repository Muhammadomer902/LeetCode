class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        sorted_unique = sorted(set(arr))
        rank_map = {value: rank + 1 for rank, value in enumerate(sorted_unique)}
        return [rank_map[element] for element in arr]