from abc import ABC, abstractmethod

class StorageProvider(ABC):
    @abstractmethod
    def save(self,*args,**kwargs): ...
    @abstractmethod
    def delete(self,*args,**kwargs): ...
