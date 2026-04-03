import re

from enum import Enum
from abc import ABC, abstractmethod
from presentation_layer.base_terminal import BaseTerminal

class Validator(Enum):
    EMAIL = "([\w.-]+)@([\w.-]+\.[a-zA-Z]{2,})"
    NAME = ".{2,}"
    YEAR = "Freshman|Sophmore|Junior|Senior"

class BaseMenu(ABC):
    def __init__(self, terminal: BaseTerminal):
        self.terminal:BaseTerminal = terminal

    @abstractmethod
    def render() -> None:
        pass
    
    def get_input(self, prompt: str, validator: Validator=None) -> str:
        print(prompt)
        for i in range(3):
            user_input = input()
            if not validator:
                return user_input
            if re.fullmatch(validator.value, user_input):
                return user_input
            print("Invalid input, please try again.")
        print("Too many failed attempts...")
        self.terminal.quit()


