class Solution:
    def minimumSteps(self, s):
        length = len(s)
        answer = 0
        one_count = 0

        # Traverse the string in reverse from last to first character
        for i in reversed(range(length)):
            # Check if the current character is '1'
            if s[i] == '1':
                # If it's '1', increment the 'one_count'
                one_count += 1
                answer += (length - i - 1) - one_count + 1

        # Return the total minimum steps calculated
        return answer
