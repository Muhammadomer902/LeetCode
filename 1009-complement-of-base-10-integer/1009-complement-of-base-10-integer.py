class Solution(object):
    def bitwiseComplement(self, n):
        binary = "{0:b}".format(n)
        bin_list = list(binary)
        for i in range(len(binary)):
            if bin_list[i]=='0':
                bin_list[i]='1'
            else:
                bin_list[i]='0'
        bin_list = ''.join(bin_list)
        return int(bin_list,2)
        