from collections import defaultdict, deque

class Solution(object):
    def findAllRecipes(self, recipes, ingredients, supplies):
        """
        :type recipes: List[str]
        :type ingredients: List[List[str]]
        :type supplies: List[str]
        :rtype: List[str]
        """
        graph = defaultdict(list)
        in_degree = defaultdict(int)
        
        # Build the graph and in-degree map
        for i, recipe in enumerate(recipes):
            for ing in ingredients[i]:
                graph[ing].append(recipe)
                in_degree[recipe] += 1
        
        # Initialize queue with initial supplies
        queue = deque(supplies)
        result = []
        
        while queue:
            item = queue.popleft()
            
            # If it's a recipe and has zero in-degree, it's creatable
            if item in in_degree and in_degree[item] == 0:
                result.append(item)
            
            # Reduce in-degree of dependent recipes
            for neighbor in graph[item]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        return result
