from Models.Task_Model import Task

class QaTaskAdapter(Task):
    def __init__(self, qa_task):
        super().__init__(qa_task.getDescription(), qa_task.getDuration(), qa_task.getState(), qa_task.getEngineerName())
        self.state = "En QA"