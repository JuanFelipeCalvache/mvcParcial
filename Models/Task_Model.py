#Task States develop (start, executing, finished)
#Task States testing (Proposed, testing, (certified returned))

class Task:
    
    def __init__(self, description, duration, state, engineer):
        self.description = description
        self.duration = duration
        self.state = state
        self.engineer = engineer
        self.finished = False
    
    def changeDuration(self, newDuration):
        self.duration = newDuration
        
    def changeState(self, newState):
        self.state = newState
    
    def getState(self):
        return self.state
    
    def getDuration(self):
        return self.duration
    
    def getEngineerName(self):
        return self.engineer.getName()
    
    def getEntineerRol(self):
        return self.engineer.getRol()
        
    def finishTask(self):
        self.finished = True
        
    def toggleFinished(self):
        self.finished = not self.finished
    
    def getFinished(self):
        return self.finished
    
    def getDescription(self):
        return self.description