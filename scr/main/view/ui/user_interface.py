from abc import ABC, abstractmethod


class User_interface(ABC):
    @abstractmethod
    def output(self):
        pass