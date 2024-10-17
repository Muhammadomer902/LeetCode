class Solution(object):
    def maximumSwap(self, num):
        \\\
        :type num: int
        :rtype: int
        \\\
        num_list = list(str(num))
        last = {int(x): i for i, x in enumerate(num_list)}
        for i, x in enumerate(num_list):
            for d in range(9, int(x), -1):
                if last.get(d, -1) > i:
                    num_list[i], num_list[last[d]] = num_list[last[d]], num_list[i]
                    return int(\\.join(num_list))
        return num

        