class Solution(object):
    def missingRolls(self, rolls, mean, n):
        total_sum = (len(rolls) + n) * mean
        current_sum = sum(rolls)
        missing_sum = total_sum - current_sum
        if missing_sum < n or missing_sum > 6 * n:
            return []  
        result = [1] * n
        remaining = missing_sum - n
        for i in range(n):
            add = min(5, remaining)
            result[i] += add
            remaining -= add
            if remaining == 0:
                break
        
        return result