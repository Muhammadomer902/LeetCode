class Solution(object):
    def countDays(self, days, meetings):
        """
        :type days: int
        :type meetings: List[List[int]]
        :rtype: int
        """
        if not meetings:
            return days
        
        # Step 1: Sort meetings by start day
        meetings.sort()
        
        # Step 2: Merge overlapping meetings
        merged = []
        for start, end in meetings:
            if not merged or merged[-1][1] < start - 1:
                merged.append([start, end])
            else:
                merged[-1][1] = max(merged[-1][1], end)
        
        # Step 3: Count available days
        available_days = merged[0][0] - 1  # Days before the first meeting
        for i in range(1, len(merged)):
            available_days += merged[i][0] - merged[i - 1][1] - 1
        
        # Days after the last meeting
        available_days += days - merged[-1][1]
        
        return available_days
