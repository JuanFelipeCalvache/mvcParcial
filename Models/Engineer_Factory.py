from abc import ABC, abstractmethod

class EngineerFactory(ABC):
    @abstractmethod
    def create_engineer(self, name, rol):
        pass
