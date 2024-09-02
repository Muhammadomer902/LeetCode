class Solution(object):
    def chalkReplacer(self, chalk, k):
        s = sum(chalk)
        k = k%s
        c = 0
        while k >= chalk[c]:
            k-=chalk[c]
            c+=1
            if c == len(chalk):
                c = 0
        return c