from abc import ABC, abstractmethod

class ChatbotInterface(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def view_tree(self):
        pass
