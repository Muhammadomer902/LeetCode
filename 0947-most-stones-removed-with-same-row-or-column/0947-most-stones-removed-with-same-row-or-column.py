class Solution(object):
    def removeStones(self, stones):

        parent = {}
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                parent[rootX] = rootY 
        for x, y in stones:
            if x not in parent:
                parent[x] = x
            if ~y not in parent:  
                parent[~y] = ~y
            union(x, ~y)
        
        unique_groups = len(set(find(x) for x in parent))
        return len(stones) - unique_groups
