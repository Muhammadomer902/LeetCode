class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        rpath=[]
        path = path.split('/')
        for i in path:
            if i == ".." and rpath:
                rpath.pop()
            elif i!='' and i!=".." and i!='.':
                rpath.append(i)

        return '/' + '/'.join(rpath)