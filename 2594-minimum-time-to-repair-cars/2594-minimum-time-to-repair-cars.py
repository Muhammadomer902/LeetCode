import math

class Solution(object):
    def repairCars(self, ranks, cars):
        left, right = 1, min(ranks) * cars * cars
        
        def canRepairInTime(mid):
            total_cars = 0
            for rank in ranks:
                total_cars += int(math.sqrt(mid // rank))
                if total_cars >= cars:
                    return True
            return total_cars >= cars
        
        while left < right:
            mid = (left + right) // 2
            if canRepairInTime(mid):
                right = mid
            else:
                left = mid + 1
        
        return left
