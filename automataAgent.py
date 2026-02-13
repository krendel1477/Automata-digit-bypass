class Agent:
    def __init__(self, start_pos):

        self.current_position = start_pos  # Текущая позиция агента
        self.path_history = []                    # История перемещений
        self.exit_found = False                   # Флаг достижения выхода
        self.commands = {}
        self.current_state = "q0"  # Начальное состояние
        

    def get_current_state(self):
        return self.current_state
    
    def set_state(self, new_state):
        self.current_state = new_state

    def cur_pos_getter(self):
        return self.current_position
        
    def history_getter(self):
        return self.path_history
        
    def commands_getter(self):
        return self.commands
        
    def is_end (self):
        return self.exit_found