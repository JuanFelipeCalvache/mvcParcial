from Models.Engineer_Factory import EngineerFactory
from Models.Engineer_Model import Engineer

class QaEngineerFactory(EngineerFactory):
    def create_engineer(self, name):
        return Engineer(name, "QA")
    
    
