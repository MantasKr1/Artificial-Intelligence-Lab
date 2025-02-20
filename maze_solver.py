# maze_solver.py
# Data: 2025-02-20
# Autorius: Mantas Kryževičius

from search import Problem, astar_search
import matplotlib.pyplot as plt

# Labirinto įkėlimo funkcija
def load_maze(filename):
    """Įkrauna labirintą iš tekstinio failo ir grąžina kaip 2D masyvą"""
    maze = []
    with open(filename, 'r') as file:
        for line in file:
            maze.append(list(line.strip()))
    return maze

# Labirinto problemos klasė, paveldima iš AIMA „Problem“ klasės
class MazeProblem(Problem):
    """Labirinto sprendimo uždavinys, naudojant AIMA architektūrą"""

    def __init__(self, maze, start, goal):
        """Inicijuoja pradinę ir galinę būsenas"""
        super().__init__(start, goal)
        self.maze = maze

    def actions(self, state):
        """Grąžina galimus veiksmus (žingsnius) iš dabartinės būsenos"""
        actions = []
        x, y = state
        for (dx, dy) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(self.maze) and 0 <= ny < len(self.maze[0]) and self.maze[nx][ny] != '#':
                actions.append((dx, dy))
        return actions

    def result(self, state, action):
        """Grąžina naują būseną pritaikius veiksmą"""
        x, y = state
        dx, dy = action
        return (x + dx, y + dy)

    def goal_test(self, state):
        """Patikrina, ar būsena yra galinė (tikslas pasiektas)"""
        return state == self.goal

    def h(self, node):
        """Euristika: Manhattan atstumas iki tikslo"""
        x1, y1 = node.state
        x2, y2 = self.goal
        return abs(x1 - x2) + abs(y1 - y2)

# Labirinto vizualizacija
def visualize_maze(maze, path=[]):
    """Atvaizduoja labirintą ir parodo optimalų kelią"""
    plt.figure(figsize=(6, 6))
    for i, row in enumerate(maze):
        for j, col in enumerate(row):
            if (i, j) == start:
                plt.text(j, i, 'S', va='center', ha='center', fontsize=12, color='green')
            elif (i, j) == goal:
                plt.text(j, i, 'G', va='center', ha='center', fontsize=12, color='red')
            elif (i, j) in path:
                plt.text(j, i, '.', va='center', ha='center', fontsize=12, color='blue')
            elif col == '#':
                plt.plot(j, i, 'ks')
    plt.gca().invert_yaxis()
    plt.axis('equal')
    plt.show()

# Įkeliamas labirintas ir inicijuojama problema
maze = load_maze('maze.txt')
start = (1, 1)  # Pradžia (S)
goal = (5, 7)   # Tikslas (G)

problem = MazeProblem(maze, start, goal)
solution = astar_search(problem)

# Parodo optimalų kelią
if solution:
    path = [node.state for node in solution.path()]
    visualize_maze(maze, path)
else:
    print("Kelias nerastas!")
