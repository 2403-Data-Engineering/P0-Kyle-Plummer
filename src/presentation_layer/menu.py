from __future__ import annotations

import re

from enum import Enum
from abc import abstractmethod
from typing import TYPE_CHECKING



if TYPE_CHECKING:
    from presentation_layer.terminal import Terminal

class Validator(Enum):
    EMAIL = "([\w.-]+)@([\w.-]+\.[a-zA-Z]{2,})"
    NAME = ".{2,}"
    YEAR = "Freshman|Sophmore|Junior|Senior"

class Menu:
    def __init__(self, terminal: Terminal):
        self.terminal:Terminal = terminal

    @abstractmethod
    def render() -> None:
        pass
    
    def get_input(self, prompt: str, validator: Validator=None) -> str:
        print(prompt)
        for i in range(3):
            input = input()
            if not validator:
                return input
            if re.fullmatch(input, validator):
                return input
            print("Invalid input, please try again.")
        print("Too many failed attempts...")
        self.terminal.quit()






