from collections import Counter

class Solution(object):
    def numTilePossibilities(self, tiles):
        """
        :type tiles: str
        :rtype: int
        """
        count = Counter(tiles)
        
        def backtrack():
            total = 0
            for tile in count:
                if count[tile] > 0:
                    count[tile] -= 1
                    total += 1 + backtrack()  # Include this tile and recurse
                    count[tile] += 1  # Restore the tile count after recursion
            return total
        
        return backtrack()
