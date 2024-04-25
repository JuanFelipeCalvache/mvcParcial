from Models.Task_Model import Task


class DevTaskAdapter(Task):
    def __init__(self, dev_task):
        super().__init__(dev_task.getDescription(), dev_task.getDuration(), dev_task.getState(), dev_task.getEngineerName())
        self.state = "En Dev"  # Cambiar el estado al adaptarla
