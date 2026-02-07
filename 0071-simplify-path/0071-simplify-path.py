class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        rpath=[]
        path = path.split('/')
        print(path)
        for i in path:
            if i == ".." and rpath:
                rpath.pop()
            elif i!='' and i!=".." and i!='.':
                rpath.append(i)
        print(rpath)
        rtpath =""

        for i in rpath:
            rtpath+= '/'+i

        return rtpath if rtpath else '/'