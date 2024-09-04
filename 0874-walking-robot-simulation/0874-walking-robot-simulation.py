class Solution(object):
    def robotSim(self, commands, obstacles):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        x, y = 0, 0 
        direction = 0  
        max_distance = 0

        obstacle_set = set(map(tuple, obstacles))

        for command in commands:
            if command == -1:
                direction = (direction + 1) % 4
            elif command == -2: 
                direction = (direction - 1) % 4
            else: 
                dx, dy = directions[direction]
                for _ in range(command):
                    if (x + dx, y + dy) not in obstacle_set:
                        x += dx
                        y += dy
                        max_distance = max(max_distance, x * x + y * y)
                    else:
                        break
        return max_distance
        