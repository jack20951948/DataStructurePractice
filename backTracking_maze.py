
class backTrackingMaze:
    def __init__(self, maze):
        self._maze = maze
        self._directions = [
            lambda x, y: (x-1, y), # goes down
            lambda x, y: (x+1, y), # goes up
            lambda x, y: (x, y+1), # goes right
            lambda x, y: (x, y-1)  # goes left
        ]

    def print_maze(self):
        for i in self._maze:
            for j in i:
                print(j, end=" ")
            print("\n", end="")

    def solve_maze(self, x, y, goal_x, goal_y):
        # 0: unreached path, 1: wall, 2: reached path, 3: dead path
        self._maze[x][y] = 2
        stack = []
        stack.append((x, y))
        print("Game started!")
        while (stack):
            current_spot = stack[-1]
            if current_spot[0] == goal_x and current_spot[1] == goal_y:
                print("Arrived!")
                return True
            for dir in self._directions:
                next = dir(current_spot[0], current_spot[1])
                if self._maze[next[0]][next[1]] == 0:
                    stack.append((next[0], next[1]))
                    self._maze[next[0]][next[1]] = 2
                    break
            else:
                self._maze[current_spot[0]][current_spot[1]] = 3
                stack.pop()
        print("Can't find!")
        return False
        


if __name__ == "__main__":

    maze = [
        [1, 1, 1, 1, 1, 1],
        [1, 0, 1, 0, 1, 1],
        [1, 0, 1, 0, 0, 1],
        [1, 0, 0, 0, 1, 1],
        [1, 0, 1, 0, 0, 1], 
        [1, 1, 1, 1, 1, 1]
    ]

    BM = backTrackingMaze(maze)
    BM.print_maze()
    BM.solve_maze(1, 1, 4, 4)
    BM.print_maze()