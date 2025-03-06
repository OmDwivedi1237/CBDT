from abc import ABC, abstractmethod

class BaseTree(ABC):
    @abstractmethod
    def insert(self, question, yes_answer, no_answer):
        pass

    @abstractmethod
    def search(self, question):
        pass

    @abstractmethod
    def traverse(self, order="inorder"):
        pass
