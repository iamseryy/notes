from abc import ABC, abstractmethod


class Note_service(ABC):
    @abstractmethod
    def find_by_id(self, id):
        pass
