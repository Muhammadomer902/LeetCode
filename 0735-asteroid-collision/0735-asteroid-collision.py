class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        out = [asteroids[0]];i=0;
        while i <len(asteroids)-1:
            flag =True
            if not out:
                out.append(asteroids[i+1])
                flag = False
            if asteroids[i+1]<0 and out[len(out)-1]>0:
                while out and out[len(out)-1]>0:
                    if out[len(out)-1]<(-1*asteroids[i+1]):
                        out.pop()
                    elif out[len(out)-1]==(-1*asteroids[i+1]):
                        out.pop()
                        flag = False
                        break
                    else:
                        flag = False
                        break
            if flag:
                out.append(asteroids[i+1])
            i+=1
        return out
            