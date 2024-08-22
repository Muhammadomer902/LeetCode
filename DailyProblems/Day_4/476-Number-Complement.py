class Solution(object):
    def findComplement(self, num):
        binary = "{0:b}".format(num)
        bin_list = list(binary)
        for i in range(len(binary)):
            if bin_list[i]=='0':
                bin_list[i]='1'
            else:
                bin_list[i]='0'
        bin_list = ''.join(bin_list)
        return int(bin_list,2)
        