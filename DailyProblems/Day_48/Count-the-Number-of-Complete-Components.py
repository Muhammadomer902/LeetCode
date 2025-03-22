class Solution(object):
    def countCompleteComponents(self, n, edges):
        from collections import defaultdict
        
        # Step 1: Build the graph
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = set()
        
        def dfs(node):
            stack = [node]
            component = set()
            while stack:
                node = stack.pop()
                if node not in visited:
                    visited.add(node)
                    component.add(node)
                    for neighbor in graph[node]:
                        if neighbor not in visited:
                            stack.append(neighbor)
            return component
        
        complete_count = 0
        
        # Step 2: Find connected components
        for node in range(n):
            if node not in visited:
                component = dfs(node)
                
                # Step 3: Check completeness of component
                size = len(component)
                edge_count = sum(len(graph[node]) for node in component) // 2
                
                # A complete graph with `size` nodes should have `size * (size - 1) / 2` edges
                if edge_count == size * (size - 1) // 2:
                    complete_count += 1
        
        return complete_count
