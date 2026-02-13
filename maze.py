import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from automataAgent import Agent

class Maze:
    def __init__(self, grid, start, end):
        self.grid = grid
        self.normalize(grid)
        self.start = tuple(start)
        self.end = tuple(end)
        self.height = len(self.grid)
        self.width = len(self.grid[0])
        self.agent = None

    def normalize (self, grid):
        height = len(grid)
        width = len(grid[0]) if height > 0 else 0
        
        for x in range(height):
            for y in range(width):
                # Если клетка на границе и является стеной (1)
                if (x == 0 or x == height-1 or y == 0 or y == width-1) and self.grid[x][y] == 1:
                    self.grid[x][y] = 0  # Удаляем стену

    def change_agent_pos_to_start (self):
        self.agent.current_position = tuple((0,0))

    def change_agent_state_to_zero (self):
        self.agent.commands = None
        self.agent.current_state = "q0"

    def add_automata (self):
        self.agent = Agent(self.start)
        return self.agent
    
    def is_red_wall(self, pos):
        x,y = pos
        if((0 <= y < self.height) and (0 <= x < self.width)):
            return False
        return True
    
    def is_black_wall (self, pos):
        x,y = pos
        if((0 <= y < self.height) and (0 <= x < self.width) and (self.grid[x][y] == 1)):
            return True
        return False

    def is_wall(self, pos):
        x, y = pos
        # здесь нужно вернуть 0 - если стены нет (нолики, по которым можно ходить)
        #                     1 - если стена черная  (изображена в лабиринте как 1)
        #                     2 - если стена красная (вышла за рамки 28х28)
        if(not(self.is_red_wall(pos)) and not(self.is_black_wall(pos))):
            return 0
        elif (self.is_black_wall(pos)):
            return 1
        else:
            return 2
        

    def is_exit(self, pos):
        return pos == self.end

    def get_start(self):
        return self.start

    def get_neighbors(self):
        x, y = self.agent.cur_pos_getter()
        
        neighbors = set()

        x += 1
        pos = (x,y)
        if ((self.is_wall(pos)) == 0):
            neighbors.add("e")
        x -= 1

        y += 1
        pos = (x,y)
        if ((self.is_wall(pos)) == 0):
            neighbors.add("n")
        y -= 1

        x -= 1
        pos = (x,y)
        if ((self.is_wall(pos)) == 0):
            neighbors.add("w")
        x += 1

        y -= 1
        pos = (x,y)
        if ((self.is_wall(pos)) == 0):
            neighbors.add("s")
        y += 1
        # print("Текущий ключ запроса:", (neighbors))
        return frozenset(neighbors)

    def step(self, agent):
        current_state = agent.get_current_state()
        command_list = agent.commands_getter()
        
        new_state = current_state
        value =  (command_list[(current_state, self.get_neighbors())])
        direction = value[0] # надеюсь я здесь обратился нормально
        next_state = value[1]# и я не долбаеб
        
        # Определяем смещение для движения и перемещаемся
        next_pos = agent.current_position
        x, y = agent.current_position
        neighbors = self.get_neighbors()
        if (("n" in neighbors) and (direction == "up")):
            next_pos = (x, y+1)
            new_state = next_state
        if(("s" in neighbors) and (direction == "down")):
            next_pos = (x, y-1)
            new_state = next_state
        if(("w" in neighbors) and (direction == "left")):
            next_pos = (x-1, y)
            new_state = next_state
        if(("e" in neighbors) and (direction == "right")):
            next_pos = (x+1, y)
            new_state = next_state

        agent.current_position = next_pos
        agent.path_history.append(next_pos)
            
        if self.is_exit(next_pos):
            agent.exit_found = True
        else:
            agent.exit_found = False
        
        agent.set_state(new_state)
        
        return new_state
    
    def visualize(self, label, path=None, agent=None):
        """Визуализация лабиринта с помощью matplotlib"""
        fig, ax = plt.subplots(figsize=(8, 8))
        
        # Создаем матрицу для визуализации (0-пусто, 1-стена)
        viz_grid = [[0 if cell in (0,2,3) else 1 for cell in row] for row in self.grid]
        
        # Отображаем основную сетку
        cmap = ListedColormap(['white', 'black'])
        ax.imshow(viz_grid, cmap=cmap, interpolation='nearest')
        
        # Разметка старта и выхода
        start_y, start_x = self.start
        exit_y, exit_x = self.end
        ax.plot(start_x, start_y, 'gs', markersize=20, label='Start')  # Зеленый квадрат
        ax.plot(exit_x, exit_y, 'rs', markersize=20, label='Exit')    # Красный квадрат
        
        # Рисуем путь если он задан
        if path:
            x_coords = [y for (x, y) in path]
            y_coords = [x for (x, y) in path]
            ax.plot(x_coords, y_coords, 'b-', linewidth=2, label='Path')  # Синяя линия

        if agent:
            # Текущая позиция
            x, y = agent.current_position
            ax.plot(y, x, 'bo', markersize=15, label='Agent')
            
            # Путь агента
            if len(agent.path_history) > 1:
                x_coords = [pos[1] for pos in agent.path_history]
                y_coords = [pos[0] for pos in agent.path_history]
                ax.plot(x_coords, y_coords, 'b-', linewidth=1.25, alpha=0.9)

        # Настройка осей и сетки
        ax.set_xticks(range(self.width))
        ax.set_yticks(range(self.height))
        ax.grid(which='both', color='grey', linestyle='-', linewidth=0.5)
        ax.set_title(f"label is {label}")
        ax.legend()
        plt.show()
