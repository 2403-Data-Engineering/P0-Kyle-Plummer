from __future__ import annotations
from enum import Enum
from typing import TYPE_CHECKING

from presentation_layer.main_menu import MainMenu
from presentation_layer.new_student_menu import NewStudentMenu
from service_layer.student_service import StudentService


if TYPE_CHECKING:
    from presentation_layer.menu import Menu

class MenuEnum(Enum):
    MAIN_MENU = MainMenu()
    NEW_STUDENT_MENU = NewStudentMenu()


class Terminal:
    def __init__(self, student_service: StudentService):
        from presentation_layer.main_menu import MainMenu
        self.current_menu = MainMenu(self)
        self.running = True
        self.student_service = student_service


    def navigate(self, menu: MenuEnum):
        self.current_menu = menu.value

    def quit(self):
        self.running = False
        print("Quitting...")
