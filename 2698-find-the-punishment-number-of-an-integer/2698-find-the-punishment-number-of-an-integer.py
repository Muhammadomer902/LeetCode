class Solution(object):
    def punishmentNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        def can_partition(s, target, index=0, current_sum=0):
            if index == len(s):
                return current_sum == target
            
            num = 0
            for i in range(index, len(s)):
                num = num * 10 + int(s[i])  # Form number from substring
                if current_sum + num > target:
                    break  # Stop early if sum exceeds target
                if can_partition(s, target, i + 1, current_sum + num):
                    return True
            return False
        
        punishment_sum = 0
        for i in range(1, n + 1):
            square_str = str(i * i)
            if can_partition(square_str, i):
                punishment_sum += i * i
        
        return punishment_sum

        