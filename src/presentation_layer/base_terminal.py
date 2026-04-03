from abc import ABC, abstractmethod

class BaseTerminal(ABC):
    @abstractmethod
    def navigate(self, menu_name: str) -> None:
        pass