from abc import ABC, abstractmethod


class Notes(ABC):
    @abstractmethod
    def find_by_id(self, id):
        pass
