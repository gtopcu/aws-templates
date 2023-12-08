from abc import ABC, abstractmethod

# Utilizing the adapter pattern - use for all API/DB connections
class DbHandler(ABC):

    def __init__(self):
        pass
    
    @abstractmethod
    def insert(self, data):
        pass
    
    @abstractmethod
    def update(self, data):
        pass
    
    @abstractmethod
    def delete(self, data):
        pass
    
    @abstractmethod
    def get_by_id(self, data):
        pass

