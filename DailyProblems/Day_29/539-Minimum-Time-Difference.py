class Solution(object):
    def findMinDifference(self, timePoints):
        \\\
        :type timePoints: List[str]
        :rtype: int
        \\\
        def convertToMinutes(time):
            hours, minutes = map(int, time.split(':'))
            return hours * 60 + minutes
        minutes_list = sorted([convertToMinutes(time) for time in timePoints])
        min_diff = 1440
        for i in range(1, len(minutes_list)):
            min_diff = min(min_diff, minutes_list[i] - minutes_list[i - 1])
        min_diff = min(min_diff, 1440 - (minutes_list[-1] - minutes_list[0]))
        return min_diff
