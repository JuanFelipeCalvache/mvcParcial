from Models.Task_Model import Task

class QaTask(Task):
    def __init__(self, description, duration, state, engineer):
        super().__init__(description, duration, state, engineer)
        