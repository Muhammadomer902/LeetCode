class Solution(object):
    def diffWaysToCompute(self, expression):
        memo = {}

        def compute(expression):
            if expression in memo:
                return memo[expression]
        
            result = []
            for i, char in enumerate(expression):
                if char in \+-*\:
                    left = compute(expression[:i])
                    right = compute(expression[i+1:])
                
                    for l in left:
                        for r in right:
                            if char == '+':
                                result.append(l + r)
                            elif char == '-':
                                result.append(l - r)
                            elif char == '*':
                                result.append(l * r)
        
            if not result:
                result.append(int(expression))
        
            memo[expression] = result
            return result

        return compute(expression)