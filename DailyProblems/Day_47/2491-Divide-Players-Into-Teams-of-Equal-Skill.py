class Solution(object):
    def dividePlayers(self, skill):
        """
        :type skill: List[int]
        :rtype: int
        """
        skill.sort()
        n = len(skill)
        total_chemistry = 0
        total_skill = skill[0] + skill[-1]
        
        for i in range(n // 2):
            if skill[i] + skill[n - 1 - i] != total_skill:
                return -1
            total_chemistry += skill[i] * skill[n - 1 - i]
        
        return total_chemistry
