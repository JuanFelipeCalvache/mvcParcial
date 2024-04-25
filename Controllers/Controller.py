from Models.Developer_Engineer_Factory import DeveloperEngineerFactory
from Models.Qa_Engineer_Factory import QaEngineerFactory
from Models.Task_Model import Task
from Models.DevTask import DevTask
from Models.QaTask import QaTask
from Models.DevTaskAdapter import DevTaskAdapter
from Models.QaTaskAdapter import QaTaskAdapter

class Controller:
    
    def __init__(self):
        self.Task = []
        self.engineers_qa = []
        self.engineers_dev = []
        self.qa_factory = QaEngineerFactory()
        self.dev_factory = DeveloperEngineerFactory()
        
    def addTask(self, task):
        self.Task.append(task)

    def add_qa_engineer(self, engineer):
        self.engineers_qa.append(engineer)
        
    def add_dev_engineer(self, engineer):
        self.engineers_dev.append(engineer)
        
    def show_all_dev_engineer(Self):
        for engineer in Self.engineers_dev:
            print(f"Dev Engineer: {engineer.getName()} - {engineer.getRol()}")
        
    def show_all_qa_engineers(self):
        for engineer in self.engineers_qa:
            print(f"QA Engineer: {engineer.getName()} - {engineer.getRol()}")

        
    def toggle_task_fin(self, indexTask):
        if indexTask >= 0 and indexTask < len(self.Task):
            task = self.Task[indexTask]
            task.toggleFinished()
            print(f'The final status of the stak was changed {task.getDescription()}')
        else:
            print('The task index doesnt exist')
        

    def create_qa_engineer(self, name):
        return self.qa_factory.create_engineer(name)

    def create_dev_engineer(self, name):
        return self.dev_factory.create_engineer(name)
    
    def create_dev_task(self, description, duration, state, engineer):
        dev_task = DevTask(description, duration, state, engineer)
        self.Task.append(dev_task)
        return dev_task

    def create_qa_task(self, description, duration, state, engineer):
        qa_task = QaEngineerFactory(description, duration, state, engineer)
        self.Task.append(qa_task)
        return qa_task
    
    def adapt_to_qa(self, dev_task):
        adapterToQa = QaTaskAdapter(dev_task)
        self.Task.append(adapterToQa)
        return adapterToQa
    
    def adapt_to_dev(Self, qa_task):
        adapterToDev = DevTaskAdapter(qa_task)
        Self.Task.append(adapterToDev)
        return adapterToDev
        