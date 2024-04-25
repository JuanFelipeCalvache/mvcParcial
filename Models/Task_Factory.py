from abc import ABC, abstractmethod

class TaskFactory(ABC):
    @abstractmethod
    def create_task(self, description, duration, state, developer ):
        pass