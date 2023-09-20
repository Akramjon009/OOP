from abc import ABC, abstractmethod

class BaseRepository(ABC):
    @abstractmethod
    def creat(self):
        pass

    @abstractmethod
    def getall(self):
        pass

    def deleteById(self):
        pass

class Myclass(BaseRepository):
    def creat(self):
        pass
    def getall(self):
        pass
