class Engineer_View:
    
    def __init__(self, controller):
        self.contoller = controller
        pass
        
    def show_all_qa_engineers(self):
        self.contoller.show_all_qa_engineers()
        pass
    
    def show_all_dev_engineers(self):
        self.contoller.show_all_dev_engineer()
    
    def showAllTasks(self):
         self.contoller.showAllTasks()
         pass   
    
    def showFinishedTask(Self,  tasks: list):
        for e in tasks:
            if e.getFinished():
                print(e.getDescription())
    
    def showUnfinishedTasks(self, tasks):
        for e in tasks:
            if not e.getFinished():
                print(e.getDescription())
    
    def getUserInput(self):
        return input("Ingrese el indice de la tarea: ")
    
    def finishTask(self, numTask):
        pass
    
    def addTask(self, newTask):
        pass
