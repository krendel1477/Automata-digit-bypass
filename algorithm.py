from maze import Maze
from backup_stateTable import StatesTable

class Algorithm:
    def __init__(self, maze, agent, states_table):
        self.maze = maze
        self.agent = agent
        self.states_table = states_table
        

    def _init_finder_agent_commands(self, agent_commands):
        self.agent.commands = agent_commands

    def _init_bypasser_agent_commands(self, agent_commands):
        self.agent.commands = agent_commands

    def _init_end_agent_commands(self, agent_commands):
        self.agent.commands = agent_commands
                
    def first_runner(self, max_iterations = 1000):
        """Запуск алгоритма обхода лабиринта."""
        self._init_finder_agent_commands(self.states_table.first_start_program)  # Инициализация состояний агента
        steps = 0
        dot = set()
        flag = 0
        while (
            not self.agent.exit_found 
        ):
            prev_state = self.agent.get_current_state()
            new_state = self.maze.step(self.agent)
            
            if (new_state == "q10" and flag == 0):
                flag = 1
                self._init_bypasser_agent_commands(self.states_table.first_bypasser_program)  # ставим камень и начинаем обход цифры
                dot.add(self.agent.current_position)
                continue
            if ((self.agent.current_position in dot) and (flag == 1)):
                self._init_end_agent_commands(self.states_table.end_program)
            
            # Логирование изменений (опционально)
            # print(f"Step {steps}: State {prev_state} -> {new_state}, Pos {self.agent.current_position}")
            if(max_iterations == steps):
                break
            steps += 1

        return self.agent.exit_found
    
    def second_runner(self, max_iterations = 1000):
        """Запуск алгоритма обхода лабиринта."""
        self._init_finder_agent_commands(self.states_table.third_start_program)  # Инициализация состояний агента
        steps = 0
        dot = set()
        flag = 0
        while (
            not self.agent.exit_found 
        ):
            prev_state = self.agent.get_current_state()
            new_state = self.maze.step(self.agent)
            
            if (new_state == "q10" and flag == 0):
                flag = 1
                self._init_bypasser_agent_commands(self.states_table.second_bypasser_program)  # ставим камень и начинаем обход цифры
                dot.add(self.agent.current_position)
                continue
            if ((self.agent.current_position in dot) and (flag == 1)):
                self._init_end_agent_commands(self.states_table.end_program)
            
            # Логирование изменений (опционально)
            # print(f"Step {steps}: State {prev_state} -> {new_state}, Pos {self.agent.current_position}")
            if(max_iterations == steps):
                break
            steps += 1

        return self.agent.exit_found

    def third_runner(self, max_iterations = 1000):
        """Запуск алгоритма обхода лабиринта."""
        self._init_finder_agent_commands(self.states_table.third_start_program)  # Инициализация состояний агента
        steps = 0
        dot = set()
        flag = 0
        while (
            not self.agent.exit_found 
        ):
            prev_state = self.agent.get_current_state()
            new_state = self.maze.step(self.agent)
            
            if (new_state == "q10" and flag == 0):
                flag = 1
                self._init_bypasser_agent_commands(self.states_table.third_bypasser_program)  # ставим камень и начинаем обход цифры
                dot.add(self.agent.current_position)
                continue
            if ((self.agent.current_position in dot) and (flag == 1)):
                self._init_end_agent_commands(self.states_table.end_program)
            
            # Логирование изменений (опционально)
            # print(f"Step {steps}: State {prev_state} -> {new_state}, Pos {self.agent.current_position}")
            if(max_iterations == steps):
                break
            steps += 1

        return self.agent.exit_found
    
    def inverted_third_runner(self, max_iterations = 1000):
        """Запуск алгоритма обхода лабиринта."""
        self._init_finder_agent_commands(self.states_table.third_start_program)  # Инициализация состояний агента
        steps = 0
        dot = set()
        flag = 0
        while (
            not self.agent.exit_found 
        ):
            prev_state = self.agent.get_current_state()
            new_state = self.maze.step(self.agent)
            
            if (new_state == "q10" and flag == 0):
                flag = 1
                self._init_bypasser_agent_commands(self.states_table.inverted_third_bypasser_program)  # ставим камень и начинаем обход цифры
                dot.add(self.agent.current_position)
                continue
            if ((self.agent.current_position in dot) and (flag == 1)):
                self._init_end_agent_commands(self.states_table.end_program)
            
            # Логирование изменений (опционально)
            # print(f"Step {steps}: State {prev_state} -> {new_state}, Pos {self.agent.current_position}")
            if(max_iterations == steps):
                break
            steps += 1

        return self.agent.exit_found

    def fourth_runner(self, max_iterations = 1000):
        """Запуск алгоритма обхода лабиринта."""
        self._init_finder_agent_commands(self.states_table.third_start_program)  # Инициализация состояний агента
        steps = 0
        dot = set()
        flag = 0
        while (
            not self.agent.exit_found 
        ):
            prev_state = self.agent.get_current_state()
            new_state = self.maze.step(self.agent)
            
            if (new_state == "q10" and flag == 0):
                flag = 1
                self._init_bypasser_agent_commands(self.states_table.fourth_bypasser_program)  # ставим камень и начинаем обход цифры
                dot.add(self.agent.current_position)
                continue
            if ((self.agent.current_position in dot) and (flag == 1)):
                self._init_end_agent_commands(self.states_table.end_program)
            
            # Логирование изменений (опционально)
            # print(f"Step {steps}: State {prev_state} -> {new_state}, Pos {self.agent.current_position}")
            if(max_iterations == steps):
                break
            steps += 1

        return self.agent.exit_found

    def fifth_runner(self, max_iterations = 1000):
        """Запуск алгоритма обхода лабиринта."""
        self._init_finder_agent_commands(self.states_table.third_start_program)  # Инициализация состояний агента
        steps = 0
        dot = set()
        flag = 0
        while (
            not self.agent.exit_found 
        ):
            prev_state = self.agent.get_current_state()
            new_state = self.maze.step(self.agent)
            
            if (new_state == "q10" and flag == 0):
                flag = 1
                self._init_bypasser_agent_commands(self.states_table.fifth_bypasser_program)  # ставим камень и начинаем обход цифры
                dot.add(self.agent.current_position)
                continue
            if ((self.agent.current_position in dot) and (flag == 1)):
                self._init_end_agent_commands(self.states_table.end_program)
            
            # Логирование изменений (опционально)
            # print(f"Step {steps}: State {prev_state} -> {new_state}, Pos {self.agent.current_position}")
            if(max_iterations == steps):
                break
            steps += 1

        return self.agent.exit_found

    def sixth_runner(self, max_iterations = 1000):
        self._init_finder_agent_commands(self.states_table.first_start_program)  # Инициализация состояний агента
        steps = 0
        dot = set()
        flag = 0
        while (
            not self.agent.exit_found 
        ):
            prev_state = self.agent.get_current_state()
            new_state = self.maze.step(self.agent)
            
            if (new_state == "q10" and flag == 0):
                flag = 1
                self._init_bypasser_agent_commands(self.states_table.sixth_bypasser_program)  # ставим камень и начинаем обход цифры
                dot.add(self.agent.current_position)
                continue
            if ((self.agent.current_position in dot) and (flag == 1)):
                self._init_end_agent_commands(self.states_table.end_program)
            
            # Логирование изменений (опционально)
            # print(f"Step {steps}: State {prev_state} -> {new_state}, Pos {self.agent.current_position}")
            if(max_iterations == steps):
                break
            steps += 1

        return self.agent.exit_found

    def program_runner(self, desired_labels):
        #125433
        # print("Определяем число:")
        good = 1



        # Проверяем цифру 1 в первую очередь
        if 1 in desired_labels: #25
            # Сбрасываем агента в начальное состояние
            self.maze.change_agent_pos_to_start()
            self.maze.change_agent_state_to_zero()
            try:
                if self.first_runner():
                    # self.maze.visualize(1, agent=self.agent)
                    return {"exit_found": True, "info": 1}
            except Exception as e:
                good = 0
                # print("Данная цифра не является 1")
                # print(f"Ошибка при проверке 1: {str(e)}")
        
        if 2 in desired_labels: #75
            self.maze.change_agent_pos_to_start()
            self.maze.change_agent_state_to_zero()
            try:
                if self.second_runner():
                    # self.maze.visualize(3, agent=self.agent)
                    return {"exit_found": True, "info": 2}
            except Exception as e:
                good = 0
                # print("Данная цифра не является 2")
                # print(f"Ошибка при проверке инвертированной 2: {str(e)}")

        if 5 in desired_labels: # 89
            self.maze.change_agent_pos_to_start()
            self.maze.change_agent_state_to_zero()
            try:
                if self.fifth_runner():
                    # self.maze.visualize(1, agent=self.agent)
                    return {"exit_found": True, "info": 5}
            except Exception as e:
                good = 0
                # print("Данная цифра не является 5")
                # print(f"Ошибка при проверке обычной 5: {str(e)}")



        if 4 in desired_labels: # 69
            self.maze.change_agent_pos_to_start()
            self.maze.change_agent_state_to_zero()
            try:
                if self.fourth_runner():
                    # self.maze.visualize(1, agent=self.agent)
                    return {"exit_found": True, "info": 4}
            except Exception as e:
                good = 0
                # print("Данная цифра не является 4")
                # print(f"Ошибка при проверке обычной 4: {str(e)}")

        if 3 in desired_labels: #71
            self.maze.change_agent_pos_to_start()
            self.maze.change_agent_state_to_zero()
            try:
                if self.inverted_third_runner():
                    # self.maze.visualize(3, agent=self.agent)
                    return {"exit_found": True, "info": 3}
            except Exception as e:
                good = 0
                # print("Данная цифра не является инвертированной 3")
                # print(f"Ошибка при проверке инвертированной 3: {str(e)}")

        if 3 in desired_labels: # 86
            self.maze.change_agent_pos_to_start()
            self.maze.change_agent_state_to_zero()
            try:
                if self.third_runner():
                    # self.maze.visualize(3, agent=self.agent)
                    return {"exit_found": True, "info": 3}
            except Exception as e:
                good = 0
                # print("Данная цифра не является обычной 3")
                # print(f"Ошибка при проверке обычной 3: {str(e)}")



                



        return {"exit_found": False, "info": None}
    # def program_runner(self, desired_labels):

    #     print("Определяем число:")

    #     # Проверяем цифру 1 в первую очередь
    #     if 1 in desired_labels: #25
    #         # Сбрасываем агента в начальное состояние
    #         self.maze.change_agent_pos_to_start()
    #         self.maze.change_agent_state_to_zero()
    #         try:
    #             if self.first_runner():
    #                 # self.maze.visualize(1, agent=self.agent)
    #                 return {"exit_found": True, "info": 1}
    #         except Exception as e:
    #             print("Данная цифра не является 1")
    #             # print(f"Ошибка при проверке 1: {str(e)}")

    #     if 4 in desired_labels: # 69
    #         self.maze.change_agent_pos_to_start()
    #         self.maze.change_agent_state_to_zero()
    #         try:
    #             if self.fourth_runner():
    #                 # self.maze.visualize(1, agent=self.agent)
    #                 return {"exit_found": True, "info": 4}
    #         except Exception as e:
    #             print("Данная цифра не является 4")
    #             # print(f"Ошибка при проверке обычной 4: {str(e)}")
        
    #     if 3 in desired_labels: #71
    #         self.maze.change_agent_pos_to_start()
    #         self.maze.change_agent_state_to_zero()
    #         try:
    #             if self.inverted_third_runner():
    #                 # self.maze.visualize(3, agent=self.agent)
    #                 return {"exit_found": True, "info": 3}
    #         except Exception as e:
    #             print("Данная цифра не является инвертированной 3")
    #             # print(f"Ошибка при проверке инвертированной 3: {str(e)}")
        
    #     if 2 in desired_labels: #75
    #         self.maze.change_agent_pos_to_start()
    #         self.maze.change_agent_state_to_zero()
    #         try:
    #             if self.second_runner():
    #                 # self.maze.visualize(3, agent=self.agent)
    #                 return {"exit_found": True, "info": 2}
    #         except Exception as e:
    #             print("Данная цифра не является 2")
    #             # print(f"Ошибка при проверке инвертированной 2: {str(e)}")

    #     if 3 in desired_labels: # 86
    #         self.maze.change_agent_pos_to_start()
    #         self.maze.change_agent_state_to_zero()
    #         try:
    #             if self.third_runner():
    #                 # self.maze.visualize(3, agent=self.agent)
    #                 return {"exit_found": True, "info": 3}
    #         except Exception as e:
    #             print("Данная цифра не является обычной 3")
    #             # print(f"Ошибка при проверке обычной 3: {str(e)}")

    #     if 5 in desired_labels: # 89
    #         self.maze.change_agent_pos_to_start()
    #         self.maze.change_agent_state_to_zero()
    #         try:
    #             if self.fifth_runner():
    #                 # self.maze.visualize(1, agent=self.agent)
    #                 return {"exit_found": True, "info": 5}
    #         except Exception as e:
    #             print("Данная цифра не является 5")
    #             # print(f"Ошибка при проверке обычной 5: {str(e)}")

    #     return {"exit_found": False, "info": None}

        
            
        
# start=(0,0), end=(27,27)
    @staticmethod
    def process_mnist_digit(img, label, desired_labels, count_of_iterations, start=(0,0), end=(27,27)):
        """Обработать одно изображение MNIST."""
        maze = Maze(img.tolist(), start, end)
        agent = maze.add_automata()
        states_table = StatesTable()
        algorithm = Algorithm(maze, agent, states_table)
        try:
          result = algorithm.sixth_runner(count_of_iterations)
            # if (result == False):
            #     result = algorithm.inverted_third_runner(count_of_iterations)
        except Exception as e:
            result = False
        result = algorithm.sixth_runner(count_of_iterations)
        # result = algorithm.program_runner(desired_labels)
        # num = result["info"] 
        # Визуализация с путем агента
        maze.visualize(label, agent=agent)
        
        return result