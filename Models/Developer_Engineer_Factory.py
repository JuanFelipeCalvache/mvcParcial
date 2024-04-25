from Models.Engineer_Factory import EngineerFactory
from Models.Engineer_Model import Engineer

class DeveloperEngineerFactory(EngineerFactory):
    def create_engineer(self, name):
        return Engineer(name, "Developer")
