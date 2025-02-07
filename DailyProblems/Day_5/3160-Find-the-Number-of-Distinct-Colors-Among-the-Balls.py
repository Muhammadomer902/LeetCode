class Solution(object):
    def queryResults(self, limit, queries):
        """
        :type limit: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        ball_colors = {}  # Dictionary to track the latest color of each ball
        color_count = {}  # Dictionary to track occurrences of each color
        distinct_colors = set()  # Set to store distinct colors
        result = []
        
        for ball, color in queries:
            # If the ball was already colored, remove the old color if needed
            if ball in ball_colors:
                old_color = ball_colors[ball]
                color_count[old_color] -= 1
                if color_count[old_color] == 0:
                    distinct_colors.remove(old_color)
            
            # Assign the new color
            ball_colors[ball] = color
            if color not in color_count:
                color_count[color] = 0
            color_count[color] += 1
            distinct_colors.add(color)
            
            # Append the current count of distinct colors
            result.append(len(distinct_colors))
        
        return result
