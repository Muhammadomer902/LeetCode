# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def spiralMatrix(self, m, n, head):
        out = [[-1] * n for _ in range(m)];x=0;y=0;up = 0;down = m-1;left =0;right = n-1;d = 1
        while head!=None:
            out[x][y] = head.val
            if d==1 and y!=right:
                y+=1
            elif d==1 and y==right:
                d=2
                x+=1
                right-=1
                up+=1
            elif d==2 and x!=down:
                x+=1
            elif d==2 and x==down:
                d=3
                y-=1
                down-=1
            elif d==3 and y!=left:
                y-=1
            elif d==3 and y==left:
                left+=1
                x-=1
                d=4
            elif d==4 and x!=up:
                x-=1
            elif d==4 and x==up:
                d=1
                y+=1
            head = head.next    
                
        return out